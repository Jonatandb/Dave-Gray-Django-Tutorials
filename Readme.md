
# [Dave Gray - Django Tutorials](https://www.youtube.com/playlist?list=PL0Zuz27SZ-6NamGNr7dEqzNFEcZ_FAUVX)

---

Note: To follow the tutorial playlist and make a new project for each lesson, I made a script called '_**clone_folder_and_increase_version.py**_' that creates a copy of the previous lesson folder and updates version numbers (in folders and files) accordingly (Thanks ChatGPT ♥)

---

## Lesson 0:
- Project creation
- Rendering of html templates
- Config and use of paths and static files (css, js)

Create env (only the first time):

  ```py -m venv venv```

Activate env:

  ```source venv/Scripts/activate```

Install Django (only the first time):

    pip install django

Create a new Django project:

    django-admin startproject lesson0

Start app:

    cd lesson0

    py manage.py runserver

Visit App:

  - http://localhost:8000

![alt text](image.png)

---

## Lesson 1:
- App creation
- App configuration
- Using of namespaced templates
- VSCode Emmet configuration for Django HTML files
- Creation and use of "Base layout" template

Create a new Django app:

    py manage.py startapp posts

Add new 'posts' app to INSTALLED_APPS on settings.py

Add new 'templates/layout.html' file with ```{% block title %}``` and  ```{% block content %}``` placeholders

Update 'homepage.html' and 'about.html' to extends and use base layout by adding ```{% extends 'layout.html' %}``` and specifing blocks content.

Also add a new posts/templates/posts/posts.list.html file with ```{% extends 'layout.html' %}```

Add posts/urls.py and update lesson1/urls.py to include the posts urls.

Start app:

    cd lesson1

    py manage.py runserver

Visit App:

  - http://localhost:8000
  - http://localhost:8000/about
  - http://localhost:8000/posts

![alt text](image-1.png)

![alt text](image-2.png)


---

## Lesson 2:

- Model and migrations

Create a class called Post inside posts/models.py (must inherit from models.Model)

Define fields (more info: https://docs.djangoproject.com/en/5.0/ref/models/fields/)

Apply base app migrations by running:

    py manage.py migrate

Create migration for new Post model:

    py manage.py makemigrations
  - A new 'posts\migrations\0001_initial.py' file will be created.

Apply migrations:

    py manage.py migrate
  - This creates Post model (_**table**_) on the database.
