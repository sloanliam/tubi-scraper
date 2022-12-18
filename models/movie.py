import uuid

class Movie:
    def __init__(self, title=None, duration=None, year=None, rating=None):
        self.title = title
        self.duration = duration
        self.year = year
        self.rating = rating
