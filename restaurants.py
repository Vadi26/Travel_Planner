from bs4 import BeautifulSoup
from googlesearch import search
import requests
import tkinter as tk

def get_restaurants(city):
    query = f"best restaurants in {city}"
    search_result = search(query, tld="com", num=10, stop=10, pause=2)
    URL = ''
    for url in search_result:
        if 'dineout' in url:
            URL = url

    html_text = requests.get(URL)
    html_content = html_text.content
    soup = BeautifulSoup(html_content, 'html.parser')
    restaurants = soup.find_all('a', class_='restnt-name ellipsis')
    rating = soup.find_all('div', class_='restnt-rating rating-4')
    restaurants_array = []
    for i in range(len(rating)):
        info = {
            'Restaurant': restaurants[i].text,
            'Rating':rating[i].text,
        }
        restaurants_array.append(info)
    return restaurants_array