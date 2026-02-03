# Polls App (Django)

This repository contains a basic Django application created as part of my Day 1 setup. I followed the official Django tutorial to set up the project and build a simple polls app. The application runs locally on port 8000 using Django’s development server and uses SQLite as the database.

## What I’ve done
- Set up a Django project
- Created a polls app with URL routing
- Added models for Questions and Choices
- Applied database migrations
- Added a `requirements.txt` for dependencies

## How to run the project

1. Clone the repository
```bash
git clone https://github.com/SujayGudur27/Polls_app.git
cd Polls_app
Create and activate a virtual environment

python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate # macOS/Linux
Install dependencies

pip install -r requirements.txt
Run migrations

python manage.py migrate
Start the server

python manage.py runserver
Open the app in the browser:

http://127.0.0.1:8000/polls/

Notes
This project is part of Day 1 learning and setup.

The polls page currently returns a simple response.

More features will be added as I continue learning Django.


Demo (Day 1)



Loom walkthrough of Day 1 setup:
https://www.loom.com/share/aad676821ae04050aab30cc6805fa9e5