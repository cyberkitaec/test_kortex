from rest_framework import serializers
from .models import *


class SingerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Singer
        fields = '__all__'

    def create(self, validated_data):
        return Singer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nickname_singer = validated_data.get('nickname_singer')
