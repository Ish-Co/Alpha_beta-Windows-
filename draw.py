def create_doorframe(self , x , y , c , door_width=30 , door_offset=1.5 , frame_width=4.75 , opens='rt' , facing='n'):
    # OPTION A , B , C , OR D
    if (facing == 'n') or (facing == 's'):
        y1 = y + (4.75 * c)
        x1 = x + (1.65 * c)
        y2 = y1 + (0.66 * c)
        x2 = x1 - (2.30 * c)
        y3 = y1 + (0.37 * c)
        y4 = y3 - (5.49 * c)
        x3 = x2 + (2.30 * c)
        y5 = y4 - (0.29 * c)
        #       The line below will create the right trim corner        #
        #                              [                                #
        self.create_line (x , y , x , y1 , x1 , y1 , x1 , y2 , x2 , y3 , x2 , y4 , x3 , y5 , x3 , y , x , y)
        x -= (door_width + 1.30) * c
        x1 = x - (1.65 * c)
        x2 = x1 + (2.30 * c)
        x3 = x2 - (2.30 * c)
        #       The line below will create the left trim corner         #
        #                              ]                                #
        self.create_line (x , y , x , y1 , x1 , y1 , x1 , y2 , x2 , y3 , x2 , y4 , x3 , y5 , x3 , y , x , y)
        x += (door_width + 1.30) * c
        x4 = x - (0.65 * c)
        x5 = x4 - (door_width * c)
        #   OPTION A OR B
        if (facing == 'n'):
            y6 = y + (door_offset * c)
            #       Create a line between the two corners          #
            #               ]---------------[                      #
            self.create_line (x4 , y6 , x5 , y6)
            x7 = x4 - (door_width * c)
            x8 = x4 + (door_width * c)
            y7 = y - (door_width * c)
            y8 = y + (door_width * c)
            #   OPTION A
            if (opens == 'rt'):
                #       The line below will create the door arc         #
                self.create_arc (x7 , y7 , x8 , y8 , start=90 , extent=90)
            #   OPTION B
            else:
                x7 -= (door_width * c)
                #       The line below will create the door arc         #
                self.create_arc (x4 , y7 , x7 , y8 , start=0 , extent=90)
        #   OPTION C OR D
        else:
            y6 = y + ((door_offset + 1.75) * c)
            #       Create a line between the two corners          #
            #               ]---------------[                      #
            self.create_line (x4 , y6 , x5 , y6)
            y += (frame_width * c)
            y7 = y - (door_width * c)
            y8 = y + (door_width * c)
            x7 = x4 - (door_width * c)
            #   OPTION C
            if (opens == 'rt'):
                x7 -= (door_width * c)
                #       The line below will create the door arc         #
                self.create_arc (x7 , y7 , x4 , y8 , start=270 , extent=90)
            #   OPTION D
            else:
                #       The line below will create the door arc         #
                self.create_arc (x7 , y7 , x4 , y8 , start=180 , extent=90)
    else:
        print ("function is under constraction!")


def create_window(self , x , y , c , width_a=31 , width_b=28 , offset=2.5 , direction='n'):
    if (direction == 'n') or (direction == 's'):                    # HORIZONTAL WINDOW
        #LEFT FIXED SODE
        self.create_rectangle (x , y + (offset * c) , x + ((width_a * c)) , y + ((offset * c) / 2),outline='blue')
        #RIGHT SLIDING SIDE
        self.create_rectangle (x + (width_a * c) , y , x + ((width_a + width_b) * c) , y + ((offset * c) / 2),outline='blue')
        return x + ((width_a + width_b) * c) , y
    else:                                                           # VERTICAL WINDOW
        #UPPER SLIDING SIDE
        self.create_rectangle (x + ((offset * c) / 2), y , x +(offset * c) , y + ((width_a * c)),outline='blue')
        #LOWER FIXED SIDE
        self.create_rectangle (x , y + ((width_a * c)) , x + ((offset * c) / 2) , y + ((width_b+width_a)*c),outline='blue')
        return x , y + ((width_b+width_a)*c)


def create_wall(self , x , y , c , length , width=4.125 , orientation='horz'):
    if (orientation == 'horz'):
        self.create_rectangle (x , y , x + (length * c) , y + (width * c) , fill='#000fff000' , outline='#000fff000')
        return x + (length * c), y + (width * c)
    else:
        self.create_rectangle (x ,y,  x + (width * c), y + (length * c) , fill='#000fff000' , outline='#000fff000')
        return x + (width * c), y + (length * c)

def light_off(self, x, y, size):
    self.create_rectangle(x,y,x+size,y+size, outline = 'white', width = 2)
    x0 = (size*0.10)
    x1 = (size*0.10)
    self.create_line(x+x0,y+(size*0.25), x+x0+x1, y+(size*0.25), fill = 'white', width = 2 )
    x2 = (size * 0.4)
    self.create_arc (x+x0+x0+x1 , y+(size*0.06) , x+x0+x0+x1+x2 , y+(size*0.45) , outline='white', style = 'chord', start=180 , extent=180, width = 2)
    self.create_line (x+x0+x0+x1+x2 + x0 , y + (size * 0.25) , x+x0+x0+x1+x2 + x0+ x1, y + (size * 0.25) , fill='white', width = 2)
    self.create_line (x + (size/2), y + (size * 0.55) , x + (size/2) , y + (size * 0.65) , fill='white', width = 2)
    self.create_arc (x+x0+x0 , y-(size*0.05) , x+x0+x0+x1+x2+x1 , y+(size*0.55) , outline='white', style = 'chord', start=180 , extent=180, width = 2)
    self.create_line (x + (size / 2) , y + (size * 0.55) , x - (size / 2) , y + (size * 0.65) , fill='white' , width=2)
