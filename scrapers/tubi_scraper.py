import json
import time

from models.movie import Movie

from selenium import webdriver
from selenium.webdriver.common.by import By

class TubiScraper:
    def __init__(self, headless=True, buffer_time=3, scroll_speed=5, scroll_buffer=5):
        self.driver = webdriver.Edge(options=self.__create_options(headless))
        self.buffer_time = buffer_time
        self.scroll_speed = scroll_speed
        self.scroll_buffer = scroll_buffer

        with open('./configs/tubi_config.json') as config_file:
            self.config = json.load(config_file)

    def create_genre_list(self):
        self.driver.get(self.config['homeUrl'])

        time.sleep(self.buffer_time)

        self.driver.find_element(By.CLASS_NAME, self.config['classNames']['sideBar']).click()

        time.sleep(self.buffer_time)

        genres = self.driver.find_elements(By.CLASS_NAME, self.config['classNames']['genres'])
        genre_list = []

        for genre in genres:
            genre_list.append(genre.get_attribute('href'))

        json_object = json.dumps(genre_list)

        with open("./configs/tubi_genre_list.json", "w") as outfile:
            outfile.write(json_object)

    def __create_options(self, headless):
        self.driver_options = webdriver.EdgeOptions()

        if headless is True:
            self.driver_options.add_argument("--headless")

        return self.driver_options

    def __preload(self):
        page_height = int(self.driver.execute_script('return document.body.scrollHeight'))

        for i in range(0, page_height * self.scroll_buffer, self.scroll_speed):
            self.driver.execute_script("window.scrollTo(0, {});".format(i))

    def get_movies_by_genre(self, category_url):
        print(f'Scraping movies from {category_url}')
        self.driver.get(category_url)

        time.sleep(self.buffer_time)

        self.__preload()

        movie_details = self.driver.find_elements(By.CLASS_NAME, self.config['classNames']['entry'])
        movie_list = []

        for movie in movie_details:
            title = movie.find_element(By.CLASS_NAME, self.config['classNames']['title']).text
            result_movie=Movie()
            result_movie.title = title

            try:
                year = movie.find_element(By.CLASS_NAME, self.config['classNames']['year']).text
                result_movie.year = year
            except:
                print(f'Could not get year for {title}.')
            try: 
                duration = movie.find_element(By.CLASS_NAME, self.config['classNames']['duration']).text
                result_movie.duration = duration
            except:
                print(f'Could not get duration for {title}.')

            try:
                rating = movie.find_element(By.CLASS_NAME, self.config['classNames']['rating']).text
                result_movie.rating = rating
            except:
                print(f'Could not get rating for {title}.')

            movie_list.append(result_movie)

        return movie_list
            