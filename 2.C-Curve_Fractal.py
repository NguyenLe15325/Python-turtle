import turtle

# NOTE: The 'turtle' module is part of Python's standard library 
# and does not require 'pip install'.
# If you were installing an external library, the command would be: 
# pip install <library-name>
# For this script, no installation is needed.

# --- Configuration ---
# Set the desired recursion depth (level of detail)
# The C-Curve works well with higher levels than the Koch Snowflake.
# Warning: Levels above 12-14 can take a long time to draw!
RECURSION_LEVEL = 11 
SIDE_LENGTH = 150 # The length of the initial segment

# --- Setup the Drawing Environment ---
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#1f2937") # Dark background for contrast
screen.title(f"Python Turtle - C-Curve Fractal (Level {RECURSION_LEVEL})")

# --- Initialize the Turtle ---
ccurve_turtle = turtle.Turtle()
ccurve_turtle.speed(0) # Fastest drawing speed (0)
ccurve_turtle.hideturtle() # Hide the turtle icon
ccurve_turtle.pensize(1) 
ccurve_turtle.color("#fca5a5") # Light red/pink line color

# --- Positioning the Turtle (to start the C-Curve from the center) ---
# Start at the center of the screen (0, 0)
ccurve_turtle.penup()
ccurve_turtle.goto(0, 0)
ccurve_turtle.pendown()


# --- C-Curve Function (Recursive) ---
def c_curve(t, order, size):
    """
    Draws a C-Curve fractal of a given order and size.
    
    Args:
        t (turtle.Turtle): The turtle object used for drawing.
        order (int): The current recursion depth.
        size (int): The length of the current line segment.
    """
    if order == 0:
        # Base case: Draw a straight line segment
        t.forward(size)
        return
    
    # Recursive step:
    # Each new segment length is divided by sqrt(2) ≈ 1.414
    new_size = size / 1.414 
    
    # 1. Turn right 45 degrees
    t.right(45)
    c_curve(t, order - 1, new_size)

    # 2. Turn left 90 degrees
    t.left(90)
    c_curve(t, order - 1, new_size)

    # 3. Turn right 45 degrees (to restore the overall orientation)
    t.right(45)


# --- Execute Drawing ---
print(f"Drawing C-Curve Fractal at level {RECURSION_LEVEL}...")
c_curve(ccurve_turtle, RECURSION_LEVEL, SIDE_LENGTH)
print("Drawing complete.")

# Keep the window open
turtle.done()
