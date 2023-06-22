from django.contrib import admin

from My_plant_project.my_plant_app.models import Profile, Plant


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name']


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ['type', 'name']
