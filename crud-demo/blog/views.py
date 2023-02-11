from django.shortcuts import redirect, render
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, "post/list.html", {"posts": posts})


def post_show(request, id):
    post = Post.objects.get(pk=id)
    return render(request, "post/show.html", {"post": post})


def post_create(request):
    if request.method == "GET":
        return render(request, "post/create.html")
    elif request.method == "POST":
        post = Post(title=request.POST["title"], content=request.POST["content"])
        post.save()
        return redirect("home")


def post_update(request, id):
    if request.method == "GET":
        post = Post.objects.get(pk=id)
        return render(request, "post/update.html", {"post": post})
    elif request.method == "POST":
        post = Post.objects.update_or_create(
            pk=id,
            defaults={
                "title": request.POST["title"],
                "content": request.POST["content"],
            },
        )

        # post.title = request.POST["title"]
        # post.content = request.POST["content"]
        # post.save()
        return redirect("home")


def post_delete(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect("home")
