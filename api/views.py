from django.contrib.auth.models import User
from api.models import *
from api.serializers import *
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
import json

class UserExtViewSet(viewsets.ModelViewSet):
    queryset = UserExt.objects.all()
    serializer_class = UserExtSerializer


class LoginViewSet(APIView):

    def post(self, request, format=None):
        if request.method != 'POST':
            return Response(status.HTTP_403_FORBIDDEN)
        jsonData = request.body
        data = json.loads(jsonData)
        if data['spotifyID'] in UserExt.objects.values_list('spotifyID'):
            return Response(status.HTTP_304_NOT_MODIFIED)
        user = UserExt.objects.create(username=data['username'], firstname=data['firstName'], lastName=data['lastName'], spotifyID=data['spotifyID'])
        ser = UserExtSerializer(user)
        return Response(ser.data, status=status.HTTP_201_CREATED)


class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer

    def post(self, request, format=None):
        if request.method != 'POST':
            return Response(status.HTTP_403_FORBIDDEN)
        jsonData = request.body
        data = json.loads(jsonData)
        creator = UserExt.objects.get(spotifyID=data['userSpotifyID'])
        queue = Song.objects.bulk_create(spotifyID=data['songSpotifyID'])
        party = Party.objects.create(name=data['name'], passKey=data['passKey'], creator=creator, queue=queue, location=data['location'])
        ser = PartySerializer(party)
        return Response(ser.data, status=status.HTTP_201_CREATED)


class SongViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = SongSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = ArtistSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = AlbumSerializer


class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PlaylistSerializer
