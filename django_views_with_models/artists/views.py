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
    fname = request.GET.get('first_name')
    db_artists = Artist.objects.all()

    if fname:
        db_artists = db_artists.filter(first_name__icontains = fname)
    
    popularity = request.GET.get('popularity')
    if popularity:
        db_artists = db_artists.filter(popularity__gte = popularity)
    
    return render(request, 'artists.html', {'artists': db_artists})


def artist(request, artist_id):
    """
        - Task 4: Implement a view under /artists/<artist_id> that takes the
        given artist_id in the URL and gets the proper Artist object from
        the DB. Then render the 'artist.html' template sending the 'artist'
        object as context
    """
    db_artist = Artist.objects.get(id = artist_id)
    
    return render(request, 'artist.html', {'artist': db_artist})


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
    db_songs = Song.objects.all()
    title = request.GET.get('title')
    
    if artist_id:
        db_songs = db_songs.filter(artist_id = artist_id)
    if title:
        db_songs = db_songs.filter(title__icontains = title)
    for song in db_songs:
        artist = Artist.objects.get(id = song.artist_id)
        song.artist = artist
    
    return render(request, 'songs.html', {'songs': db_songs})
