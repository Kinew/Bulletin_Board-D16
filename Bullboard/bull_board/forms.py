from django.db import models
from django import forms
from .models import Advert
class AdvertForms(forms.ModelForm):
    class Meta:
        model = Advert
        fields = '__all__'
