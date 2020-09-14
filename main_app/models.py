from django.db import models
from django.urls import reverse

# Create your models here.


class User(models.Model):
    pass


class Art(models.Model):
    MEDIA_TYPES = (
        ('C', 'Camera Photography'),
        ('D', 'Digital Artwork'),
        ('J', 'CSS codepen'),
        ('P', 'Painting'),
        ('S', 'Sketch Drawing'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    media_type = models.CharField(max_length=1, choices=MEDIA_TYPES)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    # tags see https://django-tagging.readthedocs.io/en/develop/
    colors_used = models.TextField(max_length=250)
    karma = models.IntegerField()
    date_posted = models.DateField()
