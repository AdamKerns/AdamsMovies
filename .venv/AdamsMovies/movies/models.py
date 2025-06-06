from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    pScore = models.FloatField()
    rtScore = models.FloatField()
    iScore = models.FloatField()
    link = models.CharField(max_length=255)
    genre_list = models.CharField(max_length=255)
    myScore = models.FloatField(max_length=255)
    summary = models.CharField(max_length=510)
    award_list = models.CharField(max_length=510)
    must_watch = models.BooleanField()