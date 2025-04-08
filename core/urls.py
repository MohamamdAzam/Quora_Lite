from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('ask/', views.ask_question, name='ask_question'),
    path('question/<int:question_id>/', views.view_question, name='view_question'),
    path('like/<int:answer_id>/', views.like_answer, name='like_answer'),
    path('question/<int:pk>/delete/', views.delete_question, name='delete_question'),
]


