from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from artists.models import Artist, Song
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Imports initial data'

    def handle(self, *args, **options):
        User.objects.all().delete()
        Artist.objects.all().delete()
        Song.objects.all().delete()

        User.objects.create_superuser(
            username='admin', email='admin@example.com', password='admin')

        ARTISTS = [
            ('Stevland', 'Judkins', 'Stevie Wonders', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Stevie_Wonder_1973.JPG/600px-Stevie_Wonder_1973.JPG', 90, 'rock'),
            ('James', 'Hendrix', 'Jimi Hendrix', 'https://upload.wikimedia.org/wikipedia/commons/a/ae/Jimi_Hendrix_1967.png', 80, 'rock'),
            ('Riley', 'King', 'B.B. King', 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/B.B._King_in_2009.jpg/600px-B.B._King_in_2009.jpg', 75, 'blues'),
        ]
        artists_ids = []
        for first_name, last_name, artistic_name, picture_url, popularity, genre in ARTISTS:
            artist = Artist.objects.create(
                first_name=first_name,
                last_name=last_name,
                artistic_name=artistic_name,
                picture_url=picture_url,
                popularity=popularity,
                genre=genre
            )
            artists_ids.append(artist.id)

        SONGS = [
            (artists_ids[0], 'Superstition', 'Talking book'),
            (artists_ids[0], 'Higher Ground', 'Innervisions'),
            (artists_ids[2], 'The Thrill Is Gone', 'Completely Well'),
        ]
        for artist_id, title, album_name in SONGS:
            Song.objects.create(
                artist_id=artist_id,
                title=title,
                album_name=album_name
            )
        print('Imported!')
