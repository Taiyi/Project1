import media

Dredd = media.Movie("Dread",
              "http://upload.wikimedia.org/wikipedia/en/1/16/Dredd2012Poster.jpg",
              "https://www.youtube.com/watch?v=DLmnJvK0DjI")

Oblivion = media.Movie("Oblivion",
              "http://upload.wikimedia.org/wikipedia/en/2/2e/Oblivion2013Poster.jpg",
              "https://www.youtube.com/watch?v=XmIIgE7eSak")

JohnWick = media.Movie("John Wick",
              "http://upload.wikimedia.org/wikipedia/en/9/98/John_Wick_TeaserPoster.jpg",
              "https://www.youtube.com/watch?v=2AUmvWm5ZDQ")

SherlockHolmes = media.Movie("Sherlock Holmes: A Game of Shadows",
              "https://pmcdeadline2.files.wordpress.com/2011/12/sherlock-holmes-a-game-of-shadows-poster__111218082858.jpg",
              "https://www.youtube.com/watch?v=eSDqyX8Ahpo")

OceansThirteen = media.Movie("Ocean's Thirteen",
              "http://upload.wikimedia.org/wikipedia/en/c/c1/Oceans13Poster1.jpg",
              "https://www.youtube.com/watch?v=L-EyG12LxME")

WallE = media.Movie("WALL-E",
              "http://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",
              "https://www.youtube.com/watch?v=alIq_wG9FNk")


def populateList():
    """
    Creates a list of movie objects
    """
    movielist = []
    movielist.append(Dredd)
    movielist.append(Oblivion)
    movielist.append(JohnWick)
    movielist.append(SherlockHolmes)
    movielist.append(OceansThirteen)
    movielist.append(WallE)
    return movielist
