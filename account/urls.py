from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("dashboard/visitor/", views.visitor_dashboard, name="visitor_dashboard"),
    path("dashboard/nursery/", views.nursery_dashboard, name="nursery_dashboard"),
]
