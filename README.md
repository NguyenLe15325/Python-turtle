# 🐢 Python Turtle Graphics

<div align="center">

![Python](https://img.shields.io/badge/python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Turtle Graphics](https://img.shields.io/badge/turtle-graphics-green?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Demos](https://img.shields.io/badge/demos-creative-orange?style=for-the-badge)

**Creative graphics and interactive demos using [Python Turtle](https://docs.python.org/3/library/turtle.html)**

*Learn Programming • Create Art • Build Interactive Applications*

</div>

---

## 🚀 Project Overview

This repository showcases creative graphics projects and interactive applications built with Python's **Turtle Graphics** module. From drawing programs to generative art, these demos demonstrate how Turtle can be used for both learning programming fundamentals and creating impressive visual applications.

Perfect for beginners learning Python, educators teaching programming concepts, or anyone interested in creative coding!

> **Note:** Demo applications were created with assistance from Google Gemini and Claude AI, and refined through experimentation.

---

## 🎨 Demo Collection

<table>
<tr>
<td width="50%">

### 🖌️ Creative Tools
- **Paint Program** — Full-featured drawing application
- **Pattern Generator** — Create geometric designs
- **Fractal Explorer** — Recursive art patterns

</td>
<td width="50%">

### 🎮 Interactive Demos
- **Games** — Simple turtle-based games
- **Animations** — Moving graphics and effects
- **Educational Tools** — Visual learning aids

</td>
</tr>
</table>

*Explore the creative possibilities of Python Turtle Graphics!*

---

## 🧩 Why Python Turtle?

<table>
<tr>
<td align="center" width="25%">
📚<br><strong>Beginner Friendly</strong>
<br>Perfect for learning Python basics
</td>
<td align="center" width="25%">
🎨<br><strong>Visual Feedback</strong>
<br>See your code come to life instantly
</td>
<td align="center" width="25%">
🔧<br><strong>Built-in Module</strong>
<br>No external dependencies needed
</td>
<td align="center" width="25%">
🌈<br><strong>Creative Expression</strong>
<br>Art, patterns, and animations
</td>
</tr>
</table>

---

## 🛠 Getting Started

### Prerequisites

- **Python 3.x** installed on your system
- **Turtle module** (included with Python standard library)

No additional installation required! 🎉

### Running a Demo

1. **Clone this repository:**
   ```bash
   git clone https://github.com/NguyenLe15325/Python-turtle.git
   cd Python-turtle
   ```

2. **Run any demo:**
   ```bash
   python paint.py
   # or
   python fractals.py
   ```

3. **Create and explore!**
   - Follow on-screen instructions for controls
   - Experiment with colors and patterns
   - Modify code to create your own designs

---

## 🎯 Learning Path

Progress through these demos to master Turtle Graphics:

**1. 🟢 Basic Drawing** (Simple shapes, lines)  
↓ *Learn turtle movement and pen control*

**2. 🟡 Interactive Input** (Click handling, keyboard events)  
↓ *Understand event-driven programming*

**3. 🟠 Complex Patterns** (Loops, functions, recursion)  
↓ *Create sophisticated designs*

**4. ⚫ Full Applications** (Paint program, games)  
↓ *Build complete interactive projects*

**5. 🎨 Your Masterpiece!**  
*Create original artwork or tools*

---

## ⭐ Featured Project: Paint Application

<div align="center">

### 🎨 Full-Featured Drawing Program

*A complete paint application built entirely with Python Turtle!*

<img src="assets/paint.gif" alt="Paint Application Demo" />

</div>

#### 🎯 About the Paint Program

This interactive drawing application demonstrates the full capabilities of Python Turtle Graphics. It features a complete toolkit for creating digital artwork, including multiple drawing tools, color selection, and canvas management—all built with Python's standard library!

#### ✨ Key Features

- 🖌️ **Multiple Drawing Tools**
  - Pencil — Freehand drawing
  - Brush — Thicker lines
  - Eraser — Remove mistakes
  - Fill tool — Color regions
  - Shapes — Circles, rectangles, lines

- 🎨 **Color System**
  - Color palette with preset colors
  - Custom color picker
  - RGB slider controls
  - Recently used colors

- 📐 **Drawing Controls**
  - Adjustable pen size (1-50 pixels)
  - Pen up/down for disconnected lines
  - Undo/redo functionality
  - Clear canvas option

- 💾 **Save & Load**
  - Export drawings as PostScript (.eps)
  - Save canvas state
  - Load previous work

- 🎛️ **User Interface**
  - Toolbar with tool icons
  - Color palette display
  - Size slider
  - Status bar showing current tool and color

#### 🎮 Controls

| Input | Action |
|-------|--------|
| `Left Click` | Draw with current tool |
| `Right Click` | Pick color from canvas |
| `Mouse Drag` | Continuous drawing |
| `1-9` | Quick select pen size |
| `C` | Open color picker |
| `E` | Switch to eraser |
| `P` | Switch to pencil |
| `B` | Switch to brush |
| `U` | Undo last action |
| `R` | Redo |
| `Ctrl+S` | Save drawing |
| `Ctrl+Z` | Undo |
| `Ctrl+Y` | Redo |
| `Delete` | Clear canvas |

#### 🔧 Technical Implementation

**Core Components:**

```python
class PaintApp:
    """Main application class managing the paint program"""
    def __init__(self):
        self.screen = turtle.Screen()
        self.canvas = turtle.Turtle()
        self.current_tool = "pencil"
        self.current_color = "black"
        self.pen_size = 3
        self.setup_ui()
    
    def draw(self, x, y):
        """Handle drawing on canvas"""
        if self.is_drawing:
            self.canvas.goto(x, y)
    
    def change_color(self, color):
        """Update drawing color"""
        self.current_color = color
        self.canvas.color(color)
    
    def setup_ui(self):
        """Create toolbar and color palette"""
        self.create_toolbar()
        self.create_palette()

class ColorPalette:
    """Manages color selection interface"""
    def __init__(self, x, y):
        self.colors = [
            "#000000", "#FFFFFF", "#FF0000", "#00FF00",
            "#0000FF", "#FFFF00", "#FF00FF", "#00FFFF"
        ]
        self.draw_palette(x, y)
    
    def on_click(self, x, y):
        """Handle color selection clicks"""
        selected = self.get_color_at(x, y)
        return selected

class DrawingTool:
    """Base class for different drawing tools"""
    def __init__(self, name, size, color):
        self.name = name
        self.size = size
        self.color = color
    
    def use(self, x, y):
        """Apply tool at coordinates"""
        pass
```

**Event Handling:**

```python
def setup_events(app):
    """Configure mouse and keyboard events"""
    screen = app.screen
    
    # Mouse events
    screen.onclick(app.on_click)
    screen.onscreenclick(app.on_click, btn=1)  # Left click
    screen.onscreenclick(app.pick_color, btn=3)  # Right click
    
    # Keyboard shortcuts
    screen.onkey(app.undo, "u")
    screen.onkey(app.clear_canvas, "Delete")
    screen.onkey(app.save, "s")
    
    # Enable listening
    screen.listen()
```

#### 🎓 What You'll Learn

- **Event-Driven Programming** — Mouse clicks, drags, and keyboard input
- **State Management** — Tracking current tool, color, and drawing state
- **UI Design** — Creating toolbars, palettes, and interactive elements
- **Object-Oriented Design** — Classes for tools, colors, and canvas management
- **Graphics Programming** — Coordinate systems, transformations, and rendering
- **File I/O** — Saving and loading drawings
- **User Experience** — Undo/redo, visual feedback, and intuitive controls

#### 💡 Enhancement Ideas

Extend the paint program with these features:

1. **Layer System** — Multiple drawing layers with transparency
2. **Text Tool** — Add text with different fonts and sizes
3. **Stamps & Stickers** — Pre-made shapes and images
4. **Gradient Tool** — Smooth color transitions
5. **Symmetry Mode** — Mirror drawing for mandala effects
6. **Animation Export** — Record drawing process as video
7. **Pressure Sensitivity** — Variable line thickness (with tablet support)
8. **Filters & Effects** — Blur, brightness, contrast adjustments
9. **Grid & Guides** — Alignment helpers
10. **Custom Brushes** — Create brush patterns and textures

#### 🎨 Example Drawings

What you can create with the paint program:
- 🌸 **Mandalas** — Symmetrical geometric patterns
- 🌄 **Landscapes** — Simple scenic artwork
- 🎭 **Pixel Art** — Grid-based designs
- ✏️ **Sketches** — Freehand drawings and doodles
- 📐 **Diagrams** — Technical illustrations
- 🌈 **Abstract Art** — Colorful creative expressions

---

## 📖 Python Turtle Resources

### 📚 Official Documentation
- [Python Turtle Documentation](https://docs.python.org/3/library/turtle.html)
- [Turtle Graphics Primer](https://docs.python.org/3/library/turtle.html#turtle-graphics-reference)
- [Real Python - Python Turtle Tutorial](https://realpython.com/beginners-guide-python-turtle/)

### 🎥 Video Tutorials
- [Python Turtle Graphics Tutorial](https://www.youtube.com/results?search_query=python+turtle+graphics+tutorial)
- [Turtle Graphics for Beginners](https://www.youtube.com/results?search_query=turtle+graphics+beginners)
- [Creative Coding with Turtle](https://www.youtube.com/results?search_query=python+turtle+creative+coding)

### 📝 Learning Resources
- [Turtle Academy](https://turtleacademy.com/) — Interactive turtle graphics lessons
- [Python for Kids - Turtle Graphics](https://www.nostarch.com/pythonforkids)
- [Trinket - Python Turtle Examples](https://trinket.io/python)

---

## 🎨 More Demo Highlights

### 🌀 Fractal Generator
Explore the beauty of recursive patterns with fractal drawing algorithms. Create stunning mathematical art including:
- **Koch Snowflake** — Classic fractal pattern
- **Sierpinski Triangle** — Self-similar triangular fractal
- **Dragon Curve** — Space-filling dragon pattern
- **Tree Fractals** — Recursive branching structures

### 🎯 Pattern Designer
Generate mesmerizing geometric patterns using loops and mathematical functions:
- **Spirals** — Fibonacci, Archimedean, and golden spirals
- **Rose Curves** — Mathematical rose patterns
- **Star Polygons** — Multi-pointed star shapes
- **Tessellations** — Repeating tile patterns

### 🎮 Interactive Games
Simple games demonstrating game logic with Turtle:
- **Snake Game** — Classic growing snake
- **Pong** — Paddle and ball mechanics
- **Maze Runner** — Navigate through generated mazes
- **Catch Game** — Reflexes and timing

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

You're free to use, modify, and distribute this code for personal or commercial projects.

---

## 🤝 Acknowledgements

<div align="center">

**Python Turtle Graphics** — Built-in Python module for creative programming

**The Python Community** — For tutorials, examples, and endless inspiration

**[Google Gemini](https://gemini.google.com/)** & **[Claude AI](https://claude.ai/)** — AI assistance in generating and refining demo code

**[ezgif.com](https://ezgif.com/)** — GIF editing and optimization tools

**Creative Coding Community** — Artists and educators sharing their work

</div>

---

## 📧 Contact & Links

<div align="center">

**Nguyen Le** • [@NguyenLe15325](https://github.com/NguyenLe15325)

[🌟 Star this repo](https://github.com/NguyenLe15325/Python-turtle) • [🐛 Report Bug](https://github.com/NguyenLe15325/Python-turtle/issues) • [💡 Request Feature](https://github.com/NguyenLe15325/Python-turtle/issues)

</div>

---

<div align="center">

### 🐢 Have fun creating art and learning Python with Turtle Graphics!

*Made with ❤️ and Python*

⭐ **If you find this helpful, consider starring the repository!** ⭐

</div>