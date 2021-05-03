from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Artistas, Albumes, Canciones
from . serializers import ArtistasSerializer, AlbumesSerializer, CancionesSerializer
from base64 import b64encode

class Artists(APIView):

    def get(self, request):
        artista1 = Artistas.objects.all()
        serializer = ArtistasSerializer(artista1, many=True)
        return Response(serializer.data)

    def post(self, request):
        datos=request.data
        name=datos['name']
        id=b64encode(name.encode()).decode('utf-8')
        id=id[0:22]
        age=datos['age']
        albums=f'http://localhost:8000/artists/{id}/albums'
        tracks=f'http://localhost:8000/artists/{id}/tracks'
        self=f'http://localhost:8000/artists/{id}'
        nuevo_artista = Artistas(id=id, name=name, age=age, albums=albums, tracks=tracks)
        nuevo_artista.self = self
        nuevo_artista.save()
        serializer = ArtistasSerializer(nuevo_artista)
        return Response(serializer.data)

class Artist_id(APIView):

    def get(self, request, id):
        artista1 = Artistas.objects.get(id=id)
        serializer = ArtistasSerializer(artista1)
        return Response(serializer.data)

    def delete(self, request, id):
        albumes1 = Albumes.objects.filter(artist_id=id)
        for album in albumes1:
            tracks1 = Canciones.objects.filter(album_id=album.id)
            for cancion in tracks1:
                cancion.delete()
            album.delete()
        artista1 = Artistas.objects.get(id=id)
        artista1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Artist_albums(APIView):

    def get(self, request, id):
        albumes1 = Albumes.objects.filter(artist_id=id)
        serializer = AlbumesSerializer(albumes1, many=True)
        return Response(serializer.data)

    def post(self, request, id):
        datos=request.data
        name=datos['name']
        nombre=f'{name}:{id}'
        artist_id=id
        id_album=b64encode(nombre.encode()).decode('utf-8')
        id_album=id_album[0:22]
        genre=datos['genre']
        artist=f'http://localhost:8000/artists/{artist_id}'
        tracks=f'http://localhost:8000/albums/{id_album}/tracks'
        self=f'http://localhost:8000/albums/{id_album}'
        nuevo_album = Albumes(id=id_album, artist_id=artist_id, name=name, genre=genre, artist=artist, tracks=tracks)
        nuevo_album.self = self
        nuevo_album.save()
        serializer = AlbumesSerializer(nuevo_album)
        return Response(serializer.data)

class Artist_tracks(APIView):

    def get(self, request, id):
        albumes1 = Albumes.objects.filter(artist_id=id)
        todas = []
        for album in albumes1:
            canciones1 = Canciones.objects.filter(album_id=album.id)
            for cancion in canciones1:
                todas.append(cancion)
        serializer = CancionesSerializer(todas, many=True)
        return Response(serializer.data)

class Artist_play(APIView):

    def put(self, request, id):
        albumes1 = Albumes.objects.filter(artist_id=id)
        for album in albumes1:
            canciones1 = Canciones.objects.filter(album_id=album.id)
            for cancion in canciones1:
                cancion.times_played += 1
                cancion.save()
        return Response(status=status.HTTP_201_CREATED)

class Albums(APIView):

    def get(self, request):
        album1 = Albumes.objects.all()
        serializer = AlbumesSerializer(album1, many=True)
        return Response(serializer.data)

class Album_id(APIView):

    def get(self, request, id):
        album1 = Albumes.objects.get(id=id)
        serializer = AlbumesSerializer(album1)
        return Response(serializer.data)

    def delete(self, request, id):
        tracks1 = Canciones.objects.filter(album_id=id)
        for cancion in tracks1:
            cancion.delete()
        album = Albumes.objects.filter(id=id)
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Album_tracks(APIView):

    def get(self, request, id):
        tracks1 = Canciones.objects.filter(album_id=id)
        serializer = CancionesSerializer(tracks1, many=True)
        return Response(serializer.data)

    def post(self, request, id):
        datos=request.data
        name=datos['name']
        nombre=f'{name}:{id}'
        album_id=id
        id_cancion=b64encode(nombre.encode()).decode('utf-8')
        id_cancion=id_cancion[0:22]
        duration=datos['duration']
        times_played=0
        album1 = Albumes.objects.get(id=album_id)
        artist_id=album1.artist_id
        artist=f'http://localhost:8000/artists/{artist_id}'
        album=f'http://localhost:8000/albums/{album_id}'
        self=f'http://localhost:8000/tracks/{id_cancion}'
        nueva_cancion = Canciones(id=id_cancion, album_id=album_id, name=name, duration=duration, times_played=times_played, artist=artist, album=album)
        nueva_cancion.self = self
        nueva_cancion.save()
        serializer = CancionesSerializer(nueva_cancion)
        return Response(serializer.data)

class Album_play(APIView):

    def put(self, request, id):
        tracks1 = Canciones.objects.filter(album_id=id)
        for cancion in tracks1:
            cancion.times_played += 1
            cancion.save()
        return Response(status=status.HTTP_201_CREATED)

class Tracks(APIView):

    def get(self, request):
        cancion1 = Canciones.objects.all()
        serializer = CancionesSerializer(cancion1, many=True)
        return Response(serializer.data)

class Track_id(APIView):

    def get(self, request, id):
        cancion1 = Canciones.objects.get(id=id)
        serializer = CancionesSerializer(cancion1)
        return Response(serializer.data)

    def delete(self, request, id):
        cancion1 = Canciones.objects.get(id=id)
        cancion1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Track_play(APIView):

    def put(self, request, id):
        cancion = Canciones.objects.get(id=id)
        cancion.times_played += 1
        cancion.save()
        return Response(status=status.HTTP_201_CREATED)
    