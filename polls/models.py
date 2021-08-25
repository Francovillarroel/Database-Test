from django.db import models


class Movie(models.Model):
    movie_name = models.CharField(max_length=30)


class Director(models.Model):
    director_firstname = models.CharField(max_length=30)
    director_lastname = models.CharField(max_length=30)


class Actor(models.Model):
    actor_firstname = models.CharField(max_length=30)
    actor_lastname = models.CharField(max_length=30)
