from scrapers.tubi_scraper import TubiScraper
from db.writer import DbWriter
from models.content import Content

import sys
import json

def populate_database():
    genre_list = []
    tubi_scraper = TubiScraper()
    db_writer = DbWriter()

    db_writer.setup_database()

    with open('./configs/tubi_genre_list.json') as genre_list_file:
        genre_list = json.load(genre_list_file)

    for genre in genre_list:
        content_by_genre = tubi_scraper.get_content_by_genre(genre)
        for content in content_by_genre:
            print(f'Writing {content.title} content to database...')
            db_writer.write_movie(content)

populate_database()




