import tkinter as tk
#import config_tastbar            #This import method will compile the "config" before executing the line below.
#import config_cursor_pos as cursor
import datetime
import turtle

#Creating an instance of the class
root = tk.Tk()

#Setting the title of the window
root.title("Alpha Beta")

#Disable resizing the GUI as (x = false, y = false)
#root.resizable(1,1)

#Disable minimize
#root.wm_minsize(0,0)
root.attributes('-fullscreen', True)
root.configure(bg = "white")


### Living Room ###
living_room = tk.Canvas(root, bg = 'black', height = 300, width = 300)
living_room.place(x = 0, y = 100)
ls_button = tk.Button(living_room)
ls_button.place(x = 0, y = 0)
ls_button.configure(font = 'currier 26 bold', background = "green", text = "Light ON")





#Keeping the app running forever
root.mainloop()
