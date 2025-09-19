import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

root = tk.Tk()

canvas = tk.Canvas(root, bg="white")

v_scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview, width=0)
v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

h_scrollbar = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=canvas.xview, width=0)
h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

canvas.config(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

path = os.path.dirname(__file__)
start_image = os.path.join(path, 'rfid_main.jpg')
image = Image.open(start_image)
image = image.resize((1920, 1080))
image = ImageTk.PhotoImage(image)
canvas.create_image((0, 0), anchor="nw", image=image)

canvas.config(scrollregion=canvas.bbox(tk.ALL))
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

def _on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

canvas.bind_all("<MouseWheel>", _on_mousewheel)

root.mainloop()
