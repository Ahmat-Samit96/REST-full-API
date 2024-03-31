"""
URL configuration for movie_api_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from movies.views import (
    MovieListCreateAPIView, 
    MovieRetrieveUpdateDestroyAPIView,
    GenreListCreateAPIView,
    GenreRetrieveUpdateDestroyAPIView,
    ActorListCreateAPIView,
    ActorRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('admin/', admin.site.urls),
     path('api/movies/', MovieListCreateAPIView.as_view(), name='movie-list-create'),
    path('api/movies/<int:pk>/', MovieRetrieveUpdateDestroyAPIView.as_view(), name='movie-retrieve-update-destroy'),
    path('api/genres/', GenreListCreateAPIView.as_view(), name='genre-list-create'),
    path('api/genres/<int:pk>/', GenreRetrieveUpdateDestroyAPIView.as_view(), name='genre-retrieve-update-destroy'),
    path('api/actors/', ActorListCreateAPIView.as_view(), name='actor-list-create'),
    path('api/actors/<int:pk>/', ActorRetrieveUpdateDestroyAPIView.as_view(), name='actor-retrieve-update-destroy')

]
