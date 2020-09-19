import datetime
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# tags see https://django-tagging.readthedocs.io/en/develop/
# Create your models here.

MEDIA_TYPES = (
    ('C', 'Camera Photography'),
    ('D', 'Digital Artwork'),
    ('J', 'CSS codepen'),
    ('P', 'Painting'),
    ('S', 'Sketch Drawing'),
)

ARTIST_TYPES = (
    ('1', ('Photographer')),
    ('2', ('Painter')),
    ('3', ('Digital Illustrator')),
)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    birthday = models.DateField(default='2020-09-17')
    artist_type = models.CharField(max_length=25, choices=ARTIST_TYPES, default=MEDIA_TYPES[0][0])
    is_public = models.BooleanField(default=True)
    location = models.CharField(max_length=100)
    profile_img = models.CharField(max_length=100)
    points = models.IntegerField(default=1)

    def get_absolute_url(self):
        return reverse ('profile_detail', kwargs={'user_id': self.user.id})

class Art(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    media_type = models.CharField(max_length=1, choices=MEDIA_TYPES)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    colors_used = models.TextField(max_length=250)
    karma = models.IntegerField(default=1)
    date_posted = models.DateField()
    is_public = models.BooleanField(default=True)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('art_index')

class Comment(models.Model):
    comment = models.TextField(max_length=500)
    rating = models.IntegerField()
    date_created = models.DateField()
    art = models.ForeignKey(Art, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('gallery_detail', kwargs={ 'art_id': self.art.id })