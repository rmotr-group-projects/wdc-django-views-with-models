from django.shortcuts import render
from django.http import HttpResponseNotFound

from .models import Artist, Song


def artists(request):
    """
        - Task 1: Implement a view under /artists URL that fetches all
        Artist's objects stored in the DB and render the 'artists.html'
        template sending all 'artists' as context.

        - Task 2: In this same view, check if a 'first_name' GET parameter
        is sent. If so, filter the previous queryset with ALL artists, in
        order to keep only the ones that contains the given pattern in its
        first_name

        - Task 3: Similar to previous task, take the 'popularity' GET
        parameter (if its given) and filter all the artists that have a
        popularity greater or equal to the given one.
    """
    artists_to_render = Artist.objects.all()

    if 'first_name' in request.GET and request.GET['first_name']:
        search = request.GET.get('first_name')
        artists_to_render = artists_to_render.filter(first_name__icontains=search)
    if 'popularity' in request.GET and request.GET['popularity']:
        pop = request.GET.get('popularity')
        artists_to_render = artists_to_render.filter(popularity__gte=pop)
    
    return render(request, 'artists.html',{
        'artists': artists_to_render,
    })
    


def artist(request, artist_id):
    """
        - Task 4: Implement a view under /artists/<artist_id> that takes the
        given artist_id in the URL and gets the proper Artist object from
        the DB. Then render the 'artist.html' template sending the 'artist'
        object as context
    """
    artist_to_render = Artist.objects.get(id = artist_id)
    return render(request, 'artist.html',{
        'artist': artist_to_render,
    })


def songs(request, artist_id=None):
    """
        - Task 5: Implement a view under /songs URL that display ALL the songs stored
        in the DB. In order to do this, fetch all the Song objects and
        render the 'songs.html' sending the 'songs' queryset as context.
        Before rendering the template, loop through the songs queryset and
        for each song, fetch the proper Artist object that matches with the
        artist_id from the song. Once you have the song's artist object, bind
        it like 'song.artist = artist'.

        - Task 6: Add a 'title' filter from a 'title' GET parameter (if given)
        that filters the 'songs' queryset for songs that contains that
        pattern, in a similar way that the tasks before.

        - Task 7: Add a new /songs/<artist_id> URL that points to this
        same view. If the artist_id is given, filter the songs queryset for
        songs that match with given artist_id and render the same 'songs.html'
        template.
    """
    songs_to_render = Song.objects.all()
    for song in songs_to_render:
        artist_id_for_song = song.artist_id
        song.artist = Artist.objects.get(id=artist_id_for_song)
    if artist_id:
        songs_to_render = songs_to_render.filter(artist_id=artist_id)
    if request.GET.get('title'):
        search = request.GET.get('title')
        songs_to_render = songs_to_render.filter(title__icontains=search)
    
    return render(request, 'songs.html',{
        'songs': songs_to_render,
    })

    
