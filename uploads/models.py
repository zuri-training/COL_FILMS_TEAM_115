from django.db import models
from django.contrib.auth.models import User
from pymediainfo import MediaInfo
from django.core.exceptions import ValidationError
import uuid
from pprint import pprint

# Create your models here.
def validate_video(video):
    media_info = MediaInfo.parse(video)
    if len(media_info.tracks) == 1:
        raise ValidationError('Not a valid video')
    track = media_info.tracks[1]
    if track.track_type == "Video":
        if track.duration > 900000:
            raise ValidationError('Video should not be longer than 15minutes')
    else:
        raise ValidationError(f'This is a {track.track_type} file. File must be in video format.')

# Create your models here.
class Upload(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    no_of_reacts = models.IntegerField(default=0)
    video_path = models.FileField('Video', upload_to='videos', validators=[validate_video])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
