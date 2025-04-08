from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import HttpResponseForbidden
from django.urls import reverse
from .models import Question, Answer, Like
from .forms import AnswerForm, QuestionForm

def home(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'core/home.html', {'questions': questions})

def register_view(request):
    if request.method == 'POST':
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
        login(request, user)
        return redirect('home')
    return render(request, 'core/register.html')

def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('home')  # or wherever
    else:
        form = QuestionForm()
    return render(request, 'core/post_question.html', {'form': form})


def view_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    form = AnswerForm()
    if request.method == 'POST' and request.user.is_authenticated:
        Answer.objects.create(
            # content=request.POST['answer'],
            content = request.POST.get('answer'),
            question=question,
            author=request.user
        )
        return HttpResponseRedirect(reverse('view_question', args=[question.id]))
    
    return render(request, 'core/view_question.html', {'question': question, 'form': form})

@login_required
def like_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    Like.objects.get_or_create(answer=answer, user=request.user)
    return HttpResponseRedirect(reverse('view_question', args=[answer.question.id]))


@login_required
def delete_question(request, pk):
    question = get_object_or_404(Question, pk=pk)

    # if question.user != request.author:
    if request.user != question.author:

        return HttpResponseForbidden("You are not allowed to delete this question.")

    question.delete()
    return redirect('home')
