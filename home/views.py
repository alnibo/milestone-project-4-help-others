from django.shortcuts import render


def index(request):
    """A view that renders the index page"""
    return render(request, "index.html")

def about_us(request):
    """View that displays the what we do page"""
    return render(request, "about.html")
