<img align="right" width="120" alt="rmotr.com" src="https://user-images.githubusercontent.com/7065401/45454218-80bee800-b6b9-11e8-97bb-bb5e7675f440.png">

# Django Views With Models

### Setup Instruction

The structure of the whole Django project is built for you. Run the following commands in order to have your local environment up and running.  

```bash
$ mkvirtualenv -p $(which python3.5) django_views_with_models
$ pip install -r requirements.txt
```

You can now run the development server and point the browser to the correct URL:

```bash
$ make runserver
```

You will have a superuser already created (username: admin, password: admin). To log in run the server and point your browser to http://localhost:8080/admin, (or on C9: http://django-orm-relationships-<your c9 username>.c9users.io:8080/admin. There you can find the Django admin site where you will be able to view, create, delete and modify objects from your database.

The database already contains some objects that we have created for you, but feel free to interact and have fun with it.


#### - Task 1:

A couple of Django models called `Artist` and `Song` are provided to you inside `artists/models.py`. For this task you'll have to implement a view inside `artists/views.py` that matches with the `/artists` URL path in `django_views_with_models/urls.py`.
This view will be in charge of fetching all `Artist` objects stored in the database (using the correct ORM command) and render the `artists.html` template. You will need to send the artists to the template in a context dictionary with the key 'artists' and the queryset as the value.

You can test the response of the view in your browser by pointing to `http://localhost:8080/artists/`, or on C9: `http://django-orm-relationships-<your C9 username>.c9users.io:8080/admin`. This is the expected result:

<img src="https://user-images.githubusercontent.com/2788551/47859330-db78e400-ddcc-11e8-9d2d-524787c756ec.png" width="50%" height="50%">


#### - Task 2:

In this task you'll extend the previous view with some functionality. The idea is to filter the list of artists by sending artists' names as GET parameters in the URL (i.e: `/artists?first_name=stev`).
For this, check if a `first_name` GET parameter is sent inside the `request.GET` dictionary. If so, filter the previous artists queryset that had ALL artists, in order to keep only the ones that contain the given pattern in their first_name.
The context while rendering the template will be the same as before, but now the artists queryset might have less artists, if a `first_name` parameter is given. The following image shows the expected result:

<img src="https://user-images.githubusercontent.com/2788551/39497588-65a6b6e0-4d7a-11e8-8f3b-4c5bbfb9cbfc.png" width="50%" height="50%">


#### - Task 3:

Similarly to the previous task, check if a `popularity` GET parameter is given in the URL and, if so, filter the artists queryset to artists who have a popularity greater than or equal to the given one.
It should work like this:

<img src="https://user-images.githubusercontent.com/2788551/39497601-7892d2b6-4d7a-11e8-8dfd-b658262a7146.png" width="50%" height="50%">

NOTE: Notice that you can send multiple GET parameters like this: `/artists?first_name=stev&popularity=80`


#### - Task 4:

For this task you'll implement a brand new view under the `/artist/<artist_id>` URL path. This view will take the given `artist_id`, get the proper Artist object from the database, and render the `artist.html` template with the artist object sent in a context dictionary.
If you want to check what id is associated with each artist, you can do it in the admin site at the `/admin/` URL.

<img src="https://user-images.githubusercontent.com/2788551/47860210-cb620400-ddce-11e8-9a9b-5dd04a2ef78b.png" width="50%" height="50%">


#### - Task 5:

Implement a view under the `/songs` URL path that displays ALL the songs stored in the database. In order to do this, fetch all the Song objects and render the `songs.html` template with the 'songs' queryset as context, much like we did with artists before.
But this time, before rendering the template, loop through the songs queryset and for each song, fetch the proper Artist object from the database that matches with the artist_id in the song. Once you have the song's artist object, bind it to the song object like this: 'song.artist = artist'.

<img src="https://user-images.githubusercontent.com/2788551/47859369-ee8bb400-ddcc-11e8-8ac1-ba0d9b845083.png" width="50%" height="50%">


#### - Task 6:

Add a `title` filter to the `songs()` view that takes a 'title' GET parameter (if given) and filters the 'songs' queryset for songs that contain that pattern, just like we did when filtering the artists.

<img src="https://user-images.githubusercontent.com/2788551/39501513-be973218-4d91-11e8-96c9-f43836cc1b42.png" width="50%" height="50%">


#### - Task 7:

Add a new `/songs/<artist_id>` URL that points to the SAME `songs()` view. Filter the songs queryset to contain only songs with a matching artist_id and render the same `songs.html` template.
Notice that this is NOT a GET parameter, but a parameter that comes in the URL path. So now the `songs()` view takes a new artist_id parameter which is set to None by default.
Remember that you can check which `id` is associated with each artist object in the Django admin page.

<img src="https://user-images.githubusercontent.com/2788551/47860340-11b76300-ddcf-11e8-8df2-02ffc2f6f2f6.png" width="50%" height="50%">

