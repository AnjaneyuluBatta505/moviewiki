from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from wiki.globals import MOVIE_GENRE, GENDER, AWARD_STATUS


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

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=80, unique=True)
    released_on = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    budget = models.CharField(max_length=100, null=True, blank=True)
    box_office = models.CharField(max_length=100, null=True, blank=True)
    rating = models.CharField(max_length=100, null=True, blank=True)
    rating = models.CharField(max_length=100, null=True, blank=True)
    genre = models.CharField(choices=MOVIE_GENRE, max_length=100, null=True, blank=True)
    updated_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('released_on',)


class Song(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=80, unique=True)
    music_director = models.ForeignKey(Person, blank=True, null=True, related_name="songs"),
    singers = models.ManyToManyField(Person, blank=True, related_name="all_songs")
    writers = models.ForeignKey(Person, blank=True, null=True, related_name="get_songs")
    lyrics = models.TextField(null=True, blank=True)
    movie = models.ForeignKey(Movie, null=True, blank=True)
    updated_on = models.DateTimeField(default=timezone.now)

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
