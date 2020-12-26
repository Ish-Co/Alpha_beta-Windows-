import tkinter as tk
import config_tastbar            #This import method will compile the "config" before executing the line below.
import config_cursor_pos as cursor
import datetime
import turtle

#Hide taskbar before starting the GUI
config_tastbar.hide_taskbar()

#Creating an instance of the class
root = tk.Tk()

#Collecting the screen resolution through tkinter and assign it to Vars
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

#Setting the title of the window
root.title("Alpha Beta")

#Disable resizing the GUI as (x = false, y = false)
root.resizable(1,1)

#Disable minimize
root.wm_minsize(0,0)


root.configure(bg = "black")

#Setting the resolution of the GUI using the Vars.
root.geometry('%dx%d+0+0' %(width,height))

#Keeping the app running forever
root.mainloop()

#unhide the taskbar after exiting the GUI
config_tastbar.unhide_taskbar()
