from http import HTTPStatus

from django.test import TestCase
from .models import Audiobook, Podcast, Song
from django.urls import reverse
from django.utils import timezone
from datetime import datetime, timedelta


# Create your tests here.
def create_song(name,duration_in_sec,upload_time):
    try:
        song = Song.objects.create(name=name,
                                   duration_in_sec=duration_in_sec,
                                   upload_time=upload_time)
        return True,song;
    except Exception:
        return False, -1


def create_song_dict(name,duration_in_sec,upload_time):
    return {"name": name, "duration_in_sec": duration_in_sec, "upload_time": upload_time}


def create_podcast(name,duration_in_sec,upload_time,host,participants):
    return Podcast.objects.create(name=name,
                                  duration_in_sec=duration_in_sec,
                                  upload_time=upload_time,
                                  host=host,
                                  participants=participants)


def create_podcast_dict(name, duration_in_sec, upload_time, host, participants):
    return {"name": name,
            "duration_in_sec": duration_in_sec,
            "upload_time": upload_time,
            "host": host,
            "participants": participants}


def create_audiobook(title,author,narrator,duration_in_sec,upload_time):
    return Audiobook.objects.create(title=title,
                                    author=author,
                                    narrator=narrator,
                                    duration_in_sec=duration_in_sec,
                                    upload_time=upload_time)


class SongCreateViewTests(TestCase):
    def test_no_songs(self):
        response = self.client.get(reverse("get", args=["song"]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Songs are Available")
        self.assertQuerysetEqual(response.context['ls'], [])

    def test_song_empty_data(self):
        song = create_song_dict("", 10, timezone.localtime(timezone.now()))
        response = self.client.post(reverse('create', args=("song",)), data= song)
        self.assertEqual(response.status_code, 500)

    def test_song_valid_data(self):
        song = create_song_dict("song2", 10, timezone.localtime(timezone.now()) + timedelta(minutes=2))
        response = self.client.post(reverse('create', args=("song",)), data=song)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(response["Location"], reverse('get', args=("song",)))

    def test_song_invalid_duration(self):
        song = create_song_dict("song2", -2, timezone.localtime(timezone.now()) + timedelta(minutes=2))
        response = self.client.post(reverse('create', args=("song",)), data=song)
        self.assertEqual(response.status_code, 500)

    def test_song_invalid_api(self):
        song = create_song_dict("song2", -2, timezone.localtime(timezone.now()) + timedelta(minutes=2))
        response = self.client.post(reverse('create', args=("song1",)), data=song)
        self.assertEqual(response.status_code, 400)

    def test_song_invalid_upload_time(self):
        song = create_song_dict("song3", 20, timezone.localtime(timezone.now()) - timedelta(minutes=2))
        response = self.client.post(reverse('create', args=("song",)), data=song)
        self.assertEqual(response.status_code, 500)

    def test_no_of_songs(self):
        response = self.client.get(reverse("get", args=["song"]))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['ls'], Song.objects.all())
