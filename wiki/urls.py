from django.conf.urls import url
from wiki.views import HomeView, MovieView, PersonView, SongView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^movie/$', MovieView.as_view(), name="movie"),
    url(r'^(?P<slug>\w+)-movies-awards-biography/$', PersonView.as_view(), name="person"),
    url(r'^song/$', SongView.as_view(), name="person"),
]