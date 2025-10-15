import turtle
import random

# NOTE: The 'turtle' module is part of Python's standard library 
# and does not require 'pip install'.

# --- Configuration for Turtle Game ---
MOVE_DISTANCE = 5   # Speed of the turtle when following the mouse
WIN_DISTANCE = 20   # How close the player needs to be to win
GAME_TICK = 30      # Milliseconds delay for game loop (approx. 30 FPS)

# --- Global Game State ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
is_game_over = False

# New global state for continuous mouse tracking (Fix for AttributeError)
cursor_x = 0
cursor_y = 0
is_mouse_visible = False # True if the mouse is currently over the canvas

screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("#111827") # Dark background
screen.title("Python Turtle Game: Cursor Follower (Fixed)")
screen.tracer(0) # Turn off screen updates for manual control in the game loop

# --- Initialize Player Turtle ---
sketch_turtle = turtle.Turtle()
sketch_turtle.speed(0)      # Fastest animation speed
sketch_turtle.shape("turtle") # Use the default turtle shape
sketch_turtle.turtlesize(1.5)
sketch_turtle.pensize(3)
sketch_turtle.color("#38bdf8") # Bright blue color for drawing
sketch_turtle.penup() # Pen up by default for chase movement

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


# --- Mouse Handler Functions (FIX: New functions to track mouse motion) ---

def handle_mouse_motion(event):
    """Updates global cursor coordinates using Tkinter event data (continuous tracking)."""
    global cursor_x, cursor_y, is_mouse_visible
    # Convert Tkinter pixel coordinates (event.x, event.y) to Turtle coordinates (relative to center)
    cursor_x = event.x - SCREEN_WIDTH / 2
    cursor_y = SCREEN_HEIGHT / 2 - event.y
    is_mouse_visible = True

def handle_mouse_leave(event):
    """Called when the mouse leaves the drawing window, stopping the follow movement."""
    global is_mouse_visible
    is_mouse_visible = False


# --- Game Logic Functions ---

def check_win():
    """Checks if the player turtle has reached the target."""
    global is_game_over
    if is_game_over:
        return

    distance = sketch_turtle.distance(target_turtle)
    
    if distance < WIN_DISTANCE:
        is_game_over = True
        status_turtle.clear()
        status_turtle.write("GOAL! Press [C] or Click to play again.", align="center", font=("Inter", 24, "bold"))
        print("WIN: Target Reached!")
        
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
    
    # 2. Position Target Turtle randomly
    min_coord = 150 # Minimum distance from center
    
    while True:
        x = random.randint(-SCREEN_WIDTH//2 + 50, SCREEN_WIDTH//2 - 50)
        y = random.randint(-SCREEN_HEIGHT//2 + 50, SCREEN_HEIGHT//2 - 50)
        if abs(x) > min_coord or abs(y) > min_coord:
            break

    target_turtle.goto(x, y)
    target_turtle.showturtle()

    # 3. Clear Status Message and provide instructions
    status_turtle.clear()
    status_turtle.write("Move mouse over the screen to guide the turtle! Click/C to restart after GOAL.", align="center", font=("Inter", 16, "normal"))

    screen.update()

def handle_click(x, y):
    """Handles simple mouse click event: Only starts a new game if the current one is over."""
    global is_game_over
    if is_game_over:
        setup_game()
        return
    
    # If the game is active, clicks have no effect (movement is automatic)


# --- Continuous Game Loop ---

def game_loop():
    """
    The main game loop that runs repeatedly to check state and move the turtle.
    This loop now uses the event-updated global mouse position.
    """
    if not is_game_over:
        moved = False
        
        # 1. Get the current mouse coordinates from global variables
        global cursor_x, cursor_y, is_mouse_visible
        
        # 2. Check if the cursor is actually inside the window area
        if is_mouse_visible:
            
            distance_to_cursor = sketch_turtle.distance(cursor_x, cursor_y)
            
            # Only move if we are far enough from the cursor to prevent jitter
            if distance_to_cursor > MOVE_DISTANCE / 2: 
                # Turn and move one step towards the cursor's position
                sketch_turtle.setheading(sketch_turtle.towards(cursor_x, cursor_y))
                sketch_turtle.forward(MOVE_DISTANCE)
                moved = True
            
        # 3. Check for Win Condition
        if moved:
            check_win()

        # 4. Manually update the screen once per tick
        screen.update()
    
    # Schedule the next call to the game loop
    screen.ontimer(game_loop, GAME_TICK)


# --- Execute and Listen for Events ---

# Initial setup: Start the first game
setup_game()

# BIND THE CONTINUOUS MOUSE TRACKING EVENT (FIX)
# We use the underlying Tkinter canvas (.cv) to bind the <Motion> event
# for continuous tracking, which is not available directly on the turtle screen object.
screen.cv.bind('<Motion>', handle_mouse_motion)
screen.cv.bind('<Leave>', handle_mouse_leave)

# Set up only the discrete keyboard and mouse bindings

# Bind 'C' key for new game
screen.onkey(setup_game, "c")
screen.onkey(setup_game, "C")

# Bind mouse click only for restarting the game after goal
screen.onclick(handle_click)

# Start listening for events (IMPORTANT!)
screen.listen()

# Start the continuous game loop
game_loop()
print("Game started with mouse following enabled.")

# Keep the window open
turtle.done()
