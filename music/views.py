from django.shortcuts import render
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import *
from .serializers import *

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import filters

class PaisViewSet(viewsets.ModelViewSet):
	queryset = Pais.objects.all()
	serializer_class = PaisSerializer

class ArtistaFilter(django_filters.FilterSet):
   class Meta:
        model = Artista
        fields = {
            'nombre': ['contains']
        }
        together = ['nombre']

class AlbumFilter(django_filters.FilterSet):
   class Meta:
        model = Album
        fields = {
            'nombre': ['contains']
        }
        together = ['nombre']

class CancionFilter(django_filters.FilterSet):
   class Meta:
        model = Cancion
        fields = {
            'nombre': ['contains']
        }
        together = ['nombre']

class ArtistaViewSet(viewsets.ModelViewSet):
	queryset = Artista.objects.all()
	serializer_class = ArtistaSerializer
	filter_class = ArtistaFilter

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object()
		serializer = self.get_serializer(instance)
		return Response(serializer.data)
	
	@action(detail=True, methods=['get'])
	def albumes(self, request, pk):
		albumes = Album.objects.filter(artista=pk)
		serializer = AlbumSerializer(albumes, many=True)
		return Response(serializer.data)
	
	@action(detail=True, methods=['get'])
	def canciones(self, request, pk):
		albumes = Album.objects.filter(artista=pk)
		canciones = Cancion.objects.filter(album__in=albumes)
		serializer = CancionSerializer(canciones, many=True)
		return Response(serializer.data)

class AlbumViewSet(viewsets.ModelViewSet):
	queryset = Album.objects.all()
	serializer_class = AlbumSerializer
	filter_class = AlbumFilter

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object()
		serializer = self.get_serializer(instance)
		return Response(serializer.data)

	@action(detail=True, methods=['get'])
	def canciones(self, request, pk):
		canciones = Cancion.objects.filter(album=pk)
		serializer = CancionSerializer(canciones, many=True)
		return Response(serializer.data)

class CancionViewSet(viewsets.ModelViewSet):
	queryset = Cancion.objects.all()
	serializer_class = CancionSerializer
	filter_class = CancionFilter

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