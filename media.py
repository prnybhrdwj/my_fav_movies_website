import webbrowser

# This document will have all the constructors listed


class Media():
    '''
    We are defining a constructor of Media so that we
    can reuse it for tv series, documentaries, etc as well as movies.
    Args:
        media_type (str) = Describes the type of media, usually Movie or Video

    Returns:
        An instance of Media that can be either "Movie" or "Video".
    '''
    def __init__(self, media_type):
        self.media_type = media_type

# We will define child class movie here.


class Movie(Media):
    '''
    We are defining a child class of Media - Movie.
    The __init__ function accepts the media_type arg from Media class,
    as well as its own args.
    Args:
        media_type (str) = Describes the type of media, usually Movie or Video
        movie_title (str) = Movie names from the real world
        movie_storyline (str) = One line plot of the movie
        poster_image (str) = URL of movie poster hosted on internet
        trailer_youtube (str) = URL of movie trailer pointing to YouTube

    Returns:
        An instance of a movie with the above mentioned attributes

    The show_trailer function opens the youtube url link when it is called.
    '''
    def __init__(
            self, media_type, movie_title, movie_storyline,
            poster_image, trailer_youtube):
        Media.__init__(self, media_type)
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
