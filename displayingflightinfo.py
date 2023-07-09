from bs4 import BeautifulSoup
from googlesearch import search
import requests
import tkinter as tk

class FlightScraper:
    def __init__(self, source, destination, start_date, end_date):
        self.source = source
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date
        self.url = self.get_url()

    def get_url(self):
        query = f"Flights from {self.source} to {self.destination}"
        search_result = search(query, tld="com", num=10, stop=10, pause=2)
        for url in search_result:
            if 'ixigo' in url:
                return url

    def get_html_content(self):
        html_text = requests.get(self.url)
        html_content = html_text.content
        return html_content

    def get_soup(self):
        html_content = self.get_html_content()
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup

    def get_flight_info(self):
        soup = self.get_soup()
        flights = soup.find_all('div', class_='u-uppercase u-text-ellipsis flight-name-color')
        flight_price = soup.find_all('span', class_='discounted-price')
        departure_time = soup.find_all('div', class_='time u-ib')
        arrival_time = soup.find_all('div', class_='time u-ib')

        flight_info = []
        for i in range(len(flights)):
            info = {
                'Flight Name': flights[i].text,
                'Price': flight_price[i].text,
                'Departure': departure_time[2 * i].text,
                'Arrival': arrival_time[(2 * i) + 1].text
            }
            flight_info.append(info)

        return flight_info


def display_flight_info(source, destination):
    flight_info = FlightScraper(source, destination, " ", " ")
    info = flight_info.get_flight_info()

    root = tk.Tk()
    root.title("Flight Information")

    row_count = (len(info) + 2) // 3  # Calculate the number of rows needed

    for i, flight in enumerate(info):
        row = i // 3  # Calculate the row index for the flight info block
        col = i % 3   # Calculate the column index for the flight info block

        frame = tk.Frame(root, borderwidth=2, relief="solid")
        frame.grid(row=row, column=col, padx=10, pady=10)

        flight_name_label = tk.Label(frame, text=f"Flight Name: {flight['Flight Name']}")
        flight_name_label.pack()

        price_label = tk.Label(frame, text=f"Price: {flight['Price']}")
        price_label.pack()

        departure_label = tk.Label(frame, text=f"Departure: {flight['Departure']}")
        departure_label.pack()

        arrival_label = tk.Label(frame, text=f"Arrival: {flight['Arrival']}")
        arrival_label.pack()

    root.mainloop()

def get_min(srra):
    min_p = min(srra, key=lambda x: int(x['Price']))['Price']
    return min_p

def get_max(srra):
    max_p = max(srra, key=lambda x: int(x['Price']))['Price']
    return max_p

