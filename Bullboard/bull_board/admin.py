from django.contrib import admin
from .models import *

from ckeditor.widgets import CKEditorWidget


class PostAdminForm(forms.ModelForm):
    description = forms.CharField(Label="Описание", widget=CKEditorWidget())
    class Meta:
        model = Movie
        fields = '__all__'


