from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from wiki.globals import MOVIE_GENRE, GENDER, AWARD_STATUS
from wiki.utils import random_select


class Person(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=80, unique=True)
    gender = models.CharField(choices=GENDER, max_length=100, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    languages_known = models.CharField(max_length=100, null=True, blank=True)
    height = models.CharField(max_length=100, null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    image = models.URLField()
    nick_names = models.CharField(max_length=100, null=True, blank=True)
    role = models.CharField(max_length=100, null=True, blank=True)
    updated_on = models.DateTimeField(default=timezone.now)
    # seo
    description = models.TextField(null=True, blank=True)

    def images(self):
        return ImageURL.objects.filter(person_id=self.id)

    def related_persons(self):
        persons = self.__class__.objects.exclude(id=self.id)
        return random_select(persons)

    def get_absolute_url(self):
        return reverse("wiki:person", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=80, unique=True)
    released_on = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    language = models.CharField(max_length=100, null=True, blank=True)
    budget = models.CharField(max_length=100, null=True, blank=True)
    box_office = models.CharField(max_length=100, null=True, blank=True)
    rating = models.CharField(max_length=100, null=True, blank=True)
    genre = models.CharField(choices=MOVIE_GENRE, max_length=100, null=True, blank=True)
    updated_on = models.DateTimeField(default=timezone.now)
    about = models.TextField(blank=True, null=True)
    producer = models.CharField(max_length=50, blank=True, null=True)
    director = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    image = models.URLField()
    team = models.ManyToManyField(Person, related_name="movies")

    def images(self):
        return ImageURL.objects.filter(movie_id=self.id)

    def related_movies(self):
        related_movies = self.__class__.objects.exclude(id=self.id)
        return random_select(related_movies)

    def get_absolute_url(self):
        return reverse("wiki:movie", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('released_on',)


class Song(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=80, unique=True)
    music_directors = models.ManyToManyField(Person, blank=True, null=True, related_name="songs"),
    singers = models.ManyToManyField(Person, blank=True, related_name="all_songs")
    writers = models.ManyToManyField(Person, blank=True, null=True, related_name="get_songs")
    lyrics = models.TextField(null=True, blank=True)
    movie = models.ForeignKey(Movie, null=True, blank=True, related_name="related_songs")
    updated_on = models.DateTimeField(default=timezone.now)
    image = models.URLField()
    # seo
    description = models.CharField(max_length=100, null=True, blank=True)

    def get_related_songs(self):
        try:
            return self.movie.related_songs.exclude(id=self.id)
        except Exception:
            return []

    def get_absolute_url(self):
        return reverse("wiki:song", kwargs={"slug": self.slug, "movie_slug": self.movie.slug})

    def __str__(self):
        return self.title


class Award(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=80, unique=True)
    awarded_on = models.DateTimeField()
    category = models.CharField(max_length=150)
    movie = models.ForeignKey(Movie)
    status = models.CharField(choices=AWARD_STATUS, max_length=50)
    awardee = models.ForeignKey(Person, null=True, blank=True, related_name="awards")
    updated_on = models.DateTimeField(default=timezone.now)
    image = models.URLField()

    def __str__(self):
        return self.title


class ImageURL(models.Model):
    url = models.URLField()
    movie = models.ForeignKey(Movie, null=True, blank=True)
    person = models.ForeignKey(Person, null=True, blank=True)
    alternate_text = models.CharField(max_length=80)
    updated_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.url

    class Meta:
        ordering = ["id"]
