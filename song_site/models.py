from django.db import models
from django.core.validators import MinValueValidator

# Model Class for song and related data.

class Song(models.Model):
    name = models.CharField(max_length=64)
    artist = models.CharField(max_length=64)
    songId = models.CharField(max_length=128, primary_key=True)

    def __str__(self):
        return "NAME: " + self.name + "\tARTIST: " + self.artist + "\tID: " + self.songId
