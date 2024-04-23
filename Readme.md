
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


---

## Lesson 3:

- ORM Intro
- Adding **'\__str\__'** method to Post model to show post title whenever a post is shown:

      def __str__(self):
        return self.title

A quick way to try and play with the Django ORM is by using the shell this way:

    py manage.py shell

From there the Post model can be imported to perform several operations:

    from posts.models import Post

To create a Post object:

    p = Post()

To set values for the attributes:

    p.title = "First Post"
    p.body = "First Post body text"

Now the Post object can be saved into the database:

    p.save()

Finally it's possible to get all posts from the database:

    Post.objects.all()

  - Expected result:

      <QuerySet [<Post: First post>]>

To exit from the shell, execute:

    exit()

![alt text](image-3.png)



---

## Lesson 4:

- Django Admin Introduction
- An user must be created to access to /admin panel:

      py manage.py createsuperuser

  - User created: admin
  - Password: admin123

- Posts can be manipulated by using the admin panel, but first it's requeried to "register" the Post model:
  - Add to '**_posts/admin.py_**', the following lines:


        from .models import Post
        admin.site.register(Post)

  - Next, access to http://localhost:8000/admin
    - A CMS web interface is available to manipulate (CRUD operations available) posts, users and groups.

![alt text](image-5.png)

- To show posts list, posts must be retrieved from the database by using Django ORM, and then passing it to the render method:

      def posts_list(request):
        posts = Post.objects.all().order_by('-date')
        return render(request, 'posts/posts_list.html', { 'posts': posts })
    - By using '-date' param, it will retrive posts in descending order.

- Finally, the HTML template must iterate the posts list to show the posts, it can be done by using a for loop:

      {% for post in posts %}
        <article  class="posts">
          <h2>{{ post.title }}</h2>
          <p>{{ post.date }}</p>
          <p>{{ post.body }}</p>
        </article>
      {% endfor %}

![alt text](image-4.png)