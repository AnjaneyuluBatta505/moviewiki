from django.conf.urls import url
from wiki import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name="home"),
    url(r'^search/$', views.SearchView.as_view(), name="search"),
    url(r'^(?P<slug>.+)-movie-details-star-casting-team/$', views.MovieView.as_view(), name="movie"),
    url(r'^(?P<slug>.+)-movies-awards-biography/$', views.PersonView.as_view(), name="person"),
    url(r'^(?P<slug>.+)-song-details-lyrics-(?P<movie_slug>.+)/$', views.SongView.as_view(), name="song"),
    url(r'^privacy-policy/$', views.PrivacyPolicyView.as_view(), name="privacy_policy"),
    url(r'^terms-conditions/$', views.TermsConditionsView.as_view(), name="terms_conditions"),
    url(r'^contact-us/$', views.ContactUsView.as_view(), name="contact_us"),
    url(r'^about-us/$', views.AboutUsView.as_view(), name="about_us"),
    url(r'^sitemap\.xml$', views.SitemapView.as_view(), name="sitemap"),
    url(r'^robots\.txt$', views.RobotsView.as_view(), name="robots"),
    url(r'^BingSiteAuth\.xml$', views.BingSiteVerificationView.as_view(), name="bing_site_verify"),
    url(r'^googlea95613a6b3c4ff8a\.html$', views.GoogleSiteVerificationView.as_view(), name="google_site_verify"),

]
