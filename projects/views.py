from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project
from .forms import AddProjectForm


# All Projects
def all_projects(request):
    projects = Project.objects.all()
    return render(request, "projects.html", {"projects": projects})


# Categories
def view_category(request, category):
    projects = Project.objects.filter(category=category)
    return render(request, "projects.html", {"projects": projects})


# Add Projects
@login_required
def add_project(request):
    if request.method == "POST":
        add_project_form = AddProjectForm(request.POST, request.FILES)

        if add_project_form.is_valid():
            add_project_form.save()
            messages.success(request, "You have successfully added a project.")
            return redirect(reverse('profile'))
        else:
            add_project_form = AddProjectForm()
            messages.error(request, "Your project couldn't be added.")
    else:
        add_project_form = AddProjectForm()

    return render(request, 'add_project.html',
                  {'add_project_form': add_project_form})
