# UPDATED as of 14 July 2019 by JW
# Program now displays a graph in the GUI

# create a GUI to prompt user to provide a file location for a local file or an external file

import tkinter as tk
import csv
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# dictSE604Project = {
#     getfile_local : pulling a digitally local data file
#     int_data_file : internal data file within the local pc
# }
# Added a dictionary to hopefully explain variable names we integrate

HEIGHT = 800
WIDTH = 1000

# def getfile_local:
#    label = GRAPH DISPLAYS HERE or provide error msg
# def getfile_external:
#    label = GRAPH DISPLAYS HERE or provide error msg

# This is copied from Dr. Cloutier's weather app to format how the output will display in the GUI
#def format_response(init_data_file):
#    f = Figure(figsize=(5,4), dpi=100)
#    a = f.add_subplot(111)
#    a.plot(Date,Average)
#        
#    dataPlot = FigureCanvasTkAgg(f, master=master)
#    dataPlot.show()
#        plt.scatter(date, average)
#        plt.title('DJIA Scatter Graph')
#        plt.xlabel('Date')
#        plt.ylabel('Average')
#        plt.show()
#    except:
#        final_str = 'There was a problem retrieving that information'
#    return final_str

# This is the function to manipulate an internal pc data file (.csv). # open the file in universal line ending mode 
def getfile_local(init_data_file):
    with open(init_data_file, 'r') as infile:
# read the file as a dictionary for each row ({header : value})
        reader = csv.DictReader(infile)
        data = {}
        for row in reader:
          for header, value in row.items():
            try:
              data[header].append(value)
            except KeyError:
              data[header] = [value]
# Extract and print the data to verify
        date = data['Date']
        print(date)
        average = data['Average']
        print(average)
# Plot the data
        f = Figure(figsize=(6,6), dpi=100)
        a = f.add_subplot(111)
        a.plot(date,average)
        canvas = FigureCanvasTkAgg(f, master=lowest_frame)
        canvas.get_tk_widget().pack(side=tk.TOP)
        canvas.draw()
       
# Creates the GUI######################################################################################################
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# Adds a background image##############################################################################################
background_image = tk.PhotoImage(file='graph.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Creates the border, text entry block and button to activate the inputs for the local file ###########################
frame = tk.Frame(root, bg='black', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.075, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Graph Local File", font=40, command=lambda: getfile_local(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

# Creates the border, text entry block and button to activate the inputs for the external file ########################
# lower_frame = tk.Frame(root, bg='black', bd=5)
# lower_frame.place(relx=0.5, rely=0.2, relwidth=0.8, relheight=0.075, anchor='n')
#
# lower_entry = tk.Entry(lower_frame, font=40)
# lower_entry.place(relwidth=0.65, relheight=1)
#
# lower_button = tk.Button(lower_frame, text="Graph External File", font=40)
# add command or function within parenthesis above, code TBD. possibly as follows: command=lambda: getfile_enternal(entry.get())
# lower_button.place(relx=0.7, relheight=1, relwidth=0.3)

# Creates the border and "canvas" where the outputs will show #########################################################
lowest_frame = tk.Frame(root, bg='black', bd=5)
lowest_frame.place(relx=0.5, rely=0.3, relwidth=0.8, relheight=0.6, anchor='n')

label = tk.Label(lowest_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()
