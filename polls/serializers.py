from rest_framework import serializers
from . models import Artistas, Canciones, Albumes

class ArtistasSerializer(serializers.ModelSerializer):

    class Meta:
        model=Artistas
        fields=('id','name','age','albums','tracks','self')

class AlbumesSerializer(serializers.ModelSerializer):

    class Meta:
        model=Albumes
        fields=('id','artist_id','name','genre','artists','tracks','self')

class CancionesSerializer(serializers.ModelSerializer):

    class Meta:
        model=Canciones
        fields=('id','album_id','name','duration','times_played','artists','albums','self')
