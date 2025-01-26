from django.shortcuts import render, HttpResponse, redirect
import random
from django.template.defaultfilters import title
from posts.models import Post
from posts.forms import PostCreateForm
from django.contrib.auth.decorators import login_required


def main_view(request):
    if request.method == "GET":
        return render(request, "main.html")

@login_required(login_url="/login/")
def posts_list_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request, "posts/posts_list.html", {"posts": posts})

@login_required(login_url="/login/")
def post_detail_view(request, post_id):
    if request.method == "GET":
        post = Post.objects.get(id=post_id)
        return render(request, "posts/post_detail.html", {"post": post})


@login_required(login_url="/login/")
def post_create_view(request):
    if request.method == "GET":
        form = PostCreateForm()
        return render(request, "posts/post_create.html", context={"form": form})
    if request.method == "POST":
        form = PostCreateForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, "posts/post_create.html", context={"form": form})
        elif form.is_valid():
            form.save()
            return redirect("/posts/")

# Create your views here.
