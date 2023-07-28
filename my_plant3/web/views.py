from django.shortcuts import render, redirect

from my_plant3.web.forms import ProfileCreateForm, PlantCreateForm, PlantEditForm, PlantDeleteForm, ProfileEditForm
from my_plant3.web.models import Profile, Plant


def get_profile():
    return Profile.objects.first()


def index(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'common/home-page.html', context)


def show_catalogue(request):
    profile = get_profile()
    plants = Plant.objects.all()
    context = {
        'profile': profile,
        'plants': plants,
    }
    return render(request, 'common/catalogue.html', context)


def profile_create(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show catalogue')
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile/create-profile.html', context)


def profile_edit(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile/edit-profile.html', context)


def profile_delete(request):
    profile = get_profile()
    if request.method == 'POST':
        profile.delete()
        Plant.objects.all().delete()
        return redirect('home page')
    context = {
        'profile': profile,
    }

    return render(request, 'profile/delete-profile.html', context)


def profile_details(request):
    profile = get_profile()
    plants = Plant.objects.all()
    context = {
        'profile': profile,
        'plants': plants[:3],
    }
    return render(request, 'profile/profile-details.html', context)


def plant_create(request):
    profile = get_profile()
    if request.method == 'GET':
        form = PlantCreateForm()
    else:
        form = PlantCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show catalogue')
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'plant/create-plant.html', context)


def plant_edit(request, pk):
    profile = get_profile()
    plant = Plant.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = PlantEditForm(instance=plant)
    else:
        form = PlantEditForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('show catalogue')

    context = {
        'profile': profile,
        'form': form,
        'plant': plant,
    }

    return render(request, 'plant/edit-plant.html', context)


def plant_delete(request, pk):
    profile = get_profile()
    plant = Plant.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = PlantDeleteForm(instance=plant)
    else:
        form = PlantDeleteForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('show catalogue')

    context = {
        'profile': profile,
        'form': form,
        'plant': plant,
    }
    return render(request, 'plant/delete-plant.html', context)


def plant_details(request, pk):
    profile = get_profile()
    plant = Plant.objects.filter(pk=pk).get()
    context = {
        'profile': profile,
        'plant': plant,
    }
    return render(request, 'plant/plant-details.html', context)
