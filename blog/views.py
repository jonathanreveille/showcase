from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import Post, Category
# from .forms import SearchedPostForm


def blog_index(request):
    """ method to get all blog posts in order
    of creation"""

    posts = Post.objects.all().order_by('-created_on')
    page_obj = Post.objects.create_paginator(posts, 2, request)

    context = {
        'posts': posts,
        'page_obj': page_obj
    }

    return render(request, 'blog/blog_index.html', context)

def blog_detail(request,post_id):
    """method to see detail of a blog post"""

    posts = get_object_or_404(Post, pk=post_id)

    context = {
        'posts':posts,
    }
    return render(request, 'blog/blog_detail.html', context)


def blog_category(request, category):
    """method to retrieve blogs posts
    with a specific category field"""
    
    posts = Post.objects.filter(
        categories__name__contains=category).order_by('-created_on')
    
    context = {
        'category' : category,
        'posts' : posts
    }

    return render(request, 'blog/blog_category.html', context)

# def blog_category(request):
#     """method to retrieve blogs posts
#     with a specific category field"""

#     if request.method == "GET":
#         form = SearchedPostForm(request.GET)

#         if form.is_valid():
#             category = form.cleaned_data.get("query_search")
#             posts = Post.objects.filter(
#                 categories__name__contains=category).order_by('-created_on')
            
#             context = {
#                 'category' : category,
#                 'posts' : posts
#             }

#     return render(request, 'blog/blog_category.html', context)

# def search(request):
#     """ method that searches in db blog posts
#     under a certain category"""

#     if request.method == "GET":
#         form = SearchedPostForm(request.GET)

#         if form.is_valid():
#             post = form.cleaned_data.get("query_search")
#             posts = Post.objects.filter(
#                 categories__name__icontains=post
#             )

#             context = {
#                 'posts': posts,
#             }

#         return render(request, 'blog/blog_category.html', context)