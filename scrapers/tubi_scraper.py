import json
import time

from models.content import Content

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
        self.driver_options.add_argument("--log-level=3")

        if headless is True:
            self.driver_options.add_argument("--headless")

        return self.driver_options

    def __preload(self):
        page_height = int(self.driver.execute_script('return document.body.scrollHeight'))

        for i in range(0, page_height * self.scroll_buffer, self.scroll_speed):
            self.driver.execute_script("window.scrollTo(0, {});".format(i))

    def get_content_by_genre(self, category_url):
        print(f'Scraping movies/shows from {category_url}')
        self.driver.get(category_url)

        time.sleep(self.buffer_time)

        self.__preload()

        content_details = self.driver.find_elements(By.CLASS_NAME, self.config['classNames']['entry'])
        content_list = []

        for content in content_details:
            try:
                title = content.find_element(By.CLASS_NAME, self.config['classNames']['title']).text
                result_content = Content()
                result_content.title = title

                try:
                    year = content.find_element(By.CLASS_NAME, self.config['classNames']['year']).text
                    result_content.year = year
                except:
                    print(f'Could not get year for {title}.')
                try: 
                    duration = content.find_element(By.CLASS_NAME, self.config['classNames']['duration']).text
                    result_content.duration = duration
                    result_content.category = "Movie"
                except:
                    result_content.category = "Show"
                    result_content.duration = "N/A"

                try:
                    rating = content.find_element(By.CLASS_NAME, self.config['classNames']['rating']).text
                    result_content.rating = rating
                except:
                    print(f'Could not get rating for {title}.')

                content_list.append(result_content)

            except:
                print('There was an error writing an entry...')

        return content_list
            