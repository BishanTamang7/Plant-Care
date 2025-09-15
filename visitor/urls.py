from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name = "visitor"

urlpatterns = [
    path("browse_plants", views.browse_plants, name="browse_plants"),
    path("plant/<int:pk>/", views.plant_detail_visitor, name="plant_detail"),
    path("my_wishlists", views.my_wishlists, name="my_wishlists"),
    path("wishlist/add/<int:plant_id>/", views.add_to_wishlist, name="add_to_wishlist"),
    path("wishlist/remove/<int:plant_id>/", views.remove_from_wishlist, name="remove_from_wishlist"),
    path("visitor/profile/", views.visitor_profile, name="visitor_profile"),
    path("profile/visitor/edit/", views.edit_visitor_profile, name="edit_visitor_profile"),
    path(
        "password/change/",
        auth_views.PasswordChangeView.as_view(
            template_name="visitor/change_password.html",
            success_url=reverse_lazy("visiotr:visitor_profile"),
        ),
        name="change_password",
    ),
]