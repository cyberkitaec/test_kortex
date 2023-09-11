from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


# Create your views here.

class SingerView(APIView):

    def get(self, request):
        queryset = Singer.objects.all()
        return Response({"data":SingerSerializer(queryset, many=True).data})

    def post(self, request, *args, **kwargs):
        """
        Создание нового исполнителя
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        serializer_singer = SingerSerializer(data=request.data)
        serializer_singer.is_valid(raise_exception=True)
        serializer_singer.save()
        return Response({"code":status.HTTP_200_OK}, status=status.HTTP_200_OK)

