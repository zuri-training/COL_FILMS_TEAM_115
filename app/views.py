from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from uploads.models import Upload

# Create your views here.
def index(request):
    videos = Upload.objects.all()
    paginator = Paginator(videos, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'videos' : page_obj
    }
    return render(request, 'apps/index.html', context)

@login_required
def single_video(request):
    video_obj = Upload.objects.get(id=request.GET.get('video_id'))
    context = {
        'video':video_obj
    }
    return render(request, 'apps/play_video.html', context)
    
