from django.db import models

# Create your models here.
from django.db import models
from django.utils.datetime_safe import datetime


class Tag(models.Model):
    title = models.CharField(max_length=100)


class Post(models.Model):
    header = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    date = models.DateField(default='')
    text = models.TextField(default='')
    tag = models.ManyToManyField(Tag)
