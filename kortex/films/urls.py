from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('singer', SingerView.as_view()),
    path('singer/<int:pk>', SingerView.as_view()),
    path('album', SingerView.as_view()),
    path('album/<int:pk>', SingerView.as_view()),

]
