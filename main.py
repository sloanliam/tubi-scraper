from scrapers.tubi_scraper import TubiScraper
from db.writer import DbWriter
from models.movie import Movie

import json

genre_list = []
tubi_scraper = TubiScraper()
db_writer = DbWriter()
movie_list = []

with open('./configs/tubi_genre_list.json') as genre_list_file:
    genre_list = json.load(genre_list_file)

for genre in genre_list:
    movie_by_genre = tubi_scraper.get_movies_by_genre(genre)
    print(f'Writing {genre} movies to database...')
    for movie in movie_by_genre:
        db_writer.write_movie(movie)




