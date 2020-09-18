from django.contrib import admin
from .models import Art, Profile, Comment

# Register your models here.
admin.site.register(Art)
admin.site.register(Profile)
admin.site.register(Comment)