from django.shortcuts import render
from uploads.models import Upload

# Create your views here.
def home(request):
    videos = Upload.objects.all()
    context = {
        'videos' : videos
    }
    return render(request, 'apps/home.html', context)
