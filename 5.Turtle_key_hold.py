import turtle
import random

# NOTE: The 'turtle' module is part of Python's standard library 
# and does not require 'pip install'.

# --- Configuration for Turtle Game ---
MOVE_DISTANCE = 5   # Smaller step for smoother continuous movement
TURN_ANGLE = 5      # Smaller angle for smoother continuous turning
WIN_DISTANCE = 20   # How close the player needs to be to win
GAME_TICK = 30      # Milliseconds delay for game loop (approx. 30 FPS)

# --- Global Game State ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
is_game_over = False

# New Global State Flags for continuous movement
is_moving_forward = False
is_moving_backward = False
is_turning_left = False
is_turning_right = False

screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("#111827") # Dark background
screen.title("Python Turtle Game: Reach the Target! (Continuous Movement)")
screen.tracer(0) # Turn off screen updates for manual control in the game loop

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
    global is_game_over, is_moving_forward, is_moving_backward, is_turning_left, is_turning_right
    is_game_over = False
    
    # Reset movement flags
    is_moving_forward = is_moving_backward = is_turning_left = is_turning_right = False
    
    # 1. Reset Player Turtle
    sketch_turtle.penup() 
    sketch_turtle.clear()
    sketch_turtle.goto(0, 0)
    sketch_turtle.setheading(90) # Start pointing up
    sketch_turtle.pendown()
    
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
    status_turtle.write("Use Arrows to move. Reach the red circle! (C to restart)", align="center", font=("Inter", 16, "normal"))

    screen.update()


# --- Continuous Game Loop ---

def game_loop():
    """
    The main game loop that runs repeatedly to check state and move the turtle.
    """
    if not is_game_over:
        
        # 1. Handle Continuous Movement
        if is_moving_forward:
            sketch_turtle.forward(MOVE_DISTANCE)
        if is_moving_backward:
            sketch_turtle.backward(MOVE_DISTANCE)
            
        # 2. Handle Continuous Turning
        if is_turning_left:
            sketch_turtle.left(TURN_ANGLE)
        if is_turning_right:
            sketch_turtle.right(TURN_ANGLE)
            
        # 3. Check for Win Condition
        if is_moving_forward or is_moving_backward:
            check_win()

        # 4. Manually update the screen once per tick
        screen.update()
    
    # Schedule the next call to the game loop
    screen.ontimer(game_loop, GAME_TICK)


# --- Key Binding Handlers (Setting/Unsetting Flags) ---

def press_forward(): global is_moving_forward; is_moving_forward = True
def release_forward(): global is_moving_forward; is_moving_forward = False

def press_backward(): global is_moving_backward; is_moving_backward = True
def release_backward(): global is_moving_backward; is_moving_backward = False

def press_left(): global is_turning_left; is_turning_left = True
def release_left(): global is_turning_left; is_turning_left = False

def press_right(): global is_turning_right; is_turning_right = True
def release_right(): global is_turning_right; is_turning_right = False

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

# Set up keyboard bindings using press/release for continuous movement

# Forward/Backward
screen.onkeypress(press_forward, "Up")
screen.onkeyrelease(release_forward, "Up")
screen.onkeypress(press_backward, "Down")
screen.onkeyrelease(release_backward, "Down")

# Left/Right Turning
screen.onkeypress(press_left, "Left")
screen.onkeyrelease(release_left, "Left")
screen.onkeypress(press_right, "Right")
screen.onkeyrelease(release_right, "Right")

# Discrete actions
screen.onkey(toggle_pen, "space")

# Bind 'C' key and Mouse Click to start new game
screen.onkey(setup_game, "c")
screen.onkey(setup_game, "C")
screen.onclick(handle_click)

# Start listening for events (IMPORTANT!)
screen.listen()

# Start the continuous game loop
game_loop()
print("Game started with continuous movement. Use arrow keys to control the blue turtle.")

# Keep the window open
turtle.done()
