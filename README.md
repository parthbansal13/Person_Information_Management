#Person Information Management

This is a simple full-stack web application for storing and viewing person information.

The application allows the user to enter personal and address details through a web form. The data is sent to a Django REST API and stored in a SQL database. The saved records can be viewed on the Person List page.

#Project Structure

Person_Information_Management/

├── frontend/
│   ├── templates/
│   │   ├── add_person.html
│   │   └── person_list.html
│   │
│   └── static/
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── script.js
│
├── backend/
│   ├── manage.py
│   │
│   ├── config/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   └── persons/
│       ├── admin.py
│       ├── models.py
│       ├── serializers.py
│       ├── urls.py
│       ├── views.py
│       └── migrations/
│
├── database/
│   └── db.sqlite3
│
├── requirements.txt
├── README.md
└── .gitignore

Technologies Used :-
HTML
CSS
JavaScript
Python
Django
Django REST Framework
SQLite
MySQL

Features:-
Add a new person
Store person information in the database
View all saved person records
REST API for creating and retrieving records
Frontend validation
Backend validation
Error messages for invalid data
SQLite and MySQL database support


The application stores the following information:-
Person Name
Mobile Number
Age
City
State
Post Code
Full Address

How to Run :-

First, open the project folder in VS Code or a terminal.

Create a virtual environment:
python -m venv venv

Activate the virtual environment on Windows:
venv\Scripts\activate

Install the required packages:
pip install -r requirements.txt

Go to the backend folder:
cd backend

Run the migrations:
python manage.py migrate

Start the Django server:
python manage.py runserver

The application will run at:
http://127.0.0.1:8000/

Pages:-

Add Person:
http://127.0.0.1:8000/

Person List:
http://127.0.0.1:8000/persons/

API:-

The application provides a REST API for person records.

Api for Create Person:-
POST /api/persons/
This API is used to add a new person record.

Example request:
{
    "person_name": "Rahul Sharma",
    "mobile_number": "9876543210",
    "age": 22,
    "city": "Harda",
    "state": "Madhya Pradesh",
    "post_code": "461331",
    "full_address": "123 Main Road, Harda"
}

Api for Get Person Records:-
GET /api/persons/
This API returns the person records stored in the database.

Database Used:-

The project supports both SQLite and MySQL.

SQLite is useful for running the project locally without setting up a separate database server. The SQLite database file is stored in database/db.sqlite3

MySQL can also be configured in Django's settings.py and used as the project's SQL database.

The database table is created from the Django model and migrations.

Model: backend/persons/models.py

Migrations: backend/persons/migrations/

The project uses Django ORM for communicating with the database.

Validation :-

Validation is implemented on both the frontend and backend.

The application checks:

Person name
Mobile number
Age
City
State
Post code
Full address

Frontend validation gives the user immediate feedback before sending the request.

Backend validation checks the data again before saving it to the database.

API and Database Flow:-

The basic flow of the application is:

User
  ↓
HTML Form
  ↓
JavaScript
  ↓
Django REST API
  ↓
Serializer
  ↓
Django Model / ORM
  ↓
SQLite or MySQL

Requirements:-

Make sure Python and the required database setup are available on the system.

Install the Python dependencies using:
pip install -r requirements.txt

For MySQL, make sure the MySQL server is running and the database connection details in Django settings are configured correctly.

Author :-
Developed as a full-stack development assignment using Python, Django, Django REST Framework, JavaScript and SQL databases.