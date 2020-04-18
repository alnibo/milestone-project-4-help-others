from django.shortcuts import render
from projects.models import Project


# def do_search(request):
#     projects = Project.objects.filter(name__icontains=request.GET['q'])
#     return render(request, "projects.html", {"projects": projects})


def do_search(request):
    qs = Project.objects.all()
    text = request.GET['q']
    for term in text.split():
        projects = qs.filter(Project(name__icontains=term) | Project(description__icontains=term))
    return render(request, "projects.html", {"projects": projects})
