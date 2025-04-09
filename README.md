
# Quora Lite 📝

A simple Quora-like web application built with Django. Users can register, ask questions, answer others' questions, and like answers.

---
### Live - Click Here : https://quora-lite.onrender.com/
---

## 🔧 Features

- User registration & login
- Ask & delete questions (only by author)
- Submit answers to questions
- Like answers
- Responsive frontend (Bootstrap)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/MohamamdAzam/Quora_Lite.git
cd Quora_Lite
```

### 2. Set Up Virtual Environment

```bash
python -m venv env
env\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run the Server

```bash
python manage.py runserver
```

Go to `http://127.0.0.1:8000` in your browser.

---

## ✅ Frontend Testing Instructions

### 🏠 Home Page

- Visit `/` to see all questions.
- Click on any question to view answers.

### 📝 Ask a Question

- Go to `/ask/` (requires login)
- Fill title & content → Submit → Redirects to home.

### 📥 Answer a Question

- Visit `/question/<id>/`
- Scroll down to **"Write your answer"**
- Submit an answer → Should appear above instantly.

### ❤️ Like an Answer

- Click the like button → Count should increment.

### ❌ Delete a Question

- Only visible if you're the question author.
- Click "Delete" → Should redirect to home.

---


## 💡 Author

**Mohammad Azam**  
GitHub: [@MohamamdAzam](https://github.com/MohamamdAzam)

---

## 📄 License

MIT License
