import os

class Canvas:
    def __init__(self,width,height,background_char):
        self.width = width
        self.height = height
        self.display = [background_char]*(width*height)
        self.xborder = ""
        self.yborder = "" 
    def render(self):
        """

            Prints display, with formatting.

            Returns none.
        """
        display = self.display
        print(self.xborder*self.width)
        for i in range(self.height):
            
            print(self.yborder + "".join(display[self.width*i:self.width*(i+1)]) + self.yborder)
        print(self.xborder*self.width)
    def render_val(self):
        """

            Returns canvas display, with formatting

        """
        display = ""
        display += self.xborder*self.width + "\n"
        for i in range(self.height):
            display += self.yborder+"".join(self.display[self.width*i:self.width*(i+1)])+ self.yborder + "\n"
        display += self.xborder*self.width
        return display
    def rect(self,background_character,y,x,width,height,line_width=0,line_width_character=" "):
        """

           Fills a square at given coordinates, x and y, to extent of the given width and height with
           background_character as the background.

           Returns none.
           
        """
        if line_width==0:
            for i in range(x,x+width):
                for j in range(y,y+height):
                    self.display[(i*self.width)+j] = background_character
        elif line_width>0:
            for i in range(x-line_width,x+width+line_width):
                for j in range(y-line_width,y+height+line_width):
                    self.display[(i*self.width)+j] = line_width_character
            for i in range(x,x+width):
                for j in range(y,y+height):
                    self.display[(i*self.width)+j] = background_character
            
    def addborders(self,x_axis,y_axis):
        """
            Make a border for the canvas (outline, will not affect display in any way.)
            x axis is for horizontal bordering of canvas
            y axis is for vertical bordering of canvas

            Leave empty string if the particular axis is not needed

            Variables will be set, no value will be returned from this function.

        """
        self.xborder = x_axis
        self.yborder = y_axis

    def draw_image(self,x,y,image):
        """
            Draw a 2d array representing your image

            returns nothing

        """
        height = len(image)
        width = len(image[0])
        for i in range(x,x+width):
            for j in range(y,y+height):
                self.display[(i*self.width)+j] = image[i-x][j-y]
        
