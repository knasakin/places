from django.contrib.gis.db import models
from django.contrib.auth.models import User


class Place(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
