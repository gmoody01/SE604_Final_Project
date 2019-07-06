# Libraries for Numpy, Pandas, Requests, JSON, and matplotlib.pyplot are imported to help with data configuration,
# requesting URL commands with JSON files, and plotting acquired JSON data.

import matplotlib.pyplot as plt
import numpy as np
import csv

# This opens and allows for appending capabilities in the external csv file titled: NYC_Water.csv;
# and this function is renamed NYC_water_file with the application.

NYC_water_file = open("NYC_Water.csv", "a")

# Testing the ability of appending future data to existing CSV file based on potential future water 
# usage entries in the CSV file. WARNING: PLEASE QUE OUT FOLLOWING THREE LINES TO PREVENT ENTRY OF 
# TESTING DATA BY MISTAKE BEFORE RUNNING APPLICATION.

NYC_water_file.write("\n2019,8239493,910,105")
NYC_water_file.write("\n2020,8230000,900,99")

NYC_water_file.close()

# Loads up the text in the csv file into the program through the use of the Numpy Module or Libraries

data = np.loadtxt("NYC_Water.csv", unpack = True, delimiter = ",")

# Defines that multiple plots will be made simultaneously, but seperately as different yet unique plots over the 
# parameter of time with specified characteristics or attributes being graphically analyzed individually.

ax = plt.subplot()

# Line of code for constructing the subplot representative of the growth of the New York City population over time 
# which is in years spanning from 1979 to 2018. This is where the title of the collection of subplots is implemented.

plt.subplot(311)
plt.plot(data[0], data[1], "r") # --- plt.plot( x-axis data, y-axis data, symbol)
ax.set_xlabel(" Time (Years)")
plt.title("NYC Urban Water Usage Attributes (1979 to 2018)")
plt.ylabel("NYC Population")
#plt.axis(1979, 2018, 7000000, 8500000)

# Line of code for constructing the subplot representative of the usage or consumption of water in millions of gallons
# per day (MGD) over time (years).

plt.subplot(312)
plt.plot(data[0], data[2], "g") # --- plt.plot( x-axis data, y-axis data, symbol)
ax.set_xlabel("Time (Years)")
plt.ylabel("NYC Consumption (MGD)")
#plt.axis(1979, 2018, 900, 1512)

# Line of code for constructing the subplot representative of the consumption of water per person per day based on
# gallons per day (GPD) over some period of time (years).

plt.subplot(313)
plt.plot(data[0], data[3], "b") # --- plt.plot( x-axis data, y-axis data, symbol)
ax.set_xlabel("Time (Years)")
plt.ylabel("Per Capita (GPD)")
#plt.axis(1979, 2018, 100, 213)  

plt.show()
