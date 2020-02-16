from django import forms
from .models import SiteUser


class ImageUpload(forms.ModelForm):
    class Meta:
        model = SiteUser
        fields = ['image']


class CheckTags(forms.ModelForm):
    pass