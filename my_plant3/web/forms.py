from django import forms

from my_plant3.web.models import Profile, Plant


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('profile_picture',)
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture',
        }


class PlantBaseForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'
        labels = {
            'plant_type': 'Type',
            'image_url': 'Image URL',
        }


class PlantCreateForm(PlantBaseForm):
    pass


class PlantEditForm(PlantBaseForm):
    pass


class PlantDeleteForm(PlantBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance




