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
    home  = Home.objects.first()

    title = home.title
    description = home.description
    logo = home.logo.url

    return render(request, 'home.html', {
        'title': title,
        'description': description,
        'logo': logo,
    })

def create(request):

    return render(request, 'create.html', {
        'title': "Create a new Home",
    })

def save(request):
    home = Home(
        title = request.POST.get('title', ''),
        description = request.POST.get('description', ''),
        logo = request.FILES['logo'],
    )

    home.save()

    return render(request, 'success.html', {
        'title': "Success",
        'description': "Successfully Saved"
    })

def delete(request):
    home  = Home.objects.first()

    home.delete()

    return render(request, 'success.html', {
        'title': "Success",
        'description': "Successfully Deleted"
    })