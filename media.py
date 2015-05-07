class Movie:
    """Movie class.  Stores all data"""

    def __init__(self, name, img, trailer):
        """
        name -- Title of movie
        img -- URL of boxart
        trailer -- URL of trailer
        """
        self.title = name
        self.poster_image_url = img
        self.trailer_youtube_url = trailer
        
