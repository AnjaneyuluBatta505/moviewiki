from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from django.contrib import admin
from wiki.models import Movie, Person, Song, Award, ImageURL
# unregister
admin.site.unregister(User)
admin.site.unregister(Group)

# class CommentInline(admin.TabularInline):
#     model = Comment

admin.site.site_header = "Cinima-Wiki Administration"
admin.site.site_title = "Cinima-Wiki"
admin.site.index_title = "Update Cinima-Wiki Data"


class ImagesInline(admin.TabularInline):
    model = ImageURL
    fields = ("url", "alternate_text",)
    extra = 1


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name', 'biography']
    list_filter = ('updated_on',)
    ordering = ('name',)
    exclude = ("updated_on",)
    inlines = [ImagesInline]

    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            '//cdn.ckeditor.com/4.5.11/standard/ckeditor.js',
            'js/custom.js',
        )


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title', 'genre']
    list_filter = ('genre', 'title', 'updated_on', 'released_on')
    ordering = ('released_on',)
    exclude = ("updated_on",)
    inlines = [ImagesInline]

    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            '//cdn.ckeditor.com/4.5.11/standard/ckeditor.js',
        )


class SongAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title', 'music_directors', 'singers', 'writers', 'lyrics', 'movie']
    list_filter = ('title', 'writers', 'singers')
    ordering = ('updated_on',)
    exclude = ("updated_on",)

    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            '//cdn.ckeditor.com/4.5.11/standard/ckeditor.js',
            '//cdnjs.cloudflare.com/ajax/libs/select2/4.0.3/js/select2.min.js',
            'js/custom.js',
        )
        css = {
            'all': (
                '//cdnjs.cloudflare.com/ajax/libs/select2/4.0.3/css/select2.min.css',
            )
        }


class AwardAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title', 'movie', 'awardee']
    list_filter = ('title', 'awardee', 'movie', 'awarded_on')
    ordering = ('title',)
    exclude = ("updated_on",)

    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            '//cdn.ckeditor.com/4.5.11/standard/ckeditor.js',
            '//cdnjs.cloudflare.com/ajax/libs/select2/4.0.3/js/select2.min.js',
            'js/custom.js',
        )
        css = {
            'all': (
                '//cdnjs.cloudflare.com/ajax/libs/select2/4.0.3/css/select2.min.css',
            )
        }


class ImageURLAdmin(admin.ModelAdmin):
    list_display = ('movie',)
    search_fields = ['movie', 'person', 'url']
    list_filter = ('movie', 'person')
    ordering = ('movie', 'person')
    exclude = ("updated_on",)

    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            '//cdn.ckeditor.com/4.5.11/standard/ckeditor.js',
            '//cdnjs.cloudflare.com/ajax/libs/select2/4.0.3/js/select2.min.js',
            'js/custom.js',
        )
        css = {
            'all': (
                '//cdnjs.cloudflare.com/ajax/libs/select2/4.0.3/css/select2.min.css',
            )
        }


admin.site.register(Person, PersonAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Award, AwardAdmin)
admin.site.register(ImageURL, ImageURLAdmin)
