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
