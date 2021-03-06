from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from projects.models import Project
from accounts.forms import UserLoginForm, UserRegistrationForm
from checkout.models import OrderLineItem
from django.db.models import Sum


def register(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])

            # if the user is authenticated
            if user:
                auth.login(user=user, request=request)
                messages.success(request, f"You have successfully registered, {user.username}!")
                return redirect(reverse('index'))
            else:
                messages.error(request,
                               "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html',
                  {"registration_form": registration_form})


def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, f"You have successfully logged in, {user.username}!")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None,
                                     "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})


@login_required
def user_profile(request):
    """The user's profile page"""
    user = User.objects.get(email=request.user.email)
    user_projects = Project.objects.filter(added_by=request.user)
    return render(request, 'profile.html', {"profile": user, "user_projects": user_projects})


@login_required
def logout(request):
    """Log the user out"""
    username = request.user.username
    auth.logout(request)
    messages.success(request, f"You have successfully been logged out, {username}!")
    return redirect(reverse('index'))


def donation_history(request):
    """View that displays the donation history"""
    total_amount = OrderLineItem.objects.filter(order__user=request.user).aggregate(Sum('amount')).get('amount__sum')
    return render(request, "donation_history.html", {"total_amount": total_amount})
