from django.contrib import admin
from .models import Wishlist


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ("user", "plant", "added_at")
    list_filter = ("added_at",)
    search_fields = ("user__email", "user__username", "plant__name")
    autocomplete_fields = ("user", "plant")
    date_hierarchy = "added_at"