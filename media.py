import webbrowser

# the Movie class contains attribute title, poster_url, and trailer_url to store
# any movie's title, box art picture, and youtube trailer respectively
class Movie():
    def __init__(self, title, poster_url, trailer_url):
        # initializing instance variables
        self.title = title
        self.poster_url = poster_url
        self.trailer_url = trailer_url