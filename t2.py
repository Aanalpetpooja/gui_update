
#!/usr/bin/python3

# Import the required libraries
import sys
import os
#import Tkinter
#import tkMessageBox

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import subprocess
#import git

#top=Tkinter.Tk()
# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("700x350")

def show_msg():
   messagebox.showinfo("Message","updating")


def helloCallBack():
    os.system('/home/robot4/Desktop/test/dist/test12')

# Add a Label
Label(win, text="Select a Day",font=('Aerial 13')).pack(pady=10)

# Create a Variable to store the selection
var = StringVar()

# Create an OptionMenu Widget and add choices to it
option = OptionMenu(win, var, "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
option.config(bg="gray81", fg="white")
option['menu'].config(bg="green3")
option.pack(padx=20, pady=30)

ttk.Button(win, text= "update", command=helloCallBack).pack(pady= 20)#command=show_msg, 
#b.pack()

win.mainloop()
