from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from uploads.models import Upload
from .models import ReactVideo, ShareVideo, Comment, Saved
from django.contrib import messages
from .forms import CommentForm


# Create your views here.
def index(request):
    # videos = Upload.objects.all()
    # paginator = Paginator(videos, 3)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    # context = {
    #     'videos' : page_obj
    # }
    if request.user.is_authenticated:
        return redirect('/home/')
    return render(request, 'apps/index.html', {})

@login_required
def home(request):
    videos = Upload.objects.all()
    if len(videos) > 0:
        latest_video = Upload.objects.latest('created_at')
    paginator = Paginator(videos, 5)
    first3 = Upload.objects.all().order_by('id')[:3]
    last3 = Upload.objects.filter().order_by('-id')[:3]
    # paginator2 = Paginator(videos, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # page_number2 = request.GET.get('page')
    # page_obj2 = paginator2.get_page(page_number2)
    context = {
        'videos' : page_obj,
        'first3' : first3,
        'last3' : last3,
        'last_v' : latest_video
    }
    return render(request, 'apps/home.html', context)

@login_required
def single_video(request):
    video_obj = Upload.objects.get(id=request.GET.get('video_id'))
    comment_qs = Comment.objects.filter(video=request.GET.get('video_id'))
    paginator = Paginator(comment_qs, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    form = CommentForm()
    context = {
        'video':video_obj,
        'form': form,
        'comments': page_obj,
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


@login_required
def share_video(request):
    username = request.user.username
    video_id = request.GET.get('video_id')

    new_share = ShareVideo.objects.create(video_id=video_id, username=username)
    new_share.save()
    messages.info(request, "Video haved been shared!!!")
    return redirect(f'/play-video/?video_id={video_id}')

@login_required
def comment(request):
    video_id = request.GET.get('video_id')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            new_comment = Comment.objects.create(user=request.user, comment=comment, video=video_id)
            new_comment.save()
        return redirect(f'/play-video/?video_id={video_id}')

@login_required
def save_video(request):
    video_id = request.GET.get('video_id')
    upload = Upload.objects.get(id=video_id)
    # print(upload)
    # video_qs = Saved.objects.filter(video=request.GET.get('video_id'), user=request.user).first()
    video_qs = Saved.objects.filter(video=upload, user=request.user).first()
    if video_qs is None:
        new_saved = Saved.objects.create(user=request.user, video=upload)  
        new_saved.save() 
        messages.info(request, "Video haved been saved!!!")
    else:
        messages.info(request, "Video already exist in your saved videos")
    return redirect(f'/play-video/?video_id={video_id}')

@login_required
def fetch_saved_video(request):
    # video_id = request.GET.get('video_id')
    video_qs = Saved.objects.filter(user=request.user)
    last_saved = video_qs.last()
    paginator = Paginator(video_qs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # print( video_qs.last().video.id)
    return render(request, 'apps/saved_video.html', {'videos': page_obj, 'last_saved': last_saved})









    
