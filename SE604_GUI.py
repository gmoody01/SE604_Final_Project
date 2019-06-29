#create a GUI to prompt user to provide a file location for a local file or an external file

import tkinter as tk
import requests

HEIGHT = 800
WIDTH = 1000

#def getfile_local:
    
#    label = GRAPH DISPLAYS HERE or provide error msg

#def getfile_external:
    
#    label = GRAPH DISPLAYS HERE or provide error msg

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='graph.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='black', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.075, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Graph Local File", font=40)
#add command or function within parenthesis above, code TBD. possibly as follows: command=lambda: getfile_local(entry.get())
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='black', bd=5)
lower_frame.place(relx=0.5, rely=0.2, relwidth=0.8, relheight=0.075, anchor='n')

lower_entry = tk.Entry(lower_frame, font=40)
lower_entry.place(relwidth=0.65, relheight=1)

lower_button = tk.Button(lower_frame, text="Graph External File", font=40)
#add command or function within parenthesis above, code TBD. possibly as follows: command=lambda: getfile_enternal(entry.get())
lower_button.place(relx=0.7, relheight=1, relwidth=0.3)

lowest_frame = tk.Frame(root, bg='black', bd=5)
lowest_frame.place(relx=0.5, rely=0.3, relwidth=0.8, relheight=0.6, anchor='n')

label = tk.Label(lowest_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()