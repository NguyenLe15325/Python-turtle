import turtle
import math
import cmath

# NOTE: The 'turtle' module is part of Python's standard library 
# and does not require 'pip install'.
# If you were installing an external library, the command would be: 
# pip install <library-name>
# For this script, no installation is needed.

# --- Configuration for Dragon Curve ---
ORDER = 13       # Recursion depth (higher = more detail, slightly slower)
LENGTH = 5       # Length of each line segment (in pixels)
START_DIRECTION = 45 # Initial direction (e.g., 0=East, 90=North)

# --- Setup the Drawing Environment ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("#1f2937") # Dark background
screen.title(f"Python Turtle - Dragon Curve Fractal (Order {ORDER})")
screen.colormode(255) # Use 0-255 color range

# --- Initialize the Turtle ---
dragon_turtle = turtle.Turtle()
dragon_turtle.speed(0)      # Fastest drawing speed
dragon_turtle.hideturtle()  # Hide the turtle icon
dragon_turtle.pensize(1)
dragon_turtle.color("#7dd3fc") # Light blue color

# --- Positioning the Turtle (to start drawing from the center-left) ---
dragon_turtle.penup()
dragon_turtle.goto(-100, 0)
dragon_turtle.setheading(START_DIRECTION)
dragon_turtle.pendown()


# --- Dragon Curve Logic ---

def generate_dragon_sequence(order):
    """
    Generates the sequence of 'R' (Right) and 'L' (Left) turns 
    for the specified Dragon Curve order.
    
    Args:
        order (int): The order of the fractal.
        
    Returns:
        str: A string of R's and L's representing the turns.
    """
    sequence = ""
    for i in range(1, order + 1):
        # Create the reverse of the current sequence
        reversed_sequence = sequence[::-1]
        
        # Swap R's and L's in the reversed sequence
        new_turns = reversed_sequence.replace('R', 'x').replace('L', 'R').replace('x', 'L')
        
        # Append 'R' and the new turns to the current sequence
        sequence = sequence + "R" + new_turns
    
    return sequence

def draw_dragon_curve(t, sequence, length):
    """
    Draws the fractal based on the generated instruction sequence.
    """
    t.forward(length) # Initial segment
    
    # Iterate through the sequence of turns
    for move in sequence:
        if move == 'R':
            t.right(90)
        elif move == 'L':
            t.left(90)
        
        # Draw the next segment after turning
        t.forward(length)

# --- Execute Drawing ---
print(f"Generating Dragon Curve sequence at order {ORDER}...")
sequence = generate_dragon_sequence(ORDER)
print(f"Sequence length: {len(sequence)}")

print("Drawing Dragon Curve...")
draw_dragon_curve(dragon_turtle, sequence, LENGTH)

print("Drawing complete.")

# Keep the window open
turtle.done()
