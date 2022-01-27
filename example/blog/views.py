from django.shortcuts import render
from blog.models import Home

# Create your views here.
"""
def my_view(request):
    posts = Post.objects.all()

    return render(request, 'blog/index.html', {
        'posts': posts,
    })

def test(request):
    post = Post.objects.get(pk=1)

    return render(request, 'test.html', {
        'post': post
    })
"""

def show(request):
    home  = Home.objects.get(pk=0)

    title = home.title
    description = home.description
    logo = home.logo

    return render(request, 'home.html', {
        'title': title,
        'description': description,
        'logo': logo,
    })

def create(request):
    title = "Create a new Home"

    return render(request, 'create.html', {
        'title': title,
    })

def save(request):
    home = Home(
        title = request.title,
        description = request.description,
        logo = request.logo,
    )

    home.save()

    return render(request, 'success.html', {
        'title': "Success",
    })