from django import forms
from django.contrib.auth.models import User
from .models import Upload


class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ('title', 'description', 'video_path')

    

