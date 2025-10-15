import turtle
import random

# NOTE: The 'turtle' module is part of Python's standard library 
# and does not require 'pip install'.

# --- Configuration for Turtle Game ---
MOVE_DISTANCE = 10  # Pixels to move with each key press
TURN_ANGLE = 30     # Degrees to turn with each key press
WIN_DISTANCE = 20   # How close the player needs to be to win

# --- Setup the Drawing Environment ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
is_game_over = False

screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("#111827") # Dark background
screen.title("Python Turtle Game: Reach the Target!")
screen.tracer(0) # Turn off screen updates for smoother movement

# --- Initialize Player Turtle ---
sketch_turtle = turtle.Turtle()
sketch_turtle.speed(0)      # Fastest animation speed
sketch_turtle.shape("turtle") # Use the default turtle shape
sketch_turtle.turtlesize(1.5)
sketch_turtle.pensize(3)
sketch_turtle.color("#38bdf8") # Bright blue color for drawing

# --- Initialize Target Turtle ---
target_turtle = turtle.Turtle()
target_turtle.shape("circle")
target_turtle.color("#dc2626") # Red target
target_turtle.penup()
target_turtle.speed(0)
target_turtle.turtlesize(1.5)

# --- Initialize Status Display Turtle ---
status_turtle = turtle.Turtle()
status_turtle.hideturtle()
status_turtle.penup()
status_turtle.color("white")
status_turtle.goto(0, SCREEN_HEIGHT/2 - 40)


# --- Game Logic Functions ---

def check_win():
    """Checks if the player turtle has reached the target."""
    global is_game_over
    if is_game_over:
        return

    # Check distance between the two turtles
    distance = sketch_turtle.distance(target_turtle)
    
    if distance < WIN_DISTANCE:
        is_game_over = True
        status_turtle.clear()
        status_turtle.write("GOAL! Press [C] or Click to play again.", align="center", font=("Inter", 24, "bold"))
        print("WIN: Target Reached!")
        
        # Stop drawing and hide the target
        sketch_turtle.penup() 
        target_turtle.hideturtle()
        screen.update()

def setup_game():
    """Sets up the player and target for a new game."""
    global is_game_over
    is_game_over = False
    
    # 1. Reset Player Turtle
    sketch_turtle.penup() 
    sketch_turtle.clear()
    sketch_turtle.goto(0, 0)
    sketch_turtle.setheading(90) # Start pointing up
    sketch_turtle.pendown()
    
    # 2. Position Target Turtle randomly
    # Generate coordinates far enough from the center (0, 0)
    min_coord = 150 # Minimum distance from center
    
    # Generate random x/y within bounds, ensuring they are outside the min_coord area
    while True:
        x = random.randint(-SCREEN_WIDTH//2 + 50, SCREEN_WIDTH//2 - 50)
        y = random.randint(-SCREEN_HEIGHT//2 + 50, SCREEN_HEIGHT//2 - 50)
        if abs(x) > min_coord or abs(y) > min_coord:
            break

    target_turtle.goto(x, y)
    target_turtle.showturtle()

    # 3. Clear Status Message and provide instructions
    status_turtle.clear()
    status_turtle.write("Use Arrows to move. Reach the red circle! (C to restart)", align="center", font=("Inter", 16, "normal"))

    screen.update()


# --- Player Control Functions ---

def move_forward():
    if not is_game_over:
        sketch_turtle.forward(MOVE_DISTANCE)
        screen.update()
        check_win()

def move_backward():
    if not is_game_over:
        sketch_turtle.backward(MOVE_DISTANCE)
        screen.update()
        check_win()

def turn_left():
    if not is_game_over:
        sketch_turtle.left(TURN_ANGLE)
        screen.update()

def turn_right():
    if not is_game_over:
        sketch_turtle.right(TURN_ANGLE)
        screen.update()

def toggle_pen():
    """Toggles the pen up (stop drawing) or pen down (start drawing)."""
    if not is_game_over:
        if sketch_turtle.isdown():
            sketch_turtle.penup()
        else:
            sketch_turtle.pendown()

def handle_click(x, y):
    """Handles mouse click event: starts a new game."""
    print(f"Mouse clicked at ({x}, {y}). Starting new game.")
    setup_game()


# --- Execute and Listen for Events ---

# Initial setup: Start the first game
setup_game()

# Set up keyboard bindings
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(toggle_pen, "space")

# Bind 'C' key to start new game
screen.onkey(setup_game, "c")
screen.onkey(setup_game, "C")

# Set up mouse click binding
screen.onclick(handle_click)

# Start listening for events (IMPORTANT!)
screen.listen()
print("Game started. Use arrow keys to control the blue turtle.")

# Keep the window open
turtle.done()
