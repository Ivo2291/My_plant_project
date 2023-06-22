from django.shortcuts import render, redirect

from My_plant_project.my_plant_app.forms import ProfileCreateForm, PlantCreateForm
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
    if request.method == 'POST':
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    form = ProfileCreateForm()

    context = {
        'form': form,
    }

    return render(request, 'create-profile.html', context)


def profile_details_page(request):
    return render(request, 'profile-details.html')


def profile_edit_page(request):
    return render(request, 'edit-profile.html')


def profile_delete_page(request):
    return render(request, 'delete-profile.html')


def catalogue_page(request):
    plants = Plant.objects.all()

    context = {
        'plants': plants,
    }

    return render(request, 'catalogue.html', context)


def plant_details_page(request, pk):
    plant = Plant.objects.filter(pk=pk).get()

    context = {
        'plant': plant
    }
    return render(request, 'plant-details.html', context)


def plant_create_page(request):
    if request.method == 'POST':
        form = PlantCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    form = PlantCreateForm()

    context = {
        'form': form,
    }

    return render(request, 'create-plant.html', context)


def plant_edit_page(request, pk):
    return render(request, 'edit-plant.html')


def plant_delete_page(request, pk):
    return render(request, 'delete-plant.html')
