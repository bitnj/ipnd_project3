import webbrowser


class Video():
    """a class for storing generic information about movies and tv shows"""

    def __init__(self, title, storyline, length_in_minutes, genre, year_made):
        self.title = title
        self. storyline = storyline
        self.length_in_minutes = length_in_minutes
        self.genre = genre
        self.year_made = year_made


class Movie(Video):
    """a class for storing information related to movie.  Inherets from Video"""
    
    def __init__(self, title, storyline, length_in_minutes, genre, year_made,
            poster_image, trailer_youtube):
        # inhereted properties from Video
        Video.__init__(self, title, storyline, length_in_minutes, genre, 
                year_made)
        # properties unique to Movie
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
