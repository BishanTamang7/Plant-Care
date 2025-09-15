from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from nursery.models import Plant
from .models import Wishlist
from .forms import VisitorProfileForm

 
@login_required
def browse_plants(request):
    plants = (
        Plant.objects.select_related("owner")
        .filter(owner__isnull=False)
        .order_by("-created_at")
    )

    query = request.GET.get("q")
    if query:
        plants = plants.filter(name__icontains=query)

    category = request.GET.get("category")
    if category:
        plants = plants.filter(category=category)

    care_level = request.GET.get("care_level")
    if care_level:
        plants = plants.filter(care_level=care_level)

    paginator = Paginator(plants, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "visitor/browse_plants.html",
        {
            "page_obj": page_obj,
            "category_choices": Plant._meta.get_field("category").choices,
            "care_choices": Plant._meta.get_field("care_level").choices,
        },
    )


@login_required
def plant_detail_visitor(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    return render(request, "visitor/plant_detail.html", {"plant": plant})


@login_required
def add_to_wishlist(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    Wishlist.objects.get_or_create(user=request.user, plant=plant)
    return redirect('visitor:my_wishlists')


@login_required
def my_wishlists(request):
    wishlists = Wishlist.objects.filter(user=request.user).select_related("plant")
    return render(request, "visitor/my_wishlists.html", {"wishlists": wishlists})


@login_required
def remove_from_wishlist(request, plant_id):
    wishlist_item = get_object_or_404(Wishlist, user=request.user, plant_id=plant_id)
    wishlist_item.delete()
    return redirect("visitor:my_wishlists")


@login_required
def visitor_profile(request):
    return render(request, "visitor/visitor_profile.html", {"visitor": request.user})


@login_required
def edit_visitor_profile(request):
    if request.method == "POST":
        form = VisitorProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("visitor_dashboard")
    else:
        form = VisitorProfileForm(instance=request.user)

    return render(request, "visitor/edit_visitor_profile.html", {"form": form})