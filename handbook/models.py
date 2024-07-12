from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField  # type: ignore
# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=65)  # type: ignore

    def __str__(self):
        return self.category


class Difficulty(models.Model):
    difficulty = models.CharField(max_length=65)  # type: ignore

    def __str__(self):
        return self.difficulty


class Moves(models.Model):
    # id
    movement_id = models.AutoField(primary_key=True)  # type: ignore

    # title
    title = models.CharField(max_length=120)  # type: ignore
    # title-slug
    title_slug = models.SlugField(unique=True)  # type: ignore
    # category
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 default=None)  # type: ignore
    # difficulty
    difficulty = models.ForeignKey(Difficulty, on_delete=models.SET_NULL,
                                   null=True,
                                   blank=True, default=None)  # type: ignore
    # video_link
    Video_link = EmbedVideoField()
    # is_published
    is_published = models.BooleanField(default=False)  # type: ignore
    # Author
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                               blank=True, default=None)  # type: ignore

    def __str__(self):
        return self.title
