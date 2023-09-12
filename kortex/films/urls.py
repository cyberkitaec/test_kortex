from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('singer', SingerView.as_view()),
    path('singer/<int:pk>', SingerView.as_view()),
    path('album', AlbumView.as_view()),
    path('album/<int:pk>', AlbumView.as_view()),
    path('song', SongView.as_view()),
    path('song/<int:pk>', SongView.as_view()),

]
