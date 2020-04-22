from django.shortcuts import render, redirect, reverse, get_object_or_404
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


# Project Details
def project_details(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, "project_details.html", {"project": project})


# Add Projects
@login_required
def add_project(request):
    if request.method == "POST":
        add_project_form = AddProjectForm(request.POST, request.FILES)

        if add_project_form.is_valid():
            project = add_project_form.save(commit=False)
            project.added_by = request.user
            project.save()
            messages.success(request, "You have successfully added a project.")
            return redirect(reverse('profile'))
        else:
            add_project_form = AddProjectForm()
            messages.error(request, "Your project couldn't be added.")
    else:
        add_project_form = AddProjectForm()

    return render(request, 'add_project.html',
                  {'add_project_form': add_project_form})


# Edit Project
@login_required
def edit_project(request,pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        edit_project_form = AddProjectForm(request.POST, request.FILES)
        
        if edit_project_form.is_valid():
            project.name = edit_project_form.cleaned_data.get('name')
            project.category = edit_project_form.cleaned_data.get('category')
            project.description = edit_project_form.cleaned_data.get('description')
            
            if edit_project_form.cleaned_data.get('image'):
                project.image = edit_project_form.cleaned_data.get('image')
                
            project.save()
            messages.success(request, "You have successfully updated your project.")
            return redirect(project_details, project.pk)

    else:
        edit_project_form = AddProjectForm(initial={'name': project.name, 'category':project.category, 'description': project.description, 'image': project.image})
        messages.error(request, "Your project couldn't be updated.")

    return render(request, "edit_project.html", {"project": project, "edit_project_form": edit_project_form})


# Delete Project
@login_required
def delete_project(request,pk):
    project = get_object_or_404(Project, pk=pk)
    cart = request.session.get('cart', {})

    if pk in cart:
        messages.error(request, "Please remove this project from your cart first before you delete it.")
        return redirect('projects')
    
    else:
        project.delete()
        messages.success(request, "You have successfully deleted your project.")
        return redirect('projects')
