from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView

# Create your views here.


class HomeView(ListView):
    template_name = "home.html"
    queryset = []


class MovieView(TemplateView):
    template_name = "movie.html"


class PersonView(TemplateView):
    template_name = "person.html"


class SongView(TemplateView):
    template_name = "song.html"
