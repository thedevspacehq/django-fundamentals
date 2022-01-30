from django.shortcuts import render
from .models import Site, Category, Tag, Post

# Create your views here.


def home(request):
    site = Site.objects.first()
    posts = Post.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()

    return render(request, 'home.html', {
        'site': site,
        'posts': posts,
        'categories': categories,
        'tags': tags,
    })


def category(request, slug):
    site = Site.objects.first()
    posts = Post.objects.filter(category__slug=slug)
    requested_category = Category.objects.get(slug=slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    return render(request, 'category.html', {
        'site': site,
        'posts': posts,
        'category': requested_category,
        'categories': categories,
        'tags': tags,
    })


def tag(request, slug):
    site = Site.objects.first()
    posts = Post.objects.filter(tag__slug=slug)
    requested_tag = Tag.objects.get(slug=slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    return render(request, 'tag.html', {
        'site': site,
        'posts': posts,
        'tag': requested_tag,
        'categories': categories,
        'tags': tags,
    })


def post(request, slug):
    site = Site.objects.first()
    requested_post = Post.objects.get(slug=slug)
    posts = Post.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()

    return render(request, 'post.html', {
        'site': site,
        'post': requested_post,
        'posts': posts,
        'categories': categories,
        'tags': tags,
    })
