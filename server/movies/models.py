from django.db import models

# Create your models here.

# first is to create models


class Genre(models.Model):
    """Holds genre like action, triller"""
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Movie(models.Model):
    """Lost of movie"""
    name = models.CharField(max_length=250)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    stars = models.FloatField(default=1.0)
    description = models.TextField()
    create = models.TextField(auto_created=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    """Store comment from user"""
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    comment = models.TextField()
    visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)