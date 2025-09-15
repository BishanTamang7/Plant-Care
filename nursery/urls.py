from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name = "nursery"

urlpatterns = [
    path("my_plant", views.plant_list, name="plant_list"),
    path("add_plant/", views.add_plant, name="add_plant"),
    path("plant/<int:pk>/", views.plant_detail, name="plant_detail"),
    path("plant/<int:pk>/edit/", views.edit_plant, name="edit_plant"),
    path("plant/<int:pk>/delete/", views.delete_plant, name="delete_plant"),
    path("nursery/profile/", views.nursery_profile, name="nursery_profile"),
    path("nursery/profile/edit/", views.edit_nursery_profile, name="edit_nursery_profile"),
    path(
        "password/change/",
        auth_views.PasswordChangeView.as_view(
            template_name="nursery/change_password.html",
            success_url=reverse_lazy("nursery:nursery_profile"),
        ),
        name="change_password",
    ),
]