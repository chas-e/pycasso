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
    (1, ('Photographer')),
    (2, ('Painter')),
    (3, ('Digital Illustrator')),
)


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
    colors_used = models.TextField(max_length=250)
    karma = models.IntegerField(default=1)
    date_posted = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('art_index')


class Photo(models.Model):
    url = models.CharField(max_length=200)
    art = models.ForeignKey(Art, on_delete=models.CASCADE)

    def __str__(self):
        return f'Photo for art_id: {self.art_id} @{self.url}'


class Files(models.Model):
    name = models.CharField(max_length=30)
    image = models.TextField()

    def __unicode__(self):
        return self.name
