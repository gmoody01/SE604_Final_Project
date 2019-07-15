# The SMART CITY WATER TRACKER APP consist of the following imported libraries:

import tkinter as tk
import requests
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import json
import pandas as pd

Height = 633
Width = 1000

#def format_response(water_data):
#    return canvas.draw()

# This definintion or function provides the necessary functionality of grabbing, formatting, and 
# plotting the data from a specific URL or API (JSON format) which comes from: https://data.cityofnewyork.us/resource/ia2d-e54m.json  

def get_smart_data(entry):
        #App_Token = "X7s1Ap2byxER5jz4707iROiuC"
        #url = "https://data.cityofnewyork.us/resource/ia2d-e54m.json"
        #params = {"APPID": App_Token, "where": year }
        #response = requests.get(url, params=params)
        data = pd.read_json("https://data.cityofnewyork.us/resource/ia2d-e54m.json")
        #print(data)

        f = Figure(figsize=(15,2), dpi=80, tight_layout=True)
        ax = plt.subplot()

# Line of code for constructing the subplot representative of the growth of the New York City population over time 
# which is in years spanning from 1979 to 2018. This is where the title of the collection of subplots is implemented.
# NOTE: df1a = x-axis data for subplot 1, df1b = y-axis data for subplot 1

        a = f.add_subplot(311)
        df1a = data.loc[0:39, ['year' ]]
        df1b = data.loc[0:39, ['new_york_city_population']]
        plt.subplot(311)
        a.plot(df1a, df1b, "r") # FORMATTING --- plt.plot( x-axis data, y-axis data, symbol)
        #a.set_xlabel(" Time (Years)")
        #a.set_title("NYC Urban Water Usage Attributes (1979 to 2018)")
        a.set_ylabel("NYC Pop.") # --- NYC Population

# Line of code for constructing the subplot representative of the usage or consumption of water in millions of gallons
# per day (MGD) over time (years).
# NOTE: df2a =  x-axis data for subplot 2, df2b = y-axis data for subplot 2

        b =f.add_subplot(312)
        df2a = data.loc[0:39, ['year']]
        df2b = data.loc[0:39, ['nyc_consumption_million_gallons_per_day']]
        plt.subplot(312)
        b.plot(df2a, df2b, "g") # FORMATTING --- plt.plot( x-axis data, y-axis data, symbol)
        #b.set_xlabel("Time (Years)")
        b.set_ylabel("NYC Consump. (MGD)") # -- NYC Consumption (MGD)
        #plt.axis(1979, 2018, 900, 1512)

# Line of code for constructing the subplot representative of the consumption of water per person per day based on
# gallons per day (GPD) over some period of time (years).
#NOTE: df3a =  x-axis data for subplot 3, df3b = y-axis data for subplot 3

        c =f.add_subplot(313)
        df3a = data.loc[0:39, ['year']]
        df3b = data.loc[0:39, ['per_capita_gallons_per_person_per_day']]
        plt.subplot(313)
        c.plot(df3a, df3b, "b") # FORMATTING --- plt.plot( x-axis data, y-axis data, symbol)
        c.set_xlabel("Time (Years)")
        c.set_ylabel("Per Capita (GPD)") # -- NYC Consumption of Gallons Capita Per Day (GPD)
        #plt.axis(1979, 2018, 100, 213)
    
# Line of code necessary to construct the matplotlib plots as figure on the tkinter canvas, more specifically on the
# lower_frame where the data for the application is expected to be located or displayed with execution of the application.
    
        canvas = FigureCanvasTkAgg(f, master=lower_frame)
        canvas.get_tk_widget().place(relx =0.5, rely=1, relwidth=1, relheight=1, anchor="s")
        canvas.draw()
        
# Hopefully an addition to come in the next version -- V2

        #decline = "Their was an Issue finding and plotting the applied Smart City Data"
        #print(decline)


# The Smart City Water Tracker Application GUI is constructed here within the root object.  

root = tk.Tk()

canvas = tk.Canvas(root, height=Height, width=Width)
canvas.pack()

# Background image of the GUI application is placed here to offer asethetic appeal to the user of the application.

#background_image = tk.PhotoImage(file="//home//pi//Documents//Smart_City_Data_Program//Smart_Cities_Image_2")

# This photo image location can be a flash drive location
# Be sure in the file argument to put double slashes for tkinter module to read directory location of where image is.
# This location can be found by right clicking the image in your file explorer and clicking Properties for file info.

background_image = tk.PhotoImage(file="D:\\Smart_Cities_Image_2")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# This is the object of the GUI responsible for folding the button for searching the API and the entry field which
# accepts the user's get file (water_data) commands.

frame = tk.Frame(root, bg="#00ccff", bd=6)
frame.place(relx=0.5, rely=0.05, relwidth=0.8, relheight=0.09, anchor='n')

button = tk.Button(frame, text="Get Smart City Data", bg="gray", fg="black", bd=2, font=12, command=
                   lambda:get_smart_data(entry.get()))
button.place(relx=0.65, rely=0.05, relwidth=0.35, relheight=0.90)

#button1 = tk.Button(frame, text="Input Y-Axis Subplot Data", bg="gray", fg="black", bd=4)
#button1.place(relx=0.7, rely=0.1, relwidth= 0.3, relheight=0.9)

entry = tk.Entry(frame, justify="left", font=40)
entry.place(relx=0.0, rely=0.05, relwidth=0.63, relheight=0.9)

# The lower frame displays user input as graphical data (output) as desired by the user of the application.

lower_frame = tk.Frame(root, bg="#00ccff", bd=8)
lower_frame.place(relx =0.5, rely=0.90, relwidth=0.8, relheight=0.65, anchor="s")

label = tk.Label(lower_frame)
label.place(relx =0.5, rely=1, relwidth=1, relheight=1, anchor="s")

# This is the application's given name or title

label1 = tk.Label(root, text="SMART CITY WATER TRACKER", bg="#00ccff", font=20)
label1.place(relx=0.5, rely=0.02, relwidth=0.8, relheight=0.04, anchor='n')

root.mainloop()
