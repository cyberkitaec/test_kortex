from django.db import models
import datetime

# Генерируем года для заполнения поля year_of_release в Album
YEAR_CHOICES = [(r,r) for r in range(1950, datetime.date.today().year+1)]


class Singer(models.Model):
    """
    Исполнитель
    """
    singer_nickname = models.CharField(u'Псевдоним исполнителя', max_length=100)


class Album(models.Model):
    """
    Альбом
    """
    name_album = models.CharField(u'Наименование альбома', max_length=300)
    year_of_release = models.IntegerField(u'Год релиза',choices=YEAR_CHOICES)
    singer_nickname = models.ForeignKey(Singer, on_delete=models.CASCADE)


class Song(models.Model):
    """
    Песня
    """
    name_song = models.CharField(u'Наименование песни', max_length=200)
    number_in_album = models.IntegerField(u'Порядковый номер в альбоме')
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

