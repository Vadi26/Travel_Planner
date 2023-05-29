import tkinter as tk
from tkinter import *
from datetime import date, timedelta
from tkinter import ttk
import csv

window = tk.Tk()
window.title("Travel Planner")
image = tk.PhotoImage(file="photo.png")
canvas = tk.Canvas(window, width=600, height=650)
canvas.grid(row=0, column=0, columnspan=3)

canvas.create_image(0, 0, anchor="nw", image=image)

cities = []
with open('worldcities.csv', newline='', encoding='utf8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader)
    for row in reader:
        cities.append(row[1]) 

source=StringVar()
source_cb=ttk.Combobox(canvas, values=cities, textvariable=source, font=("Helvetica", 15))
source_cb.insert(0, "Source")
source_cb.configure(width=15,background="white")
source_cb.place(x=100, y=80)

dest=StringVar()
dest_cb=ttk.Combobox(canvas, values=cities, textvariable=dest, font=("Helvetica", 15))
dest_cb.insert(0, "Destination")
dest_cb.configure(width=15)
dest_cb.place(x=350, y=80)


dates = []
start_date = date.today()
end_date = date(2023, 12, 31)
delta = timedelta(days=1)
while start_date <= end_date:
    dates.append(start_date.strftime("%d-%m-%Y"))
    start_date += delta

label = ttk.Label(canvas, text="Start date:", font=("Helvetica", 15),relief="raised", borderwidth="2",background="#ADD8E6")
label.place(x=100, y=200)

start = StringVar()
dropdown = ttk.Combobox(canvas, values=dates, textvariable=start, font=("Helvetica", 15))
dropdown.insert(0, "DD/MM/YYYY")
dropdown.place(x=250, y=200)

label = ttk.Label(canvas, text="End date:", font=("Helvetica", 15),relief="raised", borderwidth="2",background="#ADD8E6")
label.place(x=100, y=250)

end = StringVar()
dropdown = ttk.Combobox(canvas, values=dates[1:], textvariable=end, font=("Helvetica", 15))
dropdown.insert(0, "DD/MM/YYYY")
dropdown.place(x=250, y=250)

def createNewWindow():
    window2 = tk.Tk()
    window2.title("Travel Planner")
    image2 = tk.PhotoImage(file="photo2.png")
    canvas2 = tk.Canvas(window2, width=500, height=650)
    canvas2.grid(row=0, column=0, columnspan=3)
    canvas2.create_image(0, 0, anchor="nw", image=image2)

    travel = Label(window2, text="Travel", fg="white", bg="black", font=("Helvetica", 15))
    travel.place(x=100, y=100)

    l=["a","b", "et"]
    flights= Label(window2, text=l, fg="white", bg="black", font=("Helvetica", 15))
    flights.place(x=200, y=100)

    hotel = Label(window2, text="Hotels", fg="white", bg="black", font=("Helvetica", 15))
    hotel.place(x=100, y=300)
    stay= Label(window2, text=l, fg="white", bg="black", font=("Helvetica", 15))
    stay.place(x=100, y=350)

    places = Label(window2, text="Places to visit", fg="white", bg="black", font=("Helvetica", 15))
    places.place(x=300, y=300)
    visit= Label(window2, text=l, fg="white", bg="black", font=("Helvetica", 15))
    visit.place(x=300, y=350)

    window2.mainloop()

def click():
    s=source.get()
    d=dest.get()
    st=start.get()
    e=end.get()
    print(s,d,st,e)
    window.destroy()
    createNewWindow()

next_button = Button(window, text="NEXT", command=click, font=("Helvetica", 15), bg="green")
next_button.place(x=300, y=350)
window.mainloop()