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

# New state for mouse movement
is_moving_to_click = False
target_x = 0
target_y = 0

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
    global is_game_over, is_moving_forward, is_moving_backward, is_turning_left, is_turning_right, is_moving_to_click
    is_game_over = False
    
    # Reset movement flags
    is_moving_forward = is_moving_backward = is_turning_left = is_turning_right = is_moving_to_click = False
    
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
    # Updated instruction: Click now causes turtle to move gradually
    status_turtle.write("Use Arrows for continuous move. Click to move GRADUALLY to a spot. Click/C to restart after GOAL.", align="center", font=("Inter", 16, "normal"))

    screen.update()


# --- Continuous Game Loop ---

def game_loop():
    """
    The main game loop that runs repeatedly to check state and move the turtle.
    """
    if not is_game_over:
        moved = False
        
        # 1. Handle Gradual Mouse Movement (Priority 1)
        global is_moving_to_click, target_x, target_y
        
        if is_moving_to_click:
            distance_to_target = sketch_turtle.distance(target_x, target_y)
            
            if distance_to_target <= MOVE_DISTANCE:
                # Arrived at destination
                sketch_turtle.goto(target_x, target_y)
                is_moving_to_click = False
                sketch_turtle.pendown() # Resume drawing
                moved = True
            else:
                # Turn and move one step towards the target
                sketch_turtle.setheading(sketch_turtle.towards(target_x, target_y))
                sketch_turtle.forward(MOVE_DISTANCE)
                moved = True

        # 2. Handle Continuous Keyboard Movement (Priority 2: Only if not moving via mouse)
        elif not is_moving_to_click:
            if is_moving_forward:
                sketch_turtle.forward(MOVE_DISTANCE)
                moved = True
            if is_moving_backward:
                sketch_turtle.backward(MOVE_DISTANCE)
                moved = True
                
            # 3. Handle Continuous Turning (Turning doesn't count as a game move for win check)
            if is_turning_left:
                sketch_turtle.left(TURN_ANGLE)
            if is_turning_right:
                sketch_turtle.right(TURN_ANGLE)
            
        # 4. Check for Win Condition
        if moved:
            check_win()

        # 5. Manually update the screen once per tick
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
    """Handles mouse click event: Sets up a gradual move to the clicked position, or starts a new game if the current one is over."""
    global is_game_over, is_moving_to_click, target_x, target_y
    print(f"Mouse clicked at ({x}, {y}).")

    if is_game_over:
        # If game is over, click starts a new game
        setup_game()
        return
    
    # If the game is active, set the destination and activate mouse movement
    target_x, target_y = x, y
    is_moving_to_click = True
    
    # Lift the pen before moving to avoid drawing a line from the last point to the new one
    sketch_turtle.penup() 
    
    # Immediately disable keyboard control flags when mouse control takes over
    global is_moving_forward, is_moving_backward, is_turning_left, is_turning_right
    is_moving_forward = is_moving_backward = is_turning_left = is_turning_right = False
    
    print("Player initiated gradual mouse movement.")


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
