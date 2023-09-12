from rest_framework import serializers
from .models import *


class SingerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Singer
        fields = '__all__'

    def create(self, validated_data):
        return Singer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.singer_nickname = validated_data.get('singer_nickname')
        instance.save()
        return instance


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = '__all__'

    def create(self, validated_data):
        return Album.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.singer_nickname = validated_data.get('singer_nickname')
        instance.name_album = validated_data.get('name_album')
        instance.year_of_release = validated_data.get('year_of_release')
        instance.save()
        return instance


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = '__all__'

    def create(self, validated_data):
        return Song.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name_song = validated_data.get('name_song')
        instance.number_in_album = validated_data.get('number_in_album')
        instance.album = validated_data.get('album')
        instance.save()
        return instance
