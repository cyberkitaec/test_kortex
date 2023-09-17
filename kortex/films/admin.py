from django.contrib import admin
from .models import *
# Register your models here.
# Регистрируем модели в админке Django

class SingerAdmin(admin.ModelAdmin):
    list_display = ['id', 'singer_nickname']
    list_display_links = ['id', 'singer_nickname']
    search_fields = ['id', 'singer_nickname']


class AlbumAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_album', 'year_of_release', 'singer_nickname']
    list_display_links = ['id', 'name_album', 'year_of_release', 'singer_nickname']
    search_fields = ['id', 'name_album', 'year_of_release', 'singer_nickname']


class SongAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_song', 'number_in_album', 'album']
    list_display_links = ['id', 'name_song', 'number_in_album', 'album']
    search_fields = ['id', 'name_song', 'number_in_album', 'album']


admin.site.register(Singer, SingerAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)
