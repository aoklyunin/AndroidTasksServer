from django.db import models


class Task(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    solved = models.BooleanField(default=False)
