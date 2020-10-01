from django.contrib import admin
from .models import *

class PaisAdmin(admin.ModelAdmin):
	class Meta:
		model = Pais

class ArtistaAdmin(admin.ModelAdmin):
	class Meta:
		model = Artista

class AlbumAdmin(admin.ModelAdmin):
	class Meta:
		model = Album

class CancionAdmin(admin.ModelAdmin):
	class Meta:
		model = Cancion
    
admin.site.register(Pais, PaisAdmin)
admin.site.register(Artista, ArtistaAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Cancion, CancionAdmin)
