import turtle as trtl

# utilized a class that initializes the turtle object with a specified shape and color
class TurtleShape:
    def __init__(self, shape, color):
        self.turtle = trtl.Turtle(shape=shape)
        # lifts the pen to not draw while moving to the initial position
        self.turtle.penup()
        self.turtle.color(color)


    # moves the turtle to a start position and draws a line at a specific angle and length
    def move_and_draw(self, startx, starty, startDir, forwardLength):
        # moves the turtle to a starting (x, y) position without drawing
        self.turtle.goto(startx, starty)
        self.turtle.pendown()
        self.turtle.setheading(startDir)
        self.turtle.right(45)
        self.turtle.forward(forwardLength)

# bellow is a list of turtle shapes and colors that print in sequence
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["yellow", "purple", "orange", "green", "blue", "red"]

# the following starting positions and direction
startx = 0
starty = 0
startDir = 90
forwardLength = 50

my_turtles = []
for shape, color in zip(turtle_shapes, turtle_colors):
    my_turtles.append(TurtleShape(shape, color))

# this for loop moves and draws for each turtle which ultimatley updates the startx, starty, startDir, and forwardLength for the next drawing
for turtle_obj in my_turtles:
    turtle_obj.move_and_draw(startx, starty, startDir, forwardLength)
    
    # this code pience here update startx, starty, startDir, and forwardLength globally for the next turtle and the next shape on going
    startx = turtle_obj.turtle.xcor()
    starty = turtle_obj.turtle.ycor()
    startDir = turtle_obj.turtle.heading()
    forwardLength += 3

wn = trtl.Screen()
wn.mainloop()
