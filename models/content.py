import uuid

class Content:
    def __init__(self, title=None, duration=None, year=None, rating=None, category=None):
        self.title = title
        self.duration = duration
        self.year = year
        self.rating = rating
        self.category = category
