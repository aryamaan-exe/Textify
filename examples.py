from textify import Canvas

canvas = Canvas()

# Rectangle
canvas.rect(fillcharacter, xposition, yposition, width, height, outline_width=0, outline_character="+")
canvas.render()


# Display a 2d vector ascii image like this

image = [['#','O','#'],
        ['/','|','\'],
        ['#','|','#'],
        ['/','#','\']]
canvas.draw_image(x,y,image)
canvas.render()

# Add borders to the canvas: 

canvas.addborders('x','*') # x - axis, y - axis
