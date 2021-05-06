from django import forms
from .models import Audiobook, Podcast, Song


class CreateNewSong(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Song
        fields = "__all__"


class CreateNewPodcast(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Podcast
        fields = "__all__"


class CreateNewAudiobook(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Audiobook
        fields = "__all__"

