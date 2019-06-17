from django.shortcuts import render
from django.http import HttpResponseNotFound

from .models import Artist, Song


def artists(request):
    
    if request.GET.get('first_name'):
        artists = Artist.objects.filter(first_name__icontains=request.GET.get('first_name'))
	
    elif request.GET.get('popularity'):
        artists = Artist.objects.filter(popularity__gte=request.GET.get('popularity'))
    
    else:
        artists = Artist.objects.all()
		
    return render(request,'artists.html',{'artists':artists})
	 

    

def artist(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
	
    return render(request,'artist.html',{'artist':artist})
    

def songs(request, artist_id=None):
    
    songs = Song.objects.all()
	
    if artist_id:
        songs = [song for song in songs if song.artist_id == artist_id]
        for song in songs:
            song.artist = Artist.objects.get(id=artist_id)

    if request.GET.get('title'):
        songs =[song for song in songs if song.title==request.GET.get('title')]
	
    return render(request,'songs.html',{'songs':songs,})
    
    