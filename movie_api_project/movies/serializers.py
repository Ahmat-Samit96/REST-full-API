from rest_framework import serializers
from .models import Movie, Genre, Actor

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(many=True, queryset=Genre.objects.all())
    actors = serializers.PrimaryKeyRelatedField(many=True, queryset=Actor.objects.all())

    class Meta:
        model = Movie
        fields = '__all__'
