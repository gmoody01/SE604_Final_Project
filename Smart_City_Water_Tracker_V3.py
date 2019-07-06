# Libraries for Numpy, Pandas, Requests, JSON, and matplotlib.pyplot are imported to help with data configuration,
# requesting URL commands with JSON files, and plotting acquired JSON data.

import matplotlib.pyplot as plt 
import numpy as np
import json
import requests
import pandas as pd

# Application reads specified URL field which is in JSON formatting, therefore Pandas and JSON modules are utilized
# open and read the URL as a JSON file allowing for the collection of necessary data for plotting purposes later.

data = pd.read_json("https://data.cityofnewyork.us/resource/ia2d-e54m.json")

# Defines that multiple plots will be made simultaneously, but seperately as different yet unique plots over the 
# parameter of time with specified characteristics or attributes being graphically analyzed individually.

ax = plt.subplot()

# Line of code for constructing the subplot representative of the growth of the New York City population over time 
# which is in years spanning from 1979 to 2018. This is where the title of the collection of subplots is implemented.
# NOTE: df1a = x-axis data for subplot 1, df1b = y-axis data for subplot 1

df1a = data.loc[0:39, ['year' ]]
df1b = data.loc[0:39, ['new_york_city_population']]
plt.subplot(311)
plt.plot(df1a, df1b, "r") # FORMATTING --- plt.plot( x-axis data, y-axis data, symbol)
ax.set_xlabel(" Time (Years)")
plt.title("NYC Urban Water Usage Attributes (1979 to 2018)")
plt.ylabel("NYC Population")
#plt.axis(1979, 2018, 7000000, 8500000)

# Line of code for constructing the subplot representative of the usage or consumption of water in millions of gallons
# per day (MGD) over time (years).
# NOTE: df2a =  x-axis data for subplot 2, df2b = y-axis data for subplot 2

df2a = data.loc[0:39, ['year']]
df2b = data.loc[0:39, ['nyc_consumption_million_gallons_per_day']]
plt.subplot(312)
plt.plot(df2a, df2b, "g") # FORMATTING --- plt.plot( x-axis data, y-axis data, symbol)
ax.set_xlabel("Time (Years)")
plt.ylabel("NYC Consumption (MGD)")
#plt.axis(1979, 2018, 900, 1512)

# Line of code for constructing the subplot representative of the consumption of water per person per day based on
# gallons per day (GPD) over some period of time (years).
#NOTE: df3a =  x-axis data for subplot 3, df3b = y-axis data for subplot 3

df3a = data.loc[0:39, ['year']]
df3b = data.loc[0:39, ['per_capita_gallons_per_person_per_day']]
plt.subplot(313)
plt.plot(df3a, df3b, "b") # FORMATTING --- plt.plot( x-axis data, y-axis data, symbol)
ax.set_xlabel("Time (Years)")
plt.ylabel("Per Capita (GPD)")
#plt.axis(1979, 2018, 100, 213)  

plt.show()
