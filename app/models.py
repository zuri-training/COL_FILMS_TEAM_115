from django.db import models

# Create your models here.
class ReactVideo(models.Model):
    video_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username
