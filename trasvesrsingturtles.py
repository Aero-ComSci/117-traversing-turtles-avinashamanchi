import turtle as trtl  

# created a list to store turtle shapes and colors
my_turtles = []

# created a list of turtle shapes to use
turtle_shapes = [
    "arrow", "turtle", "circle", "square", "triangle", "classic",
    "arrow", "turtle", "circle", "square", "triangle", "classic"
]

# created a list of colors for the turtles
turtle_colors = [
    "red", "blue", "green", "orange", "purple", "gold",
    "black", "magenta", "yellow", "lime", "pink", "brown"
]

# where the position for the turtles starts
startx = 0
starty = 0

# set the variables to control direction and length of movement
current_direction = 0
initial_length = 20  # the starting length for the first turtle
length_increment = 5  # how big the increment is for each turtle's length

# created a loop to be able to loop through each shape in the turtle_shapes list
for s in turtle_shapes:
    t = trtl.Turtle(shape=s)  
    t.penup()  # lifting the pen to move without drawing
    t.goto(startx, starty)  
    t.pendown()  
    
    color = turtle_colors.pop(0)  # being able to get the next color and remove it from the list
    t.color(color)  
    t.pensize(2) 
    
    t.setheading(current_direction)  
    t.forward(initial_length) 
    
    # set the starting coordinates for the next turtle
    startx = t.xcor()
    starty = t.ycor()

    current_direction += 30  
    initial_length += length_increment  

    my_turtles.append(t) 

wn = trtl.Screen()
wn.mainloop()  
