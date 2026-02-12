# Polls App (Django)

Django Polls Application

This project is a complete implementation of the official Django tutorial (Parts 1–8). It demonstrates building a full-stack web application using Django, covering models, views, templates, forms, admin customization, testing, static files, and third-party integrations.

Project Overview

The application is a simple polling system where:

Admin users can create questions and multiple choices.

Users can vote on questions.

Results are displayed dynamically.

Only published questions are visible to users.

Automated tests validate application logic.

The Django admin interface is customized.

Static styling and images are integrated.

Django Debug Toolbar is configured for development debugging.

Features Implemented
1. Models and Database (Part 1 & 2)

Created Question and Choice models.

Implemented one-to-many relationship using ForeignKey.

Added custom model method was_published_recently().

Used Django ORM for database interaction.

Applied migrations to manage schema changes.

Registered models in Django Admin.

2. Views, URLs, and Templates (Part 3)

Implemented class-based generic views:

IndexView (ListView)

DetailView (DetailView)

ResultsView (DetailView)

Connected views using URL configuration.

Used template inheritance and Django Template Language.

Implemented URL namespacing.

Filtered unpublished (future) questions using get_queryset().

Flow:
URL → View → ORM → Template → HTTP Response

3. Form Handling and Voting Logic (Part 4)

Converted detail page into an HTML form.

Used POST method for data submission.

Added CSRF protection.

Implemented voting logic in vote() view.

Used F() expressions to avoid race conditions.

Implemented Post/Redirect/Get pattern.

Used reverse() for dynamic URL resolution.

4. Automated Testing (Part 5)

Wrote model tests for:

Future questions

Old questions

Recently published questions

Wrote view tests for:

Index page behavior

Future question exclusion

Detail view restrictions

Used Django’s TestCase.

Used Django test client for request simulation.

Tests run in isolated test database.

Command to run tests:

python manage.py test

5. Static Files and Styling (Part 6)

Added custom CSS styling.

Added background images.

Used {% load static %} template tag.

Organized static files using namespacing:

polls/static/polls/


Customized Django Admin background and styling.

6. Admin Customization (Part 7)

Created custom QuestionAdmin.

Used:

fieldsets

list_display

list_filter

search_fields

Implemented inline editing using TabularInline.

Used @admin.display decorator for custom boolean column.

Customized admin branding using template override.

7. Third-Party Integration (Part 8)

Installed Django Debug Toolbar.

Configured:

INSTALLED_APPS

MIDDLEWARE

Debug URLs

INTERNAL_IPS

Used toolbar panels to inspect:

SQL queries

Templates

Static files

Headers

Settings

Request lifecycle

Technologies Used

Python

Django 6.x

SQLite

HTML

CSS

Django ORM

Django Generic Views

Django Admin

Django Test Framework

Django Debug Toolbar

Project Structure
mysite/
│
├── mysite/                # Project settings
├── polls/                 # Application
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── tests.py
│   ├── templates/
│   └── static/
│
├── manage.py
└── db.sqlite3

How to Run the Project

Clone the repository:

git clone <repository-url>


Create and activate virtual environment:

python -m venv venv
venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Apply migrations:

python manage.py migrate


Create superuser:

python manage.py createsuperuser


Run development server:

python manage.py runserver


Access:

Polls: http://127.0.0.1:8000/polls/

Admin: http://127.0.0.1:8000/admin/

Key Learning Outcomes

Understanding Django’s MTV architecture.

Working with ORM instead of raw SQL.

Building class-based views.

Handling forms and POST requests securely.

Writing automated tests.

Customizing Django Admin.

Managing static files properly.

Integrating third-party Django packages.