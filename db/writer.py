import mysql.connector

import json

class DbWriter:
    def __init__(self):
        with open('./configs/db.json') as db_config:
            self.config = json.load(db_config)

            self.db = mysql.connector.connect (
                host=self.config['host'],
                user=self.config['user'],
                password=self.config['password'],
                database=self.config['database']
            )

    def write_movie(self, movie):
        if movie is not None:
            try:
                statement = 'INSERT INTO movies (title, duration, year, rating, category) VALUES (%s, %s, %s, %s, %s)'
                values = (movie.title, movie.duration, movie.year, movie.rating, movie.category)

                cursor = self.db.cursor()

                find_statment = f'SELECT * FROM movies WHERE title="{movie.title}" AND year="{movie.year}";'
                cursor.execute(find_statment)

                result = cursor.fetchall()

                if len(result) == 0:
                    cursor.execute(statement, values)
                    self.db.commit()
                else:
                    print("Duplicate movie found... not writing to database.")
            except:
                print(f'Could not write {movie.title}.')
        else:
            print(f'Error writing.')

        


