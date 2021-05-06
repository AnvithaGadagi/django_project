from django.contrib import admin
from .models import Audiobook, Podcast, Song


# Register your models here.
admin.site.register(Audiobook)
admin.site.register(Podcast)
admin.site.register(Song)

