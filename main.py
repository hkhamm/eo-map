import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.attributes('-fullscreen', True)

canvas = tk.Canvas(
    root, 
    width=root.winfo_screenwidth(), 
    height=root.winfo_screenheight(), 
    borderwidth=0, 
    highlightthickness=0, 
    bg="white"
)
canvas.pack()

def scale_coords(x, y, orig_width=2667, orig_height=1500, target_width=1920, target_height=1080):
    """
    Convert coordinates from an image scaled for orig_width x orig_height
    to target_width x target_height.
    """
    scale_x = target_width / orig_width
    scale_y = target_height / orig_height
    return int(x * scale_x), int(y * scale_y)

def create_background(filename, width, height):
    image = Image.open(filename)
    image = image.resize((width, height))
    image = ImageTk.PhotoImage(image)
    canvas.delete("all")  # Clear previous items
    canvas.image = image  # Keep a reference to avoid garbage collection
    canvas.create_image(0, 0, anchor="nw", image=image)

def create_button(filename, x, y, width, height, command=None):
    image = Image.open(filename)
    scaled_width, scaled_height = scale_coords(width, height)
    image = image.resize((scaled_width, scaled_height))
    image = ImageTk.PhotoImage(image)
    button = tk.Button(
        canvas,
        image=image, 
        borderwidth=0,
        bd=0,
        highlightthickness=0,
        command=command,
        height=scaled_height,
        width=scaled_width
    )
    button.image = image
    canvas.create_window(x, y, anchor="nw", window=button, width=scaled_width, height=scaled_height)

def open_home():
    create_background("images/Home.png", 1920, 1080)  
    create_button("images/Coast_Button.png", 528, 0, 268, 1500, command=open_coast)
    create_button("images/Valleys_Button.png", 720, 0, 400, 1500, command=open_valley)
    create_button("images/Plateau_Button.png", 1007, 0, 1267, 675)
    create_button("images/Basin_Button.png", 1007, 486, 1267, 825)

def open_coast():
    create_background("images/Coast_Home.png", 1920, 1080)
    create_button("images/Home_Button.png", 1681, 79, 283, 101, command=open_home)
    create_button("images/Coast_Neskowin_Button.png", 596, 177, 1688, 286, command=open_coast_1)
    create_button("images/Coast_Yaquina_Button.png", 597, 396, 1688, 286, command=open_coast_2)
    create_button("images/Coast_Dunes_Button.png", 596, 617, 1688, 286, command=open_coast_3)
    create_button("images/Coast_SOLVE_Button.png", 595, 839, 1688, 286, command=open_coast_4)

def open_coast_1():
    create_background("images/Coast_1.png", 1920, 1080)
    create_button("images/Back_Button.png", 1466, 79, 283, 101, command=open_coast)
    create_button("images/Home_Button.png", 1681, 79, 283, 101, command=open_home)

def open_coast_2():
    create_background("images/Coast_2.png", 1920, 1080)
    create_button("images/Back_Button.png", 1466, 79, 283, 101, command=open_coast)
    create_button("images/Home_Button.png", 1681, 79, 283, 101, command=open_home)

def open_coast_3():
    create_background("images/Coast_3.png", 1920, 1080)
    create_button("images/Back_Button.png", 1466, 79, 283, 101, command=open_coast)
    create_button("images/Home_Button.png", 1681, 79, 283, 101, command=open_home)

def open_coast_4():
    create_background("images/Coast_4.png", 1920, 1080)
    create_button("images/Back_Button.png", 1466, 79, 283, 101, command=open_coast)
    create_button("images/Home_Button.png", 1681, 79, 283, 101, command=open_home)

def open_valley():
    create_background("images/Valley_Home.png", 1920, 1080)
    create_button("images/Home_Button.png", 1681, 79, 283, 101, command=open_home)
    create_button("images/Valley_Silver_Falls_Button.png", 596, 177, 1688, 286, command=open_valley_1)
    create_button("images/Valley_McKenzie_Button.png", 597, 396, 1688, 286, command=open_valley_2)
    create_button("images/Valley_TableRocks_Button.png", 596, 617, 1688, 286, command=open_valley_3)
    create_button("images/Valley_Bird_Alliance_Button.png", 595, 839, 1688, 286, command=open_valley_4)

def open_valley_1():
    create_background("images/Valley_1.png", 1920, 1080)
    create_button("images/Back_Button.png", 1466, 79, 283, 101, command=open_valley)
    create_button("images/Home_Button.png", 1681, 79, 283, 101, command=open_home)

def open_valley_2():
    create_background("images/Valley_2.png", 1920, 1080)
    create_button("images/Back_Button.png", 1466, 79, 283, 101, command=open_valley)
    create_button("images/Home_Button.png", 1681, 79, 283, 101, command=open_home)

def open_valley_3():
    create_background("images/Valley_3.png", 1920, 1080)
    create_button("images/Back_Button.png", 1466, 79, 283, 101, command=open_valley)
    create_button("images/Home_Button.png", 1681, 79, 283, 101, command=open_home)  

def open_valley_4():
    create_background("images/Valley_4.png", 1920, 1080)
    create_button("images/Back_Button.png", 1466, 79, 283, 101, command=open_valley)
    create_button("images/Home_Button.png", 1681, 79, 283, 101, command=open_home)

open_home()

root.mainloop()
