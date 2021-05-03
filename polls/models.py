from django.db import models

class Artistas(models.Model):
    id=models.CharField(max_length=500, primary_key=True)
    name=models.CharField(max_length=500)
    age=models.IntegerField()
    albums=models.CharField(max_length=500)
    tracks=models.CharField(max_length=500)
    self=models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Albumes(models.Model):
    id=models.CharField(max_length=500, primary_key=True)
    artist_id=models.CharField(max_length=500)
    name=models.CharField(max_length=500)
    genre=models.CharField(max_length=500)
    artist=models.CharField(max_length=500)
    tracks=models.CharField(max_length=500)
    self=models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Canciones(models.Model):
    id=models.CharField(max_length=500, primary_key=True)
    album_id=models.CharField(max_length=500)
    name=models.CharField(max_length=500)
    duration=models.FloatField()
    times_played=models.IntegerField()
    artist=models.CharField(max_length=500)
    album=models.CharField(max_length=500)
    self=models.CharField(max_length=500)

    def __str__(self):
        return self.name
    
