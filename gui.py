import tkinter as tk
import draw


#Creating an instance of the class
root = tk.Tk()

#Setting the title of the window
root.title("Alpha Beta")

#Collecting the screen resolution through tkinter and assign it to Vars
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

#MAKE THE APP FULLSCREEN AT ALL TIMES
root.attributes('-fullscreen', True)


x_plan = 481.250
y_plan = 354.750
c = 3


### Living Room ###
plan = tk.Canvas(root, width=x_plan*c , height=y_plan*c , bg='black')
plan.place(x = 20, y = 0)

x = 0
y = 0
### Master Room
x0,y0 = draw.create_wall (plan , x , y , c , 54.125, width=6.125, orientation='vert')
x1,y1 = draw.create_window(plan, x, y0, c, direction='w')
x2,y2 = draw.create_wall (plan , x , y1 , c , 55.125, width=6.125, orientation='vert')

x3,y3 = draw.create_wall (plan , x0 , y , c , 185.625, orientation='horz')
y2-=(4.125*c)
x4,y4 = draw.create_wall (plan , x2 , y2 , c , 174.750, orientation='horz')

x5,y5 = draw.create_wall (plan , x4 , y , c , 129.027, orientation='vert')
draw.create_doorframe(plan, x4,y5,c,opens= 'lt', facing = 'w')
y6= y5+(31.3*c)
x7,y7 = draw.create_wall (plan , x4 , y6 , c , 7.425, orientation='vert')

draw.light_off(plan, 50,50,200)




#Keeping the app running forever
root.mainloop()

