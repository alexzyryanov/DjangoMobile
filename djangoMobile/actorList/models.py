from django.db import models

class Actor(models.Model):
    name_actor = models.CharField(max_length=200)
    image_actor = models.TextField()

    def __str__(self):
        return self.name_actor
