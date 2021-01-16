from django.shortcuts import render
from .models import Category, Tag, Post, General
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    general = General.objects.first()
    page = request.GET.get('page', '')
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 1)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/home.html', {
        'general': general,
        'posts': posts,
        'categories': categories,
        'tags': tags,
    })


def category(request, slug):
    general = General.objects.first()
    posts = Post.objects.filter(category__slug=slug)
    requested_category = Category.objects.get(slug=slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    return render(request, 'blog/category.html', {
        'general': general,
        'posts': posts,
        'category': requested_category,
        'categories': categories,
        'tags': tags,
    })


def tag(request, slug):
    general = General.objects.first()
    posts = Post.objects.filter(tag__slug=slug)
    requested_tag = Tag.objects.get(slug=slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    return render(request, 'blog/tag.html', {
        'general': general,
        'posts': posts,
        'tag': requested_tag,
        'categories': categories,
        'tags': tags,
    })


def post(request, slug):
    general = General.objects.first()
    requested_post = Post.objects.get(slug=slug)
    posts = Post.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    post_tags = requested_post.tag.values_list('id', flat=True)
    related_posts = Post.objects.filter(tag__in=post_tags).exclude(id=requested_post.id)

    return render(request, 'blog/post.html', {
        'general': general,
        'post': requested_post,
        'posts': posts,
        'categories': categories,
        'tags': tags,
        'related_posts': related_posts,
    })


def search(request):
    general = General.objects.first()
    query = request.GET.get('q', '')
    if query:
        posts = Post.objects.filter(title__icontains=query)
    else:
        posts = []
    return render(request, 'blog/search.html', {
        'general': general,
        'posts': posts,
        'query': query,
    })
