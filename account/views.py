from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, EmailAuthenticationForm
from .decorators import visitor_required, nursery_required, redirect_dashboard


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegistrationForm()
    return render(request, "accounts/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = EmailAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect_dashboard(user)
    else:
        form = EmailAuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("home")


@login_required
@visitor_required
def visitor_dashboard(request):
    return render(request, "accounts/visitor_dashboard.html")


@login_required
@nursery_required
def nursery_dashboard(request):
    recent_plants = request.user.plants.order_by('-created_at')[:2]

    context = {
        'recent_plants': recent_plants
    }
    return render(request, "accounts/nursery_dashboard.html", context)