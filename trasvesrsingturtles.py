import turtle as trtl

class AviTurtle:
    def __init__(self, shape, color, startx, starty, direction, length):
        self.turtle = trtl.Turtle(shape=shape)
        self.turtle.penup()
        self.turtle.goto(startx, starty)
        self.turtle.pendown()
        self.turtle.color(color)
        self.turtle.pensize(2)
        self.turtle.setheading(direction)
        self.turtle.forward(length)

    def get_position(self):
        return self.turtle.xcor(), self.turtle.ycor()

class TurtleAvi:
    def __init__(self, shapes, colors, initial_length, length_increment):
        self.turtles = []
        self.shapes = shapes
        self.colors = colors
        self.initial_length = initial_length
        self.length_increment = length_increment
        self.current_direction = 0
        self.startx = 0
        self.starty = 0
        self.create_turtles()

    def create_turtles(self):
        for shape in self.shapes:
            color = self.colors.pop(0)
            turtle = AviTurtle(shape, color, self.startx, self.starty, self.current_direction, self.initial_length)
            self.turtles.append(turtle)
            self.startx, self.starty = turtle.get_position()
            self.current_direction += 40
            self.initial_length += self.length_increment

turtle_shapes = ["arrow", "triangle", "square", "circle", "turtle", "arrow"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", 
                 "red", "blue", "green", "orange", "purple", "gold"]

turtle_draw = TurtleAvi(turtle_shapes, turtle_colors, initial_length=45, length_increment=0)

wn = trtl.Screen()
wn.mainloop()

