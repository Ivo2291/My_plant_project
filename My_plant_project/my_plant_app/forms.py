from django import forms

from My_plant_project.my_plant_app.models import Profile, Plant


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['profile_picture']


class ProfileEditForm(ProfileBaseForm):
    pass


class PlantBaseForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class PlantCreateForm(PlantBaseForm):
    pass


class PlantEditForm(PlantBaseForm):
    pass


class PlantDeleteForm(PlantBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_fields_to_disable()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        else:
            return self.instance

    def __set_fields_to_disable(self):
        for field in self.fields.values():
            field.disabled = True
