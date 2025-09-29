import tkinter as tk
import tkinter.ttk as tkk
from PIL import Image, ImageTk

root = tk.Tk()
root.attributes('-fullscreen', True)

canvas = tk.Canvas(root, bg="white", borderwidth=0, highlightthickness=0)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

def scale_coords(x, y, orig_width=2667, orig_height=1500, target_width=1920, target_height=1080):
    """
    Convert coordinates from an image scaled for orig_width x orig_height
    to target_width x target_height.
    """
    scale_x = target_width / orig_width
    scale_y = target_height / orig_height
    return int(x * scale_x), int(y * scale_y)

def create_background(filename, x, y, width, height):
    image = Image.open(filename)
    image = image.resize((width, height))
    image = ImageTk.PhotoImage(image)
    canvas.delete("all")  # Clear previous images
    canvas.image = image  # Keep a reference to avoid garbage collection
    canvas.create_image(x, y, anchor="nw", image=image)

def create_button(filename, x, y, width, height, command=None):
    scaled_width, scaled_height = scale_coords(width, height)
    image = Image.open(filename)
    image = image.resize((scaled_width, scaled_height))
    image = ImageTk.PhotoImage(image)
    button = tk.Button(
        root, 
        image=image, 
        command=command, 
        borderwidth=0, 
        highlightthickness=0,
        relief="flat"
    )
    button.image = image  # Keep a reference to avoid garbage collection
    canvas.create_window(x, y, anchor="nw", window=button, width=scaled_width, height=scaled_height)

create_background("images/Home.png", 0, 0, 1920, 1080)

create_button("images/Coast_Button.png", 528, 0, 268, 1500)
create_button("images/Valleys_Button.png", 720, 0, 400, 1500)
create_button("images/Plateau_Button.png", 1007, 0, 1267, 675)
create_button("images/Basin_Button.png", 1007, 486, 1267, 825)

root.mainloop()
