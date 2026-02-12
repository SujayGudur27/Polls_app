Django Polls Application

A complete implementation of the official Django tutorial (Parts 1–8), covering core Django concepts including models, views, templates, forms, testing, admin customization, static files, and third-party integrations.

Overview

This project is a web-based polling system built using Django.

It allows:

Admin users to create questions and multiple choices

Users to vote on questions

Display of real-time results

Filtering of unpublished (future) questions

Automated validation through testing

Admin UI customization

Static styling with CSS and images

Debugging using Django Debug Toolbar

Architecture

This project follows Django’s MTV (Model–Template–View) architecture.

URL → View → Model (ORM) → Template → HTTP Response


Model: Defines database structure and business logic

View: Handles request and returns response

Template: Handles presentation layer

URLconf: Maps URLs to views

Features Implemented
Models (Database Layer)

Question model

Choice model

One-to-many relationship using ForeignKey

Custom model method: was_published_recently()

Timezone-aware filtering using timezone.now()

Database migrations applied

Views and Routing

Class-Based Generic Views:

ListView (IndexView)

DetailView (DetailView)

DetailView (ResultsView)

Custom function-based vote() view

URL namespacing

Query filtering using get_queryset()

Exclusion of future-dated questions

Form Handling and Voting

HTML form with POST method

CSRF protection

F() expressions for atomic updates

Post/Redirect/Get pattern

Reverse URL resolution using reverse()

Automated Testing

Implemented both model tests and view tests.

Model Tests

Future question validation

Old question validation

Recently published logic validation

View Tests

Index page behavior

Future question exclusion

Multiple question ordering

Detail view restrictions

Run tests using:

python manage.py test


All tests run in an isolated temporary test database.

Static Files and Styling

Static file structure using namespacing

Custom CSS styling

Background images

Responsive styling improvements

Static file loading using {% load static %}

Directory structure:

polls/
└── static/
    └── polls/
        ├── style.css
        └── images/

Admin Customization

Enhanced Django’s built-in admin panel:

Custom ModelAdmin

Field grouping using fieldsets

Inline editing using TabularInline

Custom columns using list_display

Filters using list_filter

Search functionality using search_fields

Boolean column customization using @admin.display

Admin branding customization

Custom admin CSS styling

Third-Party Integration

Integrated Django Debug Toolbar for development debugging.

Configured:

INSTALLED_APPS

MIDDLEWARE

Debug URLs

INTERNAL_IPS

Toolbar provides:

SQL query inspection

Template rendering details

Static file tracking

Request/response debugging

Settings inspection

Technologies Used

Python

Django 6.x

SQLite

HTML

CSS

Django ORM

Django Generic Views

Django Testing Framework

Django Admin

Django Debug Toolbar

Project Structure
mysite/
│
├── manage.py
├── db.sqlite3
│
├── mysite/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── polls/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    ├── tests.py
    ├── templates/
    └── static/

How to Run the Project

Clone the repository

git clone <repository-url>
cd <project-folder>


Create virtual environment

python -m venv venv
venv\Scripts\activate


Install dependencies

pip install -r requirements.txt


Apply migrations

python manage.py migrate


Create superuser

python manage.py createsuperuser


Run development server

python manage.py runserver


Access:

Polls App: http://127.0.0.1:8000/polls/

Admin Panel: http://127.0.0.1:8000/admin/