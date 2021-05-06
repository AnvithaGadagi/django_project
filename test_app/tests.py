from django.test import TestCase
from .models import Audiobook, Podcast, Song
from django.urls import reverse
from django.utils import timezone
from datetime import datetime, timedelta


# Create your tests here.
def create_song(name,duration_in_sec,upload_time):
    return Song.objects.create(name=name,
                               duration_in_sec=duration_in_sec,
                               upload_time=upload_time)


def create_podcast(name,duration_in_sec,upload_time,host,participants):
    return Podcast.objects.create(name=name,
                                  duration_in_sec=duration_in_sec,
                                  upload_time=upload_time,
                                  host=host,
                                  participants=participants)


def create_audiobook(title,author,narrator,duration_in_sec,upload_time):
    return Audiobook.objects.create(title=title,
                                    author=author,
                                    narrator=narrator,
                                    duration_in_sec=duration_in_sec,
                                    upload_time=upload_time)


class SongCreateViewTests(TestCase):
    def test_no_songs(self):
        response = self.client.get(path="http://127.0.0.1:8000/song/")
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Songs are Available")
        self.assertQuerysetEqual(response.context['ls'], [])
