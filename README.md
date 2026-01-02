# Cake World – Django Menu Application

## Project Overview

Cake World is a Django-based web application that displays a cake menu with product images, names, prices, and descriptions.
The application is built using **Django for the backend** and **pure HTML and CSS for the frontend**.

This project focuses on understanding Django fundamentals and custom CSS-based UI design.

---

## Features

* Displays a list of cake products
* Each product includes:

  * Image
  * Name
  * Price
  * Description
* Custom-designed UI using CSS
* Responsive layout using standard CSS
* Django template rendering
* SQLite database support

---

## Technologies Used

* Python
* Django
* HTML5
* CSS3
* SQLite3
* Git and GitHub

---

## Project Structure

```
django-cakeworld-menu/
│
├── cakeworld/              # Main Django project
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── menu/                   # Application for cake menu
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── templates/
│   └── menu.html
│
├── static/
│   └── css/
│       └── style.css
│
├── media/
│   └── cakes/
│
├── db.sqlite3
├── manage.py
└── README.md
```

---

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/Aneetapaul7/django-cakeworld-menu.git
cd django-cakeworld-menu
```

---

### Step 2: Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Mac / Linux**

```bash
source venv/bin/activate
```

---

### Step 3: Install Django

```bash
pip install django
```

---

### Step 4: Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### Step 5: Run the Server

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

## Sample Products

* Chocolate Truffle Cake
* Red Velvet Cake
* Black Forest Cake
* Pineapple Cake
* Strawberry Cream Cake
* Vanilla Birthday Cake

---

## Purpose of the Project

* Practice Django project and app structure
* Learn template rendering and static file handling
* Improve CSS layout and styling skills
* Understand media file configuration in Django
* Create a beginner-friendly, interview-ready project

---

## Future Improvements

* Add cart functionality
* Add quantity and total price calculation
* Implement user authentication
* Improve mobile responsiveness
* Add admin product management UI

---



