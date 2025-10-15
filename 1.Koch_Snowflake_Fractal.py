import turtle

# NOTE: The 'turtle' module is part of Python's standard library 
# and does not require 'pip install'.
# If you were installing an external library, the command would be: 
# pip install <library-name>
# For this script, no installation is needed.

# --- Configuration ---
# Set the desired recursion depth (level of detail)
# Warning: Higher levels (4+) take significantly longer to draw!
RECURSION_LEVEL = 4
SIDE_LENGTH = 300 # The length of the initial triangle side

# --- Setup the Drawing Environment ---
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#1f2937") # Dark background for contrast
screen.title(f"Python Turtle - Koch Snowflake (Level {RECURSION_LEVEL})")

# --- Initialize the Turtle ---
snowflake_turtle = turtle.Turtle()
snowflake_turtle.speed(0) # Fastest drawing speed (0)
snowflake_turtle.hideturtle() # Hide the turtle icon
snowflake_turtle.pensize(2) 
snowflake_turtle.color("#60a5fa") # Bright blue line color

# --- Positioning the Turtle (to center the snowflake) ---
# Start drawing near the top-left of the screen 
# This ensures the entire shape is visible.
snowflake_turtle.penup()
snowflake_turtle.goto(-SIDE_LENGTH / 2, SIDE_LENGTH / 3)
snowflake_turtle.pendown()


# --- Koch Curve Function (Recursive) ---
def koch_curve(t, order, size):
    """
    Draws a Koch curve of a given order and size.
    This is the fundamental recursive function.
    
    Args:
        t (turtle.Turtle): The turtle object used for drawing.
        order (int): The current recursion depth.
        size (int): The length of the current line segment.
    """
    if order == 0:
        # Base case: Draw a straight line segment
        t.forward(size)
    else:
        # Recursive step: Break the line into 4 segments, 
        # rotating and calling the function on each new segment.
        
        # 1. First third (straight)
        koch_curve(t, order - 1, size / 3)
        
        # 2. Left turn (outward bump)
        t.left(60)
        koch_curve(t, order - 1, size / 3)
        
        # 3. Right turn (inward angle)
        t.right(120)
        koch_curve(t, order - 1, size / 3)
        
        # 4. Left turn (back to original direction)
        t.left(60)
        koch_curve(t, order - 1, size / 3)

# --- Koch Snowflake Function ---
def draw_koch_snowflake(t, order, size):
    """
    Draws the complete Koch Snowflake by drawing three Koch curves
    and rotating 120 degrees after each one.
    """
    for i in range(3):
        koch_curve(t, order, size)
        t.right(120)

# --- Execute Drawing ---
print(f"Drawing Koch Snowflake at level {RECURSION_LEVEL}...")
draw_koch_snowflake(snowflake_turtle, RECURSION_LEVEL, SIDE_LENGTH)
print("Drawing complete.")

# Keep the window open
turtle.done()
