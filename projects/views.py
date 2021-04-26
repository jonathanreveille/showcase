from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Tag
#from .forms import SearchedProductForms

# Create your views here.

def land_page(request):
    return render(request, 'projects/landing.html')

def home(request):
    projects_found = Project.objects.all()
    context = {
        'projects_found':projects_found,
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