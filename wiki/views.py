from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from wiki.models import Person
# Create your views here.


class HomeView(ListView):
    template_name = "home.html"
    queryset = []


class MovieView(TemplateView):
    template_name = "movie.html"


class PersonView(DetailView):
    template_name = "person.html"
    model = Person
    slug_field = "slug"


class SongView(TemplateView):
    template_name = "song.html"
