from tkinter import *
import math

# Window
root = Tk()
root.title("Happy Birthday Sister")
root.geometry("800x600")
root.configure(bg="#4da6ff")  # Blue background

canvas = Canvas(root, width=800, height=600, bg="#4da6ff", highlightthickness=0)
canvas.pack()

# Title Text
title_y = 650
title = canvas.create_text(
    400,
    title_y,
    text="🎉 Happy Birthday Sister 🎉",
    font=("Comic Sans MS", 28, "bold"),
    fill="white"
)

# Birthday Quote
quote = canvas.create_text(
    400,
    120,
    text='"A sister is a little bit of childhood that can never be lost."',
    font=("Arial", 18, "italic"),
    fill="white"
)

# Heart points
heart_points = []

for t in range(0, 360):
    angle = math.radians(t)

    x = 16 * (math.sin(angle) ** 3)
    y = (
        13 * math.cos(angle)
        - 5 * math.cos(2 * angle)
        - 2 * math.cos(3 * angle)
        - math.cos(4 * angle)
    )

    # Scale and position
    px = 400 + x * 12
    py = 350 - y * 12

    heart_points.append((px, py))

# Pencil
pencil = canvas.create_text(
    heart_points[0][0],
    heart_points[0][1],
    text="✏",
    font=("Arial", 24),
    fill="yellow"
)

line_objects = []

# Animation variables
index = 1

def animate():
    global index, title_y

    # Move title upward
    if title_y > 60:
        title_y -= 2
        canvas.coords(title, 400, title_y)

    # Draw heart gradually
    if index < len(heart_points):
        x1, y1 = heart_points[index - 1]
        x2, y2 = heart_points[index]

        line = canvas.create_line(
            x1, y1, x2, y2,
            fill="red",
            width=3,
            smooth=True
        )

        line_objects.append(line)

        # Move pencil
        canvas.coords(pencil, x2, y2)

        index += 1

    root.after(15, animate)

animate()

root.mainloop()