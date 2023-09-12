from django.shortcuts import render
from rest_framework.status import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


# Create your views here.

class SingerView(APIView):

    def get(self, request, *args, **kwargs):
        if kwargs:
            try:
                serializer = Singer.objects.get(pk=kwargs['pk'])
                return Response({'data': SingerSerializer(serializer).data})
            except:
                return Response({'code': HTTP_404_NOT_FOUND, 'error_message': 'object not found'},
                                status=HTTP_404_NOT_FOUND)
        queryset = Singer.objects.all()
        return Response({"data":SingerSerializer(queryset, many=True).data})

    def post(self, request, *args, **kwargs):
        serializer_singer = SingerSerializer(data=request.data)
        serializer_singer.is_valid(raise_exception=True)
        serializer_singer.save()
        return Response({"code": HTTP_200_OK}, status= HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        try:
            instance = Singer.objects.get(pk=kwargs['pk'])
            serializer = SingerSerializer(data=request.data, instance=instance)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'code': HTTP_200_OK}, status= HTTP_200_OK)
        except:
            return Response({'code': HTTP_404_NOT_FOUND, 'error_message': 'object not found'},
                            status=HTTP_404_NOT_FOUND)


class AlbumView(APIView):

    def get(self, request, *args, **kwargs):
        if kwargs:
            try:
                serializer = Album.objects.get(pk=kwargs['pk'])
                return Response({'data': AlbumSerializer(serializer).data})
            except:
                return Response({'code': HTTP_404_NOT_FOUND, 'error_message': 'object not found'},
                                status=HTTP_404_NOT_FOUND)
        queryset = Album.objects.all()
        return Response({"data": AlbumSerializer(queryset, many=True).data})

    def post(self, request, *args, **kwargs):
        serializer_singer = AlbumSerializer(data=request.data)
        serializer_singer.is_valid(raise_exception=True)
        serializer_singer.save()
        return Response({"code": HTTP_200_OK}, status=HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        try:
            instance = Album.objects.get(pk=kwargs['pk'])
            serializer = AlbumSerializer(data=request.data, instance=instance)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'code': HTTP_200_OK}, status=HTTP_200_OK)
        except:
            return Response({'code': HTTP_404_NOT_FOUND, 'error_message': 'object not found'},
                            status=HTTP_404_NOT_FOUND)

class SongView(APIView):

    def get(self, request, *args, **kwargs):
        if kwargs:
            try:
                serializer = Song.objects.get(pk=kwargs['pk'])
                return Response({'data': SongSerializer(serializer).data})
            except:
                return Response({'code': HTTP_404_NOT_FOUND, 'error_message': 'object not found'},
                                status=HTTP_404_NOT_FOUND)
        queryset = Song.objects.all()
        return Response({"data": SongSerializer(queryset, many=True).data})

    def post(self, request, *args, **kwargs):
        serializer_singer = SongSerializer(data=request.data)
        serializer_singer.is_valid(raise_exception=True)
        serializer_singer.save()
        return Response({"code": HTTP_200_OK}, status=HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        try:
            instance = Song.objects.get(pk=kwargs['pk'])
            serializer = SongSerializer(data=request.data, instance=instance)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'code': HTTP_200_OK}, status=HTTP_200_OK)
        except:
            return Response({'code': HTTP_404_NOT_FOUND, 'error_message': 'object not found'},
                            status=HTTP_404_NOT_FOUND)