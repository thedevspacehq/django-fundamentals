from django.shortcuts import redirect, render
from .models import Site, Category, Tag, Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

n = 2

# Create your views here.
def home(request):
    site = Site.objects.first()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    featured_post = Post.objects.filter(is_featured=True).first()

    # Add Paginator
    page = request.GET.get("page", "")  # Get the current page number
    posts = Post.objects.all().filter(is_published=True)
    paginator = Paginator(posts, n)  # Showing n post for every page

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(
        request,
        "home.html",
        {
            "site": site,
            "posts": posts,
            "categories": categories,
            "tags": tags,
            "featured_post":featured_post
        },
    )


def category(request, slug):
    site = Site.objects.first()
    requested_category = Category.objects.get(slug=slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    # Add Paginator
    page = request.GET.get("page", "")  # Get the current page number
    posts = Post.objects.filter(category__slug=slug).filter(is_published=True)
    paginator = Paginator(posts, n)  # Showing 1 post for every page

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(
        request,
        "category.html",
        {
            "site": site,
            "posts": posts,
            "category": requested_category,
            "categories": categories,
            "tags": tags,
        },
    )


def tag(request, slug):
    site = Site.objects.first()
    posts = Post.objects.filter(tag__slug=slug).filter(is_published=True)
    requested_tag = Tag.objects.get(slug=slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    # Add Paginator
    page = request.GET.get("page", "")  # Get the current page number
    posts = Post.objects.filter(tag__slug=slug).filter(is_published=True)
    paginator = Paginator(posts, n)  # Showing 1 post for every page

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(
        request,
        "tag.html",
        {
            "site": site,
            "posts": posts,
            "tag": requested_tag,
            "categories": categories,
            "tags": tags,
        },
    )


def post(request, slug):
    site = Site.objects.first()
    requested_post = Post.objects.get(slug=slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    # Related Posts

    # Get all the tags related to this article
    post_tags = requested_post.tag.all()
    # Filter all posts that contain tags that are related to the current post, and exclude the current post
    related_posts_ids = (
        Post.objects.all()
        .filter(tag__in=post_tags)
        .exclude(id=requested_post.id)
        .values_list("id")
    )
    print(related_posts_ids)
    related_posts = Post.objects.filter(pk__in=related_posts_ids)

    return render(
        request,
        "post.html",
        {
            "site": site,
            "post": requested_post,
            "categories": categories,
            "tags": tags,
            "related_posts": related_posts,
        },
    )


def search(request):
    site = Site.objects.first()
    categories = Category.objects.all()
    tags = Tag.objects.all()

    query = request.POST.get("q", "")
    if query:
        posts = Post.objects.filter(is_published=True).filter(title__icontains=query)
    else:
        posts = []
    return render(
        request,
        "search.html",
        {
            "site": site,
            "categories": categories,
            "tags": tags,
            "posts": posts,
            "query": query,
        },
    )
