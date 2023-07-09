from bs4 import BeautifulSoup
from googlesearch import search
import requests
import tkinter as tk

def get_hotels(city):
    query = f"Hotels to stay in or near {city}"
    search_result = search(query, tld="com", num=30, stop=10, pause=2)
    URL = ''
    for url in search_result:
        if 'holidify' in url:
            URL = url
            break

    if URL == 'holidify':
        html_text = requests.get(URL)
        html_content = html_text.content
        soup = BeautifulSoup(html_content, 'html.parser')
        hotels = soup.find_all('h3', class_='card-heading')
        prices = soup.find_all('span', class_='price default')
        hotels_array = []
        for i in range(len(prices)):
            info = {
                'Hotel': hotels[i].text,
                'Price': prices[i].text,
            }
            hotels_array.append(info)
        return hotels_array
    else :
        URL = f'https://www.booking.com/city/in/{city}.html'
        html_text = requests.get(URL)
        html_content = html_text.content
        soup = BeautifulSoup(html_content, 'html.parser')
        hotels = soup.find_all('span', class_='bui-card__title')
        prices = soup.find_all('div', class_='bui-price-display__value bui-f-color-constructive')
        hotels_array = []
        for i in range(len(prices)):
            info = {
                'Hotel': hotels[i].text,
                'Price': prices[i].text,
            }
            hotels_array.append(info)
        print(hotels_array)
        return hotels_array


# hotels = get_h    otels("mumbai")
# print(hotels)     