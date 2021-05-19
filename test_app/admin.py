from django.contrib import admin
from .models import Audiobook, Podcast, Song


# Register Audiobook, Podcast and Song models
admin.site.register(Audiobook)
admin.site.register(Podcast)
admin.site.register(Song)

