from django.shortcuts import render, HttpResponse, redirect
import random
from django.template.defaultfilters import title
from django.db.models import Q
from unicodedata import category

from posts.models import Post
from posts.forms import PostCreateForm, SearchForm
from django.contrib.auth.decorators import login_required


def main_view(request):
    if request.method == "GET":
        return render(request, "main.html")

@login_required(login_url="/login/")
def posts_list_view(request):
    search_form = SearchForm()
    if request.method == "GET":
        search = request.GET.get("search")
        category = int(request.GET.get("category")) if request.GET.get("category") else None
        ordering = request.GET.get("ordering")
        page = int(request.GET.get("page")) if request.GET.get("page") else 1
        posts = Post.objects.all()
        if search:
            posts = posts.filter(Q(title__icontains=search) | Q(description__icontains=search))
        if category:
            posts = posts.filter(category_id=category)

        if ordering:
            posts = posts.order_by(ordering)


        limit = 3
        max_pages = posts.count() / limit
        if round(max_pages) < max_pages:
            max_pages = round(max_pages) + 1
        else:
            max_pages = round(max_pages)

        start = (page - 1) * limit
        end = page * limit

        posts = posts[start:end]

        context_data = {"posts": posts, "search_form": search_form, "max_pages": range(1, max_pages + 1)}


        return render(request, "posts/posts_list.html", context=context_data)

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
