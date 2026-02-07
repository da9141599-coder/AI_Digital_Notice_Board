# AI Digital Notice Board

An AI-enabled web-based Digital Notice Board developed using Django.

## Features
- Role-based access (Admin, Teacher, Student)
- Notice creation and viewing
- AI-based priority classification
- Voice-assisted notice description
- Responsive UI (Mobile + Desktop)
- Secure authentication

## Tech Stack
- Backend: Django 4.2
- Frontend: HTML, Bootstrap 5
- Database: SQLite (can be upgraded to MySQL/PostgreSQL)
- AI/NLP: NLTK, Scikit-learn

## How to Run Locally
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
