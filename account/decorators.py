from django.shortcuts import redirect
from functools import wraps

def visitor_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.role == "visitor":
            return view_func(request, *args, **kwargs)
        return redirect_dashboard(request.user)
    return wrapper


def nursery_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.role == "nursery":
            return view_func(request, *args, **kwargs)
        return redirect_dashboard(request.user)
    return wrapper


def redirect_dashboard(user):
    if user.role == "visitor":
        return redirect("visitor_dashboard")
    elif user.role == "nursery":
        return redirect("nursery_dashboard")
    else:
        return redirect("login")
