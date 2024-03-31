from django.urls import path
from .views import (
    GenreListCreateAPIView,
    GenreRetrieveUpdateDestroyAPIView,
    ActorListCreateAPIView,
    ActorRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('api/genres/', GenreListCreateAPIView.as_view(), name='genre-list-create'),
    path('api/genres/<int:pk>/', GenreRetrieveUpdateDestroyAPIView.as_view(), name='genre-retrieve-update-destroy'),
    path('api/actors/', ActorListCreateAPIView.as_view(), name='actor-list-create'),
    path('api/actors/<int:pk>/', ActorRetrieveUpdateDestroyAPIView.as_view(), name='actor-retrieve-update-destroy'),
]
