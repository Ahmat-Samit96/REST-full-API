from django.db import models

# Create your models here.
from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")

    def __str__(self):
        return self.name

class Actor(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="ФИО")

    def __str__(self):
        return self.full_name

class Movie(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    year = models.IntegerField(verbose_name="Год выпуска")
    director = models.CharField(max_length=100, verbose_name="Режиссер")
    length = models.DurationField(verbose_name="Продолжительность")
    rating = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Рейтинг")
    genres = models.ManyToManyField(Genre, verbose_name="Жанры")
    actors = models.ManyToManyField(Actor, verbose_name="Актеры")
    plot = models.TextField(verbose_name="Сюжет")
    poster = models.ImageField(upload_to="movie_posters/", verbose_name="Постер", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кинофильм"
        verbose_name_plural = "Кинофильмы"
