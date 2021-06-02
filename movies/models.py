from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    release = models.IntegerField()
    daily_rate = models.FloatField()
    in_stock = models.BooleanField()

    def __str__(self):
        return self.name
