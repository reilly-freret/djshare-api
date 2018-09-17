from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserExt(models.Model):
    username = models.CharField(max_length=255, null=True, blank=True)
    firstName = models.CharField(max_length=127, null=True, blank=True)
    lastName = models.CharField(max_length=127, null=True, blank=True)
    spotifyID = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return str(self.username)


class Song(models.Model):
    # title = models.CharField(max_length=255)
    # artist = models.CharField(max_length=255)
    # album = models.CharField(max_length=255, null=True, blank=True)
    # duration = models.IntegerField()
    # upvotes = models.IntegerField(default=0)
    # downvotes = models.IntegerField(default=0)
    # dateAdded = models.DateTimeField(auto_now=True)
    spotifyID = models.CharField(max_length=255)

    def __str__(self):
        return str(self.title)


class Party(models.Model):
    name = models.CharField(max_length=255)
    passKey = models.CharField(max_length=255, null=True)
    creator = models.ForeignKey(UserExt, on_delete=models.CASCADE)
    members = models.ManyToManyField(UserExt, related_name="parties", null=True, blank=True)
    queue = models.ManyToManyField(Song, related_name="partyQueueSongs", null=True, blank=True)
    stream = models.ManyToManyField(Song, related_name="partyStreamSongs", null=True, blank=True)
    location = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.creator.username)


class Artist(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255, default="null")
    spotifyID = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Album(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255, default="null")
    artist = models.ForeignKey(Artist, related_name="albums", on_delete=models.CASCADE)
    spotifyID = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Playlist(models.Model):
    name = models.CharField(max_length=255)
    creator = models.ForeignKey(UserExt, related_name="playlists", on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song, null=True, blank=True)
    spotifyID = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.name)
