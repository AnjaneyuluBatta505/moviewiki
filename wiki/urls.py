from django.conf.urls import url
from wiki.views import HomeView, MovieView, PersonView, SongView, SearchView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^search/$', SearchView.as_view(), name="search"),
    url(r'^(?P<slug>\w+)-movie-details-star-casting-team/$', MovieView.as_view(), name="movie"),
    url(r'^(?P<slug>\w+)-movies-awards-biography/$', PersonView.as_view(), name="person"),
    url(r'^(?P<slug>\w+)-song-details-lyrics-(?P<movie_slug>\w+)/$', SongView.as_view(), name="song"),
]
