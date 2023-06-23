from django.shortcuts import render, redirect

from My_plant_project.my_plant_app.forms import ProfileCreateForm, PlantCreateForm, PlantEditForm, PlantDeleteForm, \
    ProfileEditForm
from My_plant_project.my_plant_app.models import Profile, Plant


def get_profile():
    try:
        return Profile.objects.get()

    except Profile.DoesNotExist:
        return None


def index(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'home-page.html', context)


def profile_create_page(request):
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'create-profile.html', context)


def profile_details_page(request):
    profile = get_profile()
    plants_count = Plant.objects.all().count()

    context = {
        'profile': profile,
        'plants_count': plants_count,
    }

    return render(request, 'profile-details.html', context)


def profile_edit_page(request):
    profile = get_profile()

    form = ProfileEditForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile details')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'edit-profile.html', context)


def profile_delete_page(request):
    profile = get_profile()
    plants = Plant.objects.all()

    if request.method == 'POST':
        profile.delete()
        plants.delete()

        return redirect('index')

    return render(request, 'delete-profile.html', {'profile': profile,})


def catalogue_page(request):
    plants = Plant.objects.all()
    profile = get_profile()

    context = {
        'plants': plants,
        'profile': profile,
    }

    return render(request, 'catalogue.html', context)


def plant_details_page(request, pk):
    plant = Plant.objects.filter(pk=pk).get()

    context = {
        'plant': plant
    }
    return render(request, 'plant-details.html', context)


def plant_create_page(request):
    profile = get_profile()
    form = PlantCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'create-plant.html', context)


def plant_edit_page(request, pk):
    plant = Plant.objects.filter(pk=pk).get()

    form = PlantEditForm(request.POST or None, instance=plant)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant,
    }

    return render(request, 'edit-plant.html', context)


def plant_delete_page(request, pk):
    plant = Plant.objects.filter(pk=pk).get()

    if request.method == 'POST':
        form = PlantDeleteForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    form = PlantDeleteForm(instance=plant)

    context = {
        'form': form,
        'plant': plant,
    }

    return render(request, 'delete-plant.html', context)
