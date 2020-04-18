from django.shortcuts import render
from projects.models import Project


def do_search(request):
    projects = Project.objects.filter(name__icontains=request.GET['q'])
    return render(request, "projects.html", {"projects": projects})
