from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from uploads.models import Upload
from .models import ReactVideo

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

@login_required
def react_video(request):
    username = request.user.username
    video_id = request.GET.get('video_id')

    upload_obj = Upload.objects.get(id=video_id)

    react_filter = ReactVideo.objects.filter(video_id=video_id, username=username).first()

    if react_filter == None:
        new_react = ReactVideo.objects.create(video_id=video_id, username=username)
        new_react.save()
        upload_obj.no_of_reacts = upload_obj.no_of_reacts+1
        upload_obj.save()
        print(f'{request.path_info}/?{video_id}')
        return redirect(f'/play-video/?video_id={video_id}')
    else:
        react_filter.delete()
        upload_obj.no_of_reacts = upload_obj.no_of_reacts-1
        upload_obj.save()
        return redirect(f'/play-video/?video_id={video_id}')


    
