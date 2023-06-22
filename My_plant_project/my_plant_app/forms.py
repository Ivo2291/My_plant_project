from django import forms

from My_plant_project.my_plant_app.models import Profile, Plant


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['profile_picture']


class PlantCreateForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'
