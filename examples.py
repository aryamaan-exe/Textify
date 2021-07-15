from textify import Canvas

canvas = Canvas(10, 10, "#")

# Rectangle
canvas.rect("o", 1, 3, 4, 2, outline_width=0, outline_character="+")
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
canvas.render()
