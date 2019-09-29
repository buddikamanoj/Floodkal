
from django.views.generic import DetailView, ListView, UpdateView, CreateView , TemplateView
from .models import Map
from .forms import MapForm

import django.views.generic
#from django.views.generic import direct_to_template
from django.http import Http404


class MapListView(ListView):
    model = Map


class MapCreateView(CreateView):
    model = Map
    form_class = MapForm


class MapDetailView(DetailView):
    model = Map


class MapUpdateView(UpdateView):
    model = Map
    form_class = MapForm
