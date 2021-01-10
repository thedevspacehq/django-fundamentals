# Django 3.1 Tutorial For Beginners

![Django Tutorial For Beginners](https://miro.medium.com/max/1000/1*YT-sRZ4MxOGGiEnZCourMQ.png)

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Just like Laravel, Django aims to ease the construction of complex, database-driven web applications. Again, in this Django tutorial for beginners, we’ll talk about the key features of Django by building a simple blog.

You can download the source code of this tutorial here.

https://www.techjblog.com/index.php/django-tutorial-for-beginners/

## Part One: Django Basics

Before we can start building our project, we need to talk about some basic concepts in Django. Let’s start by making some preparations, install the necessary software, create a new Django project, and then, we need to understand the MTV structure, which is commonly used by most of the web frameworks. And finally, we’ll talk about Django Admin, the built-in admin panel for Django applications.

[Django Tutorial #1: Setup the Project](https://www.techjblog.com/index.php/2020/11/django-tutorial-1-setup-the-project/)

[Django Tutorial #2: URL Configuration](https://www.techjblog.com/index.php/2020/11/django-tutorial-2-url-configuration/)

[Django Tutorial #3: The MTV Structure](https://www.techjblog.com/index.php/2020/11/django-tutorial-3-the-mtv-structure/)

[Django Tutorial #4: Admin Panel](https://www.techjblog.com/index.php/2020/12/django-tutorial-4-admin-panel-2/)

## Part Two: Build A Blog

[Django Tutorial #5: Create the Home Page](https://www.techjblog.com/index.php/2020/12/django-tutorial-5-create-the-home-page/)

One of the most important steps of web development is to design the database structure. In this tutorial, we’ll make four database tables together.

The `users` table stores the user name, email and password. The model for this table is already included in Django. The `categories` and `tags` tables store the category names and tag names. And finally, the `posts` table stores the post title, content, post image and so on.

However, just creating the tables is not enough. The tables have relationships with each other. This part could be a little tough for beginners, I will try to make it easy to understand.

[Django Tutorial #6: Create Models and Setup Admin Panel](https://www.techjblog.com/index.php/2020/12/django-tutorial-6-create-models-and-setup-admin-panel/)

URLs are the entry points when someone visits your blog. They receive URLs and returns views. Views retrieve data from the database through models and put them in templates. Templates are what we actually see in the browser, so they do look like HTML and CSS. However, things are more complicated than that.

[Django Tutorial #7: Create Views and Templates](https://www.techjblog.com/index.php/2020/12/django-tutorial-7-create-views-and-templates/)

In the next two articles, we’ll build search, pagination and some other optional features for our project. However, if you are not interested, feel free to jump to the end, and we can finally deploy our application.

[Django Tutorial #8: Search](https://www.techjblog.com/index.php/2020/12/django-tutorial-8-search/)

[Django Tutorial #9: Wrap Things Up](https://www.techjblog.com/index.php/2021/01/django-tutorial-9-wrap-things-up/)

[Django Tutorial #10: Deployment](https://www.techjblog.com/index.php/2021/01/django-tutorial-10-deployment/)

[How to Deploy A Django Project](https://www.techjblog.com/index.php/2020/07/how-to-deploy-a-django-project/)

[Build A Single Page App Using Django & Vue.js](https://www.techjblog.com/index.php/2020/08/build-a-single-page-app-using-django-vue-js/)

## Other Resources

[Some Useful Tools For Web Development Using Python](https://www.techjblog.com/index.php/2020/05/some-useful-tools-for-web-development-using-python/)

[Django Official Documentation](https://www.djangoproject.com/)
