"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from polls import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'artists/', views.Artists.as_view()),
    path(r'albums/', views.Albums.as_view()),
    path(r'tracks/', views.Tracks.as_view()),
    path('artists/<str:id>', views.Artist_id.as_view()),
    path('albums/<str:id>', views.Album_id.as_view()),
    path('tracks/<str:id>', views.Track_id.as_view()),
    path('artists/<str:id>/albums', views.Artist_albums.as_view()),
    path('artists/<str:id>/tracks', views.Artist_tracks.as_view()),
    path('albums/<str:id>/tracks', views.Album_tracks.as_view()),
    path('artists/<str:id>/albums/play', views.Artist_play.as_view()),
    path('albums/<str:id>/tracks/play', views.Album_play.as_view()),
    path('tracks/<str:id>/play', views.Track_play.as_view())
]
