import streamlit as st
from datetime import date, timedelta
from places_scraper import *
from hotels import *
from restaurants import *
from PIL import Image  # Import the Image module from PIL
from displayingflightinfo import *
import csv
from streamlit_lottie import st_lottie

def load_lottie(url):
    r = requests.get(url=url)
    if r.status_code != 200:
        return None
    return r.json()

def main():
    st.write("<h1 style='text-align: center;'>TRAVEL PLANNER</h1>", unsafe_allow_html=True)
    title_style = """
    <style>
    .center-title {
        text-align: center;
    }
    </style>
    """
    st.markdown(title_style, unsafe_allow_html=True)
    st.markdown(
        """
        <style>
        .container {
            border: 1px solid #ccc;
            padding: 10px;
            margin-bottom: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # --- LOAD ASSETS ---
    lottie = load_lottie("https://assets9.lottiefiles.com/packages/lf20_vwcugezu.json")
    with st.container():
        st.write("---")
        st_lottie(lottie, height=500, key="coding")

    cities = []
    with open('worldcities.csv', newline='', encoding='utf8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader)
        for row in reader:
            cities.append(row[1])

    source = st.selectbox("Source", cities)
    dest = st.selectbox("Destination", cities)

    dates = []
    start_date = date.today()
    end_date = date(2023, 12, 31)
    delta = timedelta(days=1)
    while start_date <= end_date:
        dates.append(start_date.strftime("%d-%m-%Y"))
        start_date += delta

    st.subheader("Select Start and End Date")
    start = st.selectbox("Start Date", dates)
    end = st.selectbox("End Date", dates[1:])

    if st.button("NEXT"):
        # Displaying flight INFO
        flight_write = FlightScraper(source, dest, start, end)
        write = flight_write.get_flight_info()
        min_flight = get_min(write)
        max_flight = get_max(write)

        # Extracting Places to visit write
        place_finder = PlaceFinder(dest)
        place_finder.find_places()
        places_to_visit = place_finder.return_places()

        # Extracting Accommodation options
        hotels = get_hotels(dest)

        # Extracting Restaurant options
        restaurants = get_restaurants(dest)

        st.write("<h1 style='text-align: center;'>Flight Details</h1>", unsafe_allow_html=True)

        lottie2 = load_lottie("https://assets6.lottiefiles.com/packages/lf20_5YaHks9vQh.json")
        with st.container():
            st.write("---")
            st_lottie(lottie2, height=500, key="coding2")

        # Display flight information
        with st.container():
            st.write("---")
            left_column, middle_column, right_column = st.columns(3)
            for i, flight in enumerate(write):
                if (i % 3 == 0):
                    with left_column:
                        st.write(f"<p style='font-size: 20px;'>Flight {i+1}", unsafe_allow_html=True)
                        st.write(f"<p style='font-size: 20px;'>Flight Name: {flight['Flight Name']}", unsafe_allow_html=True)
                        st.write(f"<p style='font-size: 20px;'>Price: {flight['Price']}", unsafe_allow_html=True)
                        st.write(f"<p style='font-size: 20px;'>Departure: {flight['Departure']}", unsafe_allow_html=True)
                        st.write(f"<p style='font-size: 20px;'>Arrival: {flight['Arrival']}", unsafe_allow_html=True)
                        st.write("---")
                elif (i % 3 == 1):
                    with middle_column:
                        st.write(f"<p style='font-size: 20px;'>Flight {i+1}", unsafe_allow_html=True)
                        st.write(f"<p style='font-size: 20px;'>Flight Name: {flight['Flight Name']}", unsafe_allow_html=True)
                        st.write(f"<p style='font-size: 20px;'>Price: {flight['Price']}", unsafe_allow_html=True)
                        st.write(f"<p style='font-size: 20px;'>Departure: {flight['Departure']}", unsafe_allow_html=True)
                        st.write(f"<p style='font-size: 20px;'>Arrival: {flight['Arrival']}", unsafe_allow_html=True)
                        st.write("---")
                else:
                    with right_column:
                        st.write(f"<p style='font-size: 20px;'>Flight {i+1}", unsafe_allow_html=True)
                        st.write(f"<p style='font-size: 20px;'>Flight Name: {flight['Flight Name']}", unsafe_allow_html=True)
                        st.write(f"<p style='font-size: 20px;'>Price: {flight['Price']}", unsafe_allow_html=True)
                        st.write(f"<p style='font-size: 20px;'>Departure: {flight['Departure']}", unsafe_allow_html=True)
                        st.write(f"<p style='font-size: 20px;'>Arrival: {flight['Arrival']}", unsafe_allow_html=True)
                        st.write("---")
            st.write(f"<p style='font-size: 20px;'>Budget : {min_flight} - {max_flight}", unsafe_allow_html=True)
        # Display places to visit
        st.write("<h1 style='text-align: center;'>Tourist Attractions</h1>", unsafe_allow_html=True)

        lottie3 = load_lottie("https://assets4.lottiefiles.com/packages/lf20_r4s12cqb.json")
        with st.container():
            st.write("---")
            st_lottie(lottie3, height=500, key="coding3")

        with st.container():
            st.write("---")
            left_column, right_column = st.columns(2)
            i = 0
            for place in places_to_visit:
                if i % 2 == 0:
                    with left_column:
                        st.write(f"<p style='font-size: 20px;'>{place}", unsafe_allow_html=True)
                if i % 2 == 1:
                    with right_column:
                        st.write(f"<p style='font-size: 20px;'>{place}", unsafe_allow_html=True)
                i = i + 1

        # Display accommodation options
        st.write("<h1 style='text-align: center;'>Accomodation</h1>", unsafe_allow_html=True)
        lottie4 = load_lottie("https://assets5.lottiefiles.com/packages/lf20_26KVdO.json")
        with st.container():
            st.write("---")
            st_lottie(lottie4, height=500, key="coding4")
        with st.container():
            st.write("---")
            left_column, right_column = st.columns(2)
            i = 0
            for hotel in hotels:
                st.write(f"<p style='font-size: 20px;'>{hotel['Hotel']}\nPrice: {hotel['Price']}", unsafe_allow_html=True)
                # else :
                #     with right_column:
                #         st.write(f"{hotel['Hotel']}\nPrice: {hotel['Price']}")
            st.write("---")

        # Displaying Restaurants
        st.write("<h1 style='text-align: center;'>Restaurants</h1>", unsafe_allow_html=True)
        lottie5 = load_lottie("https://assets1.lottiefiles.com/packages/lf20_GUQObWT5Mw.json")
        with st.container():
            st.write("---")
            st_lottie(lottie5, height=500, key="coding5")
        with st.container():
            st.write("---")
            l1, l2, r1, r2 = st.columns(4)
            for i, restaurant in enumerate(restaurants):
                if i % 4 == 0:
                    with l1:
                        st.write(f"<p style='font-size: 20px;'>Hotel Name : {restaurant['Restaurant']}", unsafe_allow_html=True)
                        st.write(f"<p style='font-size: 20px;'>Rating : {restaurant['Rating']}", unsafe_allow_html=True)
                if i % 4 == 1:
                    with l2:
                        st.write(f"<p style='font-size: 20px;'>Hotel Name : {restaurant['Restaurant']}", unsafe_allow_html=True)
                        st.write(f"<p style='font-size: 20px;'>Rating : {restaurant['Rating']}", unsafe_allow_html=True)
                if i % 4 == 2:
                    with r1:
                        st.write(f"<p style='font-size: 20px;'>Hotel Name : {restaurant['Restaurant']}", unsafe_allow_html=True)
                        st.write(f"<p style='font-size: 20px;'>Rating : {restaurant['Rating']}", unsafe_allow_html=True)
                if i % 4 == 3:
                    with r2:
                        st.write(f"<p style='font-size: 20px;'>Hotel Name : {restaurant['Restaurant']}", unsafe_allow_html=True)
                        st.write(f"<p style='font-size: 20px;'>Rating : {restaurant['Rating']}", unsafe_allow_html=True)

        st.button("Restart")

if __name__ == "__main__":
    main()

