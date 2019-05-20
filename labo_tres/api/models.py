from django.db import models

class Planet(models.Model):
    _id = models.IntegerField(unique=True)
    name = models.CharField(max_length=50, default="")
    galaxy_name = models.CharField(max_length=50, default="")
    mass = models.CharField(max_length=50, default="")
    mean_radius = models.CharField(max_length=50, default="")
    number_of_stars = models.IntegerField(default=0)
    mean_temperature = models.FloatField(default=0.0)
    average_orbital_speed = models.FloatField(default=0.0)
    pressure = models.FloatField(default=0.0)
    discoverer = models.CharField(max_length=50, default="")