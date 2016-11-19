from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from wiki.models import Person, Movie, Song
# Create your views here.


class HomeView(ListView):
    template_name = "home.html"
    model = Movie
    paginate_by = 1

    def get_template_names(self):
        if self.request.is_ajax():
            self.template_name = "partials/load_movies.html"
        return super(HomeView, self).get_template_names()


class SearchView(ListView):
    template_name = "search.html"
    model = Movie


class MovieView(DetailView):
    template_name = "movie.html"
    model = Movie
    slug_field = "slug"


class PersonView(DetailView):
    template_name = "person.html"
    model = Person
    slug_field = "slug"


class SongView(DetailView):
    template_name = "song.html"
    model = Song
    slug_field = "slug"
