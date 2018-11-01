<img align="right" width="120" alt="rmotr.com" src="https://user-images.githubusercontent.com/7065401/45454218-80bee800-b6b9-11e8-97bb-bb5e7675f440.png">

# Django Views With Models

### Setup Instruction

The structure of the whole Django project is built for you. Run the following commands in order to have your local environment up and running.  

```bash
$ mkvirtualenv -p $(which python3) django_orm_intro
$ pip install -r requirements.txt
$ make migrate
```

You can now run the development server and point the browser to the correct URL:

```bash
$ make runserver
```

A command to load some initial data into your database is also provided.

```bash
$ make load_initial_data
```

You should see an `Imported!` message when the command execution finishes. That mean all initial data was imported successfully.

This will also create a superuser (user: `admin`, password: `admin`) that you can use when you point to `http://localhost:8080/admin` in your browser with the server running. You will find the Django admin site where you can create, delete and modify objects from your database.


#### - Task 1:

A couple of Django models called `Artist` and `Song` are provided to you inside `artists/models.py`. For this task you'll have to implement a view inside `artists/views.py` that matches with `/artists` URL located in `django_views_with_models/urls.py`.
This view will be in charged of fetching all `Artist`'s objects stored in the database (previously loaded with the given command) and render the `artists.html` template sending all `artists` as context.

You can test the response of the view in your browser, pointing to `http://localhost:8080/artists/`. This is the expected result:

<img src="https://user-images.githubusercontent.com/2788551/47859330-db78e400-ddcc-11e8-9d2d-524787c756ec.png" width="50%" height="50%">


#### - Task 2:

In this task you'll extend the previous view with some functionality. The idea is to filter the list of artists by name sending GET parameters in the URL (i.e: `/artists?first_name=stev`).
For this, check if a `first_name` GET parameter is sent inside `request.GET` dictionary. If so, filter the previous artists queryset that had ALL artists, in order to keep only the ones that contains the given pattern in their first_name.
The context while rendering the template will be the same as before, but now the artists queryset might have less artists, if a `first_name` parameter is given. The following image shows the expected result:

<img src="https://user-images.githubusercontent.com/2788551/39497588-65a6b6e0-4d7a-11e8-8f3b-4c5bbfb9cbfc.png" width="50%" height="50%">


#### - Task 3:

In a similar way as done before, check if a `popularity` GET parameter is given in the URL and if so, filter the artists queryset by artists that have a popularity greater or equal to the one given.
It should work like this:

<img src="https://user-images.githubusercontent.com/2788551/39497601-7892d2b6-4d7a-11e8-8dfd-b658262a7146.png" width="50%" height="50%">

NOTE: Notice that you can send multiple GET parameters like this: `/artists?first_name=stev&popularity=80`


#### - Task 4:

For this task you'll implement a brand new view under `/artist/<artist_id>` URL. This view will take the given `artist_id`, get the proper Artist object from the database and render the `artist.html` template sending the artist object as context.
If you want to check what id is associated with each artist, you can do it in the admin page at `/admin/` URL.

<img src="https://user-images.githubusercontent.com/2788551/39497626-9f1ee55a-4d7a-11e8-94fe-b0f81c0e6c14.png" width="50%" height="50%">


#### - Task 5:

Implement a view under `/songs` URL that display ALL the songs stored in the database. In order to do this, fetch all the Song objects and render the `songs.html` sending the 'songs' queryset as context.
Before rendering the template, loop through the songs queryset and for each song, fetch the proper Artist object from the database that matches with the artist_id in the song. Once you have the song's artist object, bind it to the song object like 'song.artist = artist'.

<img src="https://user-images.githubusercontent.com/2788551/47859369-ee8bb400-ddcc-11e8-8ac1-ba0d9b845083.png" width="50%" height="50%">


#### - Task 6:

Add a `title` filter to the `songs()` view that takes 'title' GET parameter (if given) and filters the 'songs' queryset for songs that contains that pattern, in a similar way that the tasks before.

<img src="https://user-images.githubusercontent.com/2788551/39501513-be973218-4d91-11e8-96c9-f43836cc1b42.png" width="50%" height="50%">


#### - Task 7:

Add a new `/songs/<artist_id>` URL that points to the same `songs()` view. Filter the songs queryset for songs that match with given artist_id and render the same `songs.html` template.
Notice that this is NOT a GET parameter, but a parameter that comes in the URL path. So now the `songs()` view takes a new artist_id parameter which by default is set to None.
Remember that you can check which `id` is associated with each artist object in the Django admin page.

<img src="https://user-images.githubusercontent.com/2788551/39501602-401e5eb0-4d92-11e8-92a8-9fd1d5e3e1cb.png" width="50%" height="50%">
