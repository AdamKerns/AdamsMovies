from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    pScore = models.FloatField()
    rtScore = models.FloatField()
    iScore = models.FloatField()
    link = models.CharField(max_length=255)