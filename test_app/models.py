from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from django_mysql.models import ListCharField


def validate_date(date):
    if date < timezone.localtime(timezone.now() + timedelta(seconds=-5)):
        raise ValidationError("Date cannot be in the past")


class MainClass(models.Model):
    name = models.CharField(max_length=100)
    duration_in_sec = models.PositiveIntegerField()
    upload_time = models.DateTimeField(validators=[validate_date])

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


# Create your models here.
class Song(MainClass):
    pass


class Podcast(MainClass):
    host = models.CharField(max_length=100)
    participants = ListCharField(
        base_field=models.CharField(max_length=100),
        size=10,
        max_length=(10 * 101))

    def __str__(self):
        return self.name


class Audiobook(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
    duration_in_sec = models.PositiveIntegerField()
    upload_time = models.DateTimeField(validators=[validate_date])

    def __str__(self):
        return self.title
