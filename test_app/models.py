from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from django_mysql.models import ListCharField


def validate_date(date):
    if date < timezone.localtime(timezone.now() + timedelta(seconds=-5)):
        raise ValidationError("Date cannot be in the past")


# Abstract class to store the similar fields of the database
class MainClass(models.Model):
    # name - mandatory, max_length = 100
    name = models.CharField(max_length=100)
    # duration_in_sec - mandatory, integer positive
    duration_in_sec = models.PositiveIntegerField()
    # upload_time - mandatory, DateTime, cannot be in the past
    upload_time = models.DateTimeField(validators=[validate_date])

    # Get name when requested for the data
    def __str__(self):
        return self.name

    class Meta:
        abstract = True


# Song table contains same fields as the MainClass
class Song(MainClass):
    pass


# Podcast table contains MainClass fields with added fields
class Podcast(MainClass):
    # host - mandatory, string, max_length=100
    host = models.CharField(max_length=100)
    # participants - list of string, each string max_length= 100, max_participants = 10
    participants = ListCharField(
        base_field=models.CharField(max_length=100),
        size=10,
        max_length=(10 * 101))

    # Get name when requested for the data
    def __str__(self):
        return self.name

# Audiobook table field values
class Audiobook(models.Model):
    # Title of the Audiobook - string, max_length =100
    title = models.CharField(max_length=100)
    # Author of the Audiobook - string, max_length =100
    author = models.CharField(max_length=100)
    # Narrator of the Audiobook - string, max_length =100
    narrator = models.CharField(max_length=100)
    # duration_in_sec - mandatory, integer positive
    duration_in_sec = models.PositiveIntegerField()
    # upload_time - mandatory, DateTime, cannot be in the past
    upload_time = models.DateTimeField(validators=[validate_date])

    def __str__(self):
        return self.title
