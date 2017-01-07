from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView

from django.db.models import Q

from wiki.models import Person, Movie, Song


class HomeView(ListView):
    template_name = "home.html"
    model = Movie
    paginate_by = 10

    def get_template_names(self):
        if self.request.is_ajax():
            self.template_name = "partials/load_movies.html"
        return super(HomeView, self).get_template_names()


class SearchView(TemplateView):
    template_name = "search.html"
    model = Movie

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        persons = Person.objects.all()
        movies = Movie.objects.all()
        songs = Song.objects.all()
        query = self.request.GET.get("query")
        if query:
            query_list = query.split()
            persons_query = None
            for word in query_list:
               q_aux = Q(name__icontains=word)|Q(nick_names__icontains=word)
               persons_query = ( q_aux & persons_query ) if bool( persons_query ) else q_aux
            movies_query = None
            for word in query_list:
               q_aux = Q(title__icontains=word)|Q(language__icontains=word)|Q(producer__icontains=word)|Q(director__icontains=word)
               movies_query = ( q_aux & movies_query ) if bool( movies_query ) else q_aux
            songs_query = None
            for word in query_list:
               q_aux = Q(title__icontains=word)|Q(lyrics__icontains=word)|Q(description__icontains=word)
               songs_query = ( q_aux & songs_query ) if bool( songs_query ) else q_aux
            persons = persons.filter(persons_query)
            movies = movies.filter(movies_query)
            songs = songs.filter(songs_query)
        context.update({
            "persons": persons[:150],
            "movies": movies[:150],
            "songs": songs[:150]
        })
        return context



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


class PrivacyPolicyView(TemplateView):
    template_name = "privacy-policy.html"


class TermsConditionsView(TemplateView):
    template_name = "terms-conditions.html"


class ContactUsView(TemplateView):
    template_name = "contact-us.html"


class AboutUsView(TemplateView):
    template_name = "about-us.html"


class SitemapView(TemplateView):
    template_name = "sitemap.xml"
    content_type = "application/xml"

    def get_context_data(self):
        context = super(SitemapView, self).get_context_data()
        context.update({
            "movies": Movie.objects.all(),
            "songs": Song.objects.all(),
            "persons": Person.objects.all()
        })
        return context



class RobotsView(TemplateView):
    template_name = "robots.txt"
    content_type = "text"


class GoogleSiteVerificationView(TemplateView):    
    template_name = "googlea95613a6b3c4ff8a.html"
    content_type = "text/plain"


class BingSiteVerificationView(TemplateView):    
    template_name = "BingSiteAuth.xml"
    content_type = "application/xml"

