from django.db import models
from datetime import datetime


class Cursit(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    url = models.URLField(blank=None)
    img = models.ImageField(upload_to='media/picturesIT')
    description = models.TextField()

    def __str__(self):
        return self.title
