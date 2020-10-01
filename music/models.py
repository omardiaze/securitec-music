from django.db import models

class Pais(models.Model):
    nombre          = models.CharField(max_length=20, verbose_name='Nombre', unique=True)
    iso             = models.CharField(max_length=4, verbose_name='Iso', unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Pais"
        verbose_name_plural = "Paises"

class Artista(models.Model):
    nombre          = models.CharField(max_length=80, verbose_name='Nombre', unique=True)
    acerca          = models.TextField(max_length=250, verbose_name='Acerca de')
    nacionalidad    = models.ForeignKey(Pais, verbose_name="Nacionalidad", on_delete=models.PROTECT)


    def __str__(self):
        return self.nombre

    def nacionalidad_nombre(self):
        return self.nacionalidad.nombre if self.nacionalidad else ''

    class Meta:
        verbose_name = "Artista"
        verbose_name_plural = "Artistas"

class Album(models.Model):
    nombre          = models.CharField(max_length=80, verbose_name='Nombre', unique=True)
    portada         = models.ImageField(upload_to='portadas', null=True, blank=True )
    descripcion     = models.TextField(max_length=250, verbose_name='Descripcion')
    anio            = models.IntegerField(verbose_name="Año", null=True)
    artista         = models.ForeignKey(Artista, verbose_name="Artista", on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

    def artista_nombre(self):
        return self.artista.nombre if self.artista else ''

    class Meta:
        verbose_name = "Álbum"
        verbose_name_plural = "Álbumes"

class Cancion(models.Model):
    nombre          = models.CharField(max_length=80, verbose_name='Nombre', unique=True)
    duracion        = models.TimeField(verbose_name='Duración')
    album           = models.ForeignKey(Album, verbose_name="Álbum", on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

    def album_nombre(self):
        return self.album.nombre if self.album else ''

    class Meta:
        verbose_name = "Canción"
        verbose_name_plural = "Canciones"