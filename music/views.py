from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

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

class index(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny]
        return super(index, self).get_permissions()

    def get(self, request, *args, **kwargs):
        response = {'api':'/api'}
        return Response(data=response)