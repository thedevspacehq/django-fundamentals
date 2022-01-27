from django.db import models


# Create your models here.
"""
# One-to-one relation
class Person(models.Model):
    name = models.CharField(max_length=100)


class Phone(models.Model):
    person = models.OneToOneField('Person', on_delete=models.CASCADE)


# Many-to-one relation
class Category(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


# Many-to-many relation
class Tag(models.Model):
    name = models.CharField(max_length=100)

class Article(models.Model):
    tags = models.ManyToManyField('Tag')
"""

"""
class Category(models.Model):
    name = models.CharField(max_length=100)


class Author(models.Model):
    name = models.CharField(max_length=200)


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)
"""

class Home(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to='uploads/images/logo')