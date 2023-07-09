from bs4 import BeautifulSoup
from googlesearch import search
import requests

class PlaceFinder:
    def __init__(self, city):
        self.city = city
        self.url = ''
        self.place_tags = []

    def find_places(self):
        query = f"places near {self.city}"
        search_result = search(query, tld="com", num=10, stop=30, pause=10)

        for url in search_result:
            if 'holidify' in url:
                self.url = url
                break

        html_text = requests.get(self.url)
        html_content = html_text.content
        soup = BeautifulSoup(html_content, 'html.parser')
        self.place_tags = soup.find_all('h3', class_='card-heading')

    def return_places(self):
        array = []
        for place_tag in self.place_tags:
            place_name = place_tag.text.strip()
            array.append(place_name)
        return array