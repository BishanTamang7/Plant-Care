from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from account.decorators import nursery_required
from django.core.exceptions import PermissionDenied
from .models import Plant
from .forms import PlantForm, NurseryProfileForm


@login_required
def plant_list(request):
    plants = Plant.objects.filter(owner=request.user)
    return render(request, "nursery/plant_list.html", {"plants": plants})


@login_required
@nursery_required
def add_plant(request):
    if request.method == "POST":
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            plant = form.save(commit=False)
            plant.owner = request.user
            plant.save()
            return redirect("nursery:plant_list")
    else:
        form = PlantForm()
    return render(request, "nursery/add_plant.html", {"form": form})


@login_required
def edit_plant(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    if plant.owner != request.user:
        raise PermissionDenied("You are not allowed to edit this plant.")
    if request.method == "POST":
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            return redirect("nursery:plant_detail", pk=pk)
    else:
        form = PlantForm(instance=plant)
    return render(request, "nursery/edit_plant.html", {"form": form, "plant": plant})


def plant_detail(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    return render(request, "nursery/plant_detail.html", {"plant": plant})


@login_required
def delete_plant(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    if plant.owner != request.user:
        raise PermissionDenied("You are not allowed to delete this plant.")

    if request.method == "POST":
        plant.delete()
    return redirect("nursery:plant_list")

@login_required
def nursery_profile(request):
    return render(request, "nursery/nursery_profile.html", {"nursery": request.user})


@login_required
@nursery_required
def edit_nursery_profile(request):
    if request.method == "POST":
        form = NurseryProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("nursery:nursery_profile")
    else:
        form = NurseryProfileForm(instance=request.user)
    return render(request, "nursery/edit_nursery_profile.html", {"form": form})
