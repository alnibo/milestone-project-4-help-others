from django.shortcuts import render
from .models import Project


# All Projects
def all_projects(request):
    projects = Project.objects.all()
    return render(request, "projects.html", {"projects": projects})


# Categories
def view_category(request, category):
    projects = Project.objects.filter(category=category)
    return render(request, "projects.html", {"projects": projects})
