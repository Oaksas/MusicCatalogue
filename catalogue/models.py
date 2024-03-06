from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, unique=True)
    bio = models.TextField(null=True, blank=True,
                           help_text="Enter a brief bio")
    song_total = models.IntegerField(default=0)
    choices = models.TextField(
        choices=[('1', 'Choice 1'), ('2', 'Choice 2')], blank=True, null=True)
    favorite = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class Album(models.Model):
    title = models.CharField(max_length=100)
    released_on = models.DateTimeField(blank=True, null=True)
    artists = models.ManyToManyField('Artist')


class Song(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
