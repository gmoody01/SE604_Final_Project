# create a GUI to prompt user to provide a file location for a local file or an external file

import tkinter as tk
# import requests
import csv
# import math

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
def format_response(data_list):
    try:
        final_str = str(data_list)
    except:
        final_str = 'There was a problem retrieving that information'
    return final_str

# This is the function to manipulate an internal pc data file (.csv). For this example I just wanted the csv data
# to print in the window
def getfile_local(init_data_file):
    with open(init_data_file, 'r') as data_file:

#craig's code
#        data_reader = csv.reader(data_file)
#        for line in data_reader:
#            data_list = line
#            print(data_list)
#            label['text'] = format_response(data_list)

#Dr. Cloutier's code
# creating a csv reader object 
        csvreader = csv.reader(data_file)

# initializing the titles and rows list 
        fields = [] 
        rows = [] 
  
# extracting field names through first row 
        fields = csvreader
    
# extracting each data row one by one 
        for row in csvreader: 
            rows.append(row) 

## get total number of rows 
#            print("Total no. of rows: %d"%(csvreader.line_num)) 
#  
### printing the field names 
##            print('Field names are:' + ', '.join(field for field in fields)) 
#  
##  printing first 5 rows 
#            print('\nFirst 5 rows are:\n') 
#            for row in rows[:1]: 
#    # parsing each column of a row 
#                for col in row: 
#                    print(row)
                    
        label['text'] = format_response(rows)

# This was a different version of the function to manipulate data
# def getfile_local():
#     with open('DJIA.csv') as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         line_count = 0
#         for row in csv_reader:
#             if line_count == 0:
#                 label['text'] = format_response(data_list)
#                 line_count += 1
#             else:
#                 print('done')
#                 line_count += 1

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