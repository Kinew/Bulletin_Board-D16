from django.http import  HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView
)

from .forms import AdvertForms
from .models import *


class AdvertListView(LoginRequiredMixin, ListView):
    model = Advert
    template_name = 'name/advert_list.html'
    context_object_name = 'advert_list'

class AdvertCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = AdvertForm
    model = Advert
    template_name = 'advert_create.html'
    context_object_name = 'create'


class AdvertUpdate(LoginRequiredMixin, UpdateView):
    form_class = AdvertForm
    model = Advert
    template_name = 'advert_edit.html'


class AdvertDelete(LoginRequiredMixin, DeleteView):
    model = Advert
    template_name = 'advert_delete.html'
    success_url = reverse_lazy('advert_list')