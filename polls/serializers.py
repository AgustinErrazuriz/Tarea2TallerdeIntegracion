from rest_framework import serializers
from . models import Artistas, Canciones, Albumes

class ArtistasSerializer(serializers.ModelSerializer):

    class Meta:
        model=Artistas
        fields='__all__'

class AlbumesSerializer(serializers.ModelSerializer):

    class Meta:
        model=Albumes
        fields='__all__'

class CancionesSerializer(serializers.ModelSerializer):

    class Meta:
        model=Canciones
        fields='__all__'
