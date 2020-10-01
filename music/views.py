from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class PaisViewSet(viewsets.ModelViewSet):
	queryset = Pais.objects.all()
	serializer_class = PaisSerializer

class ArtistaViewSet(viewsets.ModelViewSet):
	queryset = Artista.objects.all()
	serializer_class = ArtistaSerializer

class AlbumViewSet(viewsets.ModelViewSet):
	queryset = Album.objects.all()
	serializer_class = AlbumSerializer

class CancionViewSet(viewsets.ModelViewSet):
	queryset = Cancion.objects.all()
	serializer_class = CancionSerializer

class login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

    # def post(self, request, *args, **kwargs):
    #     if 'token' in request.data:
    #         user, token = self.getInitialData(request, True)
    #     else:
    #         user, token = self.getInitialData(request)
        
    #     response = {
    #         'id': user.id,
    #         'username': user.username,
    #         'email': user.email,
	# 		'token': token.key
    #     }

    # def getInitialData(self, request, token_request=False):
    #     if token_request:
    #         token_key = request.data['token']
    #         token = Token.objects.get(key=token_key)
    #         user = token.user
    #     else:            
    #         serializer = self.serializer_class(data=request.data,context={'request': request})
    #         serializer.is_valid(raise_exception=True)
    #         user = serializer.validated_data['user']
    #         token, created = Token.objects.get_or_create(user=user)
    #     return user, token
