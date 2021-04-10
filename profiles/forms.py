from django import forms
from .import models


class Showprofile(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['name', 'user', 'bio', 'image']
