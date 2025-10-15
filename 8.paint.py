import turtle

# NOTE: The 'turtle' module is part of Python's standard library 
# and does not require 'pip install'.

# --- Configuration ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
DEFAULT_PENSIZE = 5
MIN_PENSIZE = 1
MAX_PENSIZE = 20
DEFAULT_ERASER_SIZE = 50 # New default constant
MAX_ERASER_SIZE = 100 # New max constant
BACKGROUND_COLOR = "#111827"
COLOR_PALETTE = ["red", "blue", "green", "orange", "purple"]

# --- Global State ---
current_pensize = DEFAULT_PENSIZE
current_eraser_size = DEFAULT_ERASER_SIZE # Initializing adjustable eraser size
current_color_index = 0
is_erasing = False
cursor_x = 0
cursor_y = 0

screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(BACKGROUND_COLOR) # Use constant
screen.title("Interactive Turtle Paint App")
screen.tracer(0) # Disable automatic updates for smoother drawing

# --- Initialize Drawing Turtle (Hidden) ---
pen_turtle = turtle.Turtle()
pen_turtle.shape("arrow")
pen_turtle.color(COLOR_PALETTE[current_color_index])
pen_turtle.pensize(current_pensize)
pen_turtle.speed(0)
pen_turtle.penup()
pen_turtle.hideturtle() # Drawing pen remains hidden

# --- Initialize Cursor Turtle (Visible Brush Indicator) ---
cursor_turtle = turtle.Turtle()
cursor_turtle.shape("circle")
cursor_turtle.color("white")
cursor_turtle.pensize(2)
cursor_turtle.penup()
cursor_turtle.speed(0)
cursor_turtle.hideturtle() # HIDE THE TURTLE SHAPE, only show the drawn outline

# --- Initialize Status Turtle (for Instructions) ---
status_turtle = turtle.Turtle()
status_turtle.hideturtle()
status_turtle.penup()
status_turtle.color("white")

# --- Utility Functions ---

def write_status():
    """Clears and rewrites the instruction text."""
    status_turtle.clear()
    status_turtle.goto(0, SCREEN_HEIGHT/2 - 40)
    status_turtle.write(
        "Drag mouse to draw. Colors: 1-5. Size: +/-. Mode: E (Eraser/Brush). Clear: C/Space.", 
        align="center", 
        font=("Inter", 14, "normal")
    )
    # REMOVED screen.update() from here. Update is now managed in update_cursor_visuals().

def update_cursor_visuals():
    """Updates the cursor_turtle's position and appearance to match mode/size."""
    cursor_turtle.clear()
    cursor_turtle.goto(cursor_x, cursor_y)

    if is_erasing:
        size = current_eraser_size # Use current_eraser_size variable
        color = "white"
    else:
        size = current_pensize
        color = COLOR_PALETTE[current_color_index]
    
    # Draw a circle outline that represents the brush size
    cursor_turtle.color(color)
    cursor_turtle.pendown()
    # Draw circle based on diameter (size). The radius is size / 2.
    cursor_turtle.circle(size / 2) 
    cursor_turtle.penup()
    
    # ADDED: Redraw status text immediately before the final screen update
    write_status()
    
    screen.update()

# --- Drawing Functions ---

def start_draw(x, y):
    """Called when the mouse button is pressed down (start of drag)."""
    pen_turtle.penup()
    
    # Set pen size/color based on mode
    if is_erasing:
        pen_turtle.color(BACKGROUND_COLOR)
        pen_turtle.pensize(current_eraser_size) # Use current_eraser_size variable
    else:
        pen_turtle.color(COLOR_PALETTE[current_color_index])
        pen_turtle.pensize(current_pensize)

    pen_turtle.goto(x, y)
    pen_turtle.pendown()

def draw(x, y):
    """Called continuously while the mouse is dragged (during draw)."""
    # Simply move the turtle to the new cursor position. 
    pen_turtle.goto(x, y)
    
    # NOTE: screen.update() is called inside handle_mouse_drag_tk via update_cursor_visuals()
    # to maintain high-frequency redraws during drawing.

def stop_draw(x, y):
    """Called when the mouse button is released (end of drag)."""
    pen_turtle.penup()
    # Ensure cursor visuals are updated if needed
    update_cursor_visuals()


# --- Control Functions (Keyboard) ---

def clear_screen():
    """Clears all drawings and resets the turtle's position."""
    pen_turtle.clear()
    pen_turtle.penup()
    pen_turtle.goto(0, 0)
    pen_turtle.pendown()
    # write_status() is now called in update_cursor_visuals()
    screen.update() # Ensure the canvas clear is visible immediately

def toggle_eraser():
    """Toggles between drawing and erasing mode."""
    global is_erasing
    is_erasing = not is_erasing
    
    # Update cursor visual to reflect the new mode
    update_cursor_visuals()
    
    mode = "Eraser" if is_erasing else "Brush"
    print(f"Mode toggled to: {mode}")

def change_color(color_index):
    """Changes the pen color based on the index provided."""
    global current_color_index, is_erasing
    if 0 <= color_index < len(COLOR_PALETTE):
        # 1. Turn off eraser mode to switch back to painting
        was_erasing = is_erasing
        is_erasing = False 
        
        # 2. Update color index
        current_color_index = color_index
        new_color = COLOR_PALETTE[current_color_index]
        
        # 3. Update cursor visual (always update now that mode might have changed)
        update_cursor_visuals() 
        
        # 4. Print message
        if was_erasing:
            print(f"Switched from Eraser to Brush. Color set to: {new_color}")
        else:
            print(f"Color set to: {new_color}")


def increase_size():
    """Increases the pen size or eraser size, up to the respective maximum."""
    global current_pensize, current_eraser_size
    if is_erasing:
        # Increase eraser size by 5 (for quicker adjustment since it's a larger tool)
        if current_eraser_size < MAX_ERASER_SIZE:
            current_eraser_size += 5
            update_cursor_visuals()
            print(f"Eraser size increased to: {current_eraser_size}")
    else:
        # Increase pen size by 1
        if current_pensize < MAX_PENSIZE:
            current_pensize += 1
            update_cursor_visuals()
            print(f"Pen size increased to: {current_pensize}")

def decrease_size():
    """Decreases the pen size or eraser size, down to the minimum."""
    global current_pensize, current_eraser_size
    if is_erasing:
        # Decrease eraser size by 5
        if current_eraser_size > MIN_PENSIZE + 4: # Prevent shrinking too close to 1
            current_eraser_size -= 5
            update_cursor_visuals()
            print(f"Eraser size decreased to: {current_eraser_size}")
    else:
        # Decrease pen size by 1
        if current_pensize > MIN_PENSIZE:
            current_pensize -= 1
            update_cursor_visuals()
            print(f"Pen size decreased to: {current_pensize}")

# --- Tkinter Event Wrapper Functions ---

def handle_mouse_coords(event):
    """Converts Tkinter pixel coords to Turtle coords (0,0 center)."""
    width = screen.window_width()
    height = screen.window_height()
    # Tkinter (0,0) is top-left. Turtle (0,0) is center.
    turtle_x = event.x - width / 2
    turtle_y = height / 2 - event.y
    return turtle_x, turtle_y

def handle_mouse_down_tk(event):
    """Tkinter wrapper for <Button-1> (mouse down). Starts drawing."""
    x, y = handle_mouse_coords(event)
    start_draw(x, y)

def handle_mouse_drag_tk(event):
    """Tkinter wrapper for <B1-Motion> (mouse drag). Continues drawing and moves cursor."""
    global cursor_x, cursor_y
    x, y = handle_mouse_coords(event)
    cursor_x, cursor_y = x, y # Update cursor position
    update_cursor_visuals() # Move cursor visual and redraw status
    draw(x, y)

def handle_mouse_up_tk(event):
    """Tkinter wrapper for <ButtonRelease-1> (mouse up). Stops drawing."""
    stop_draw(None, None)

def handle_mouse_motion_tk(event):
    """Tkinter wrapper for <Motion> (mouse movement without click). Moves cursor."""
    global cursor_x, cursor_y
    x, y = handle_mouse_coords(event)
    cursor_x, cursor_y = x, y # Update global position
    update_cursor_visuals() # Move and redraw the cursor turtle and status


# --- Event Bindings ---

# Bind mouse motion (CURSOR FOLLOW)
screen.cv.bind('<Motion>', handle_mouse_motion_tk)
# Bind mouse down (start draw)
screen.cv.bind('<Button-1>', handle_mouse_down_tk) 
# Bind drag/motion while button 1 is pressed (continuous drawing)
screen.cv.bind('<B1-Motion>', handle_mouse_drag_tk)
# Bind mouse button release (stop draw)
screen.cv.bind('<ButtonRelease-1>', handle_mouse_up_tk) 


# Keyboard Bindings:
screen.onkey(clear_screen, "c")
screen.onkey(clear_screen, "C")
screen.onkey(clear_screen, "space")

# Eraser Toggle
screen.onkey(toggle_eraser, "e")
screen.onkey(toggle_eraser, "E")

# Size controls
screen.onkey(increase_size, "+")
screen.onkey(increase_size, "equal") # For keyboards where '+' is SHIFT + '='
screen.onkey(decrease_size, "-")
screen.onkey(decrease_size, "underscore") # For keyboards where '-' is used

# Color selection using numbers 1-5
screen.onkey(lambda: change_color(0), "1")
screen.onkey(lambda: change_color(1), "2")
screen.onkey(lambda: change_color(2), "3")
screen.onkey(lambda: change_color(3), "4")
screen.onkey(lambda: change_color(4), "5")


# Start listening for events (CRITICAL)
screen.listen()

# Initial cursor draw (which now also calls write_status())
update_cursor_visuals()

# Keep the window open
turtle.done()
