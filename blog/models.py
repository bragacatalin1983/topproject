from django.db import models
from datetime import datetime


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(blank=None)
    img = models.ImageField(upload_to='media/pictures')
    date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.title
