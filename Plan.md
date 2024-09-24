# Planning Document.

## Objective
![Screenshot 2024-09-23 131905](https://github.com/user-attachments/assets/1452a53c-2203-48a8-a42d-7beebd56b1ca)
### This is what we would want out final project to look like 
- To create a visual display using turtle graphics, where each turtle has a unique shape and color, positioned in a circular pattern.

## Planning Components

### 1. Variables

- **Turtle Lists**
  - `turtle_shapes`: List of shapes to assign to each turtle for example "arrow", "circle".
  - `turtle_colors`: List of colors to assign to each turtle for example "red", "blue".
  - `my_turtles`: List to store instances of turtle objects created.

- **Positioning Variables**
  - `startx`: X-coordinate for the starting position of the turtles.
  - `starty`: Y-coordinate for the starting position of the turtles.

- **Movement Variables**
  - `current_direction`: Variable to track the heading direction of each turtle.
  - `initial_length`: Starting length for the first turtle's movement.
  - `length_increment`: Amount to increase the movement length for each subsequent turtle.

### 2. Conditionals

- **Shape and Color**
  - Conditional checks to ensure there are enough shapes and colors available when assigning them to turtles.
  
- **Movement Logic**
  - Determine if the turtle has reached a certain position or angle to adjust the next turtle's placement accordingly.

### 3. Boolean Statements

- **List**
  - Use Boolean checks to verify if there are remaining shapes and colors in their respective lists before assigning them to a turtle.
  
- **Interaction**
  - Check for user input or window events to determine when to exit the program or restart the drawing.

## Logic Flow

1. **Turtle Graphics**
   - Set up the turtle screen and necessary configurations to the screen width and screen background color.

2. **Loop through Turtle Shapes**
   - For each shape in `turtle_shapes`:
     - Create a new turtle instance.
     - Assign a color from `turtle_colors`.
     - Move the turtle to the calculated position based on `startx`, `starty`.
     - Update `current_direction` and `initial_length` for the next iteration.
