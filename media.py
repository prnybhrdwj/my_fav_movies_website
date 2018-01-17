import webbrowser

# This document will have all the constructors listed


class Media():
    '''We are defining a constructor of Media so that we
        can reuse it for tv series, documentaries, etc as well as movies'''
    def __init__(self, media_type):
        self.media_type = media_type

# We will define child class movie here.


class Movie(Media):
    '''We are defining a child class of Media - Movie.'''
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
