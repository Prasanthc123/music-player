from django.shortcuts import render
from app.models import *
# Create your views here.
def song_list(request):
    songs = Song.objects.all()
    return render(request, 'app/song_list.html', {'songs': songs})

def playlist_detail(request, playlist_id):
    playlist = Playlist.objects.get(id=playlist_id)
    return render(request, 'app/playlist_detail.html', {'playlist': playlist})

def base(request):
    return render(request,'base.html')