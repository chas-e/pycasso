from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    ARTIST_TYPES = (
        (1, ('Photographer')),
        (2, ('Painter')),
        (3, ('Digital Illustrator'))
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    birthday = models.DateField()
    artist_type = models.CharField(max_length=25, choices=ARTIST_TYPES)
    is_public = models.BooleanField(default=True)
    location = models.CharField(max_length=100)
    profile_img = models.CharField(max_length=100)
    points = models.IntegerField(default=1)


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
    media_type = models.CharField(max_length=1, choices=MEDIA_TYPES)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    # tags see https://django-tagging.readthedocs.io/en/develop/
    colors_used = models.TextField(max_length=250)
    karma = models.IntegerField(default=1)
    date_posted = models.DateField()
    is_public = models.BooleanField(default=True)

