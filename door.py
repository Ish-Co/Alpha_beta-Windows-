import tkinter as tk

# Creating an instance of the class
root = tk.Tk()

door = tk.Canvas(root , width=1000 , height=800 , bg='white')
door.pack()

factor = 20
x = 50
y = 50 - 1.65
# door.create_line(x,y,x,y-(1.65*factor),x-(0.65*factor),y-(1.65*factor),x-(0.65*factor),y+(0.37*factor))
# door.create_line(x,y,x,y-(1.65*factor),x-(0.65*factor),y-(1.65*factor),x-(0.37*factor),y+(0.65*factor),x+(0.37*factor),y+(0.65*factor))
# door.create_line(x,y-(1.65*factor),x-(0.65*factor),y-(1.65*factor))
x = 50
y = 50
# door.create_rectangle(x,y,x+(4.75* factor),y+(0.65* factor))
# door.create_line(x+(4.75* factor),y,x+(4.75* factor),y-(1.65*factor), x+(0.65*factor),y-(1.65*factor))
# door.create_rectangle(x,y+(0.65*factor),x+(1.5* factor),y+(30.65* factor))


# NORTH/SOUTH TRIM
def ns_trim(x , y , door_width, wall_width, c):
    door.create_line(x , y , x - (0.66 * c) , y , x - (0.37 * c) , y + (2.30 * c) , x , y + (2.30 * c) , x , y)
    x += (wall_width * c)
    door.create_line(x , y , x + (0.66 * c) , y , x + (0.37 * c) , y + (2.30 * c) , x , y + (2.30 * c) , x , y)
    x -= (wall_width * c)
    y = ((door_width+4.6) * c)
    door.create_line(x , y , x - (0.66 * c) , y , x - (0.37 * c) , y - (2.30 * c) , x , y - (2.30 * c) , x , y)
    x += (wall_width * c)
    door.create_line(x , y , x + (0.66 * c) , y , x + (0.37 * c) , y - (2.30 * c) , x , y - (2.30 * c) , x , y)

def ew_trim(x , y , door_width, wall_width, c):
    door.create_line(x , y , x , y - (0.66 * c) , x - (2.30 * c) , y - (0.37 * c) , x - (2.30 * c) , y , x , y)
    y += (wall_width * c)
    door.create_line(x , y , x , y + (0.66 * c) , x - (2.30 * c) , y + (0.37 * c) , x - (2.30 * c) , y , x , y)
    y -= (wall_width * c)
    x -= ((door_width+4.6) * c)
    door.create_line(x , y , x , y - (0.66 * c) , x + (2.30 * c) , y - (0.37 * c) , x + (2.30 * c) , y , x , y)
    y += (wall_width * c)
    door.create_line(x , y , x , y + (0.66 * c) ,x + (2.30 * c) , y + (0.37 * c), x + (2.30 * c) , y ,x,y)

def vert_door(x,y,w,l,c):
    door.create_rectangle(x,y,x+(w* c),y+(l* c))
    door.create_line(x , y , x , y - (l * c))


def horz_door(x,y,w,l,c):
    door.create_rectangle(x , y , x - (l * c) , y + (w * c))
    door.create_line(x , y , x , y - (l * c))
    door.create_arc(x-(l*c),y-(l*c),x+(l*c),y+(l*c),start=90, extent = 90)

def vert_frame(x,y,c):
    door.create_rectangle(x , y , x + (4.75*c) , y + (0.65 * c))

def horz_frame(x , y , door_width, c):
    door.create_rectangle(x , y , x - (0.65 * c) , y + (4.75 * c))
    x-=(door_width+0.65)*c
    door.create_rectangle(x , y , x - (0.65 * c) , y + (4.75 * c))


def create_doorframe(x,y, door_width = 30 , door_offset = 1.5 , frame_width = 4.75, opens = 'rt', facing='north'):


create_doorframe(30,40)
ew_trim(500 , 400 , 30,4.75,12)
horz_door(500-(2.3*12),400,1.5,30,12)
horz_frame(500-(1.65*12),400,30,12)


#ns_trim(500 , 200 , 30,4.75,12)



root.mainloop()
import tkinter as tk

# Creating an instance of the class
root = tk.Tk()

door = tk.Canvas(root , width=1000 , height=800 , bg='white')
door.pack()

factor = 20
x = 50
y = 50 - 1.65
# door.create_line(x,y,x,y-(1.65*factor),x-(0.65*factor),y-(1.65*factor),x-(0.65*factor),y+(0.37*factor))
# door.create_line(x,y,x,y-(1.65*factor),x-(0.65*factor),y-(1.65*factor),x-(0.37*factor),y+(0.65*factor),x+(0.37*factor),y+(0.65*factor))
# door.create_line(x,y-(1.65*factor),x-(0.65*factor),y-(1.65*factor))
x = 50
y = 50
# door.create_rectangle(x,y,x+(4.75* factor),y+(0.65* factor))
# door.create_line(x+(4.75* factor),y,x+(4.75* factor),y-(1.65*factor), x+(0.65*factor),y-(1.65*factor))
# door.create_rectangle(x,y+(0.65*factor),x+(1.5* factor),y+(30.65* factor))


# NORTH/SOUTH TRIM
def ns_trim(x , y , door_width, wall_width, c):
    door.create_line(x , y , x - (0.66 * c) , y , x - (0.37 * c) , y + (2.30 * c) , x , y + (2.30 * c) , x , y)
    x += (wall_width * c)
    door.create_line(x , y , x + (0.66 * c) , y , x + (0.37 * c) , y + (2.30 * c) , x , y + (2.30 * c) , x , y)
    x -= (wall_width * c)
    y = ((door_width+4.6) * c)
    door.create_line(x , y , x - (0.66 * c) , y , x - (0.37 * c) , y - (2.30 * c) , x , y - (2.30 * c) , x , y)
    x += (wall_width * c)
    door.create_line(x , y , x + (0.66 * c) , y , x + (0.37 * c) , y - (2.30 * c) , x , y - (2.30 * c) , x , y)

def ew_trim(x , y , door_width, wall_width, c):
    door.create_line(x , y , x , y - (0.66 * c) , x - (2.30 * c) , y - (0.37 * c) , x - (2.30 * c) , y , x , y)
    y += (wall_width * c)
    door.create_line(x , y , x , y + (0.66 * c) , x - (2.30 * c) , y + (0.37 * c) , x - (2.30 * c) , y , x , y)
    y -= (wall_width * c)
    x -= ((door_width+4.6) * c)
    door.create_line(x , y , x , y - (0.66 * c) , x + (2.30 * c) , y - (0.37 * c) , x + (2.30 * c) , y , x , y)
    y += (wall_width * c)
    door.create_line(x , y , x , y + (0.66 * c) ,x + (2.30 * c) , y + (0.37 * c), x + (2.30 * c) , y ,x,y)

def vert_door(x,y,w,l,c):
    door.create_rectangle(x,y,x+(w* c),y+(l* c))
    door.create_line(x , y , x , y - (l * c))


def horz_door(x,y,w,l,c):
    door.create_rectangle(x , y , x - (l * c) , y + (w * c))
    door.create_line(x , y , x , y - (l * c))
    door.create_arc(x-(l*c),y-(l*c),x+(l*c),y+(l*c),start=90, extent = 90)

def vert_frame(x,y,c):
    door.create_rectangle(x , y , x + (4.75*c) , y + (0.65 * c))

def horz_frame(x , y , door_width, c):
    door.create_rectangle(x , y , x - (0.65 * c) , y + (4.75 * c))
    x-=(door_width+0.65)*c
    door.create_rectangle(x , y , x - (0.65 * c) , y + (4.75 * c))


def create_doorframe(x,y, door_width = 30 , door_offset = 1.5 , frame_width = 4.75, opens = 'rt', facing='north'):


create_doorframe(30,40)
ew_trim(500 , 400 , 30,4.75,12)
horz_door(500-(2.3*12),400,1.5,30,12)
horz_frame(500-(1.65*12),400,30,12)


#ns_trim(500 , 200 , 30,4.75,12)



root.mainloop()
