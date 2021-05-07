from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from .models import Project, Tag
from blog.models import Post
#from .forms import SearchedProductForms

# Create your views here.
def land_page(request):
    """landing page views"""
    posts = Post.objects.all().order_by('-created_on')[:2]
    context = {
        'posts':posts
    }
    return render(request, 'projects/landing.html', context)


def home(request):
    """showcase of projects, 
    pagination will show only 3 projects
    per pages"""

    projects_found = Project.objects.all()
    page_obj = Project.objects.create_paginator(projects_found, 3, request)

    context = {
        'projects_found':projects_found,
        'page_obj': page_obj,
    }

    return render(request, 'projects/home.html', context)

def detail(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    context = {
        'project': project,
    }
    return render(request, 'projects/detail.html', context)

def search(request):
    pass