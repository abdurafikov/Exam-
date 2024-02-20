# content_manager/models.py
from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    body = models.TextField()

    def str(self):
        return self.title