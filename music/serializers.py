from .models import *
from rest_framework import serializers

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ['id', 'nombre', 'iso']

class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = ['id', 'nombre', 'acerca', 'nacionalidad', 'nacionalidad_nombre']

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'nombre', 'portada', 'descripcion', 'anio', 'artista', 'artista_nombre', 'numero_canciones', 'duracion']

class CancionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancion
        fields = ['id', 'nombre', 'duracion', 'album', 'album_nombre']