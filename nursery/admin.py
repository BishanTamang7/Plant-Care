from django.contrib import admin
from .models import Plant
from visitor.models import Wishlist


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "owner", "care_level", "created_at")
    list_filter = ("category", "care_level", "owner")
    search_fields = ("name", "care_instructions")
    ordering = ("-created_at",)
    date_hierarchy = "created_at"
    autocomplete_fields = ("owner",)
    class WishlistInline(admin.TabularInline):
        model = Wishlist
        extra = 0
        autocomplete_fields = ("user",)

    inlines = [WishlistInline]