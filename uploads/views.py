from django.shortcuts import render
from .forms import UploadForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from moviepy.editor import VideoFileClip

# Create your views here.
@login_required
def upload(request):
    form = UploadForm()
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        # context['form'] = form
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()
            messages.success(request, "Successfully Uploaded!")
    context = {
        'form': form
    }
    return render(request, 'apps/upload.html', context)
