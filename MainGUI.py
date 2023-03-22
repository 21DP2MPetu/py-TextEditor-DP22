import tkinter as tk
from tkinter import filedialog

class GUI:

    def __init__(self, root):
    # Attributes
        self.root = root
        self.root.state("zoomed")
        self.root.title("Text Editor: DEMO")

    # Frames

        # Side Frame hierarchy

        side_frame = tk.Frame(master=self.root, height=1080, width=1980)
        side_frame.pack(side=tk.LEFT, fill=tk.Y)

        side_frame_01 = tk.Frame(master=side_frame)
        side_frame_01.pack()

        # Main Frame hierarchy

        main_frame = tk.Frame(master=self.root, height=1080, width=1980)
        main_frame.pack(side=tk.RIGHT, fill=tk.Y)

    # Buttons

        button_open = tk.Button(text="Open File", master=side_frame_01)
        button_open.pack()

        button_new = tk.Button(text="New File", master=side_frame_01)
        button_new.pack()

        button_save = tk.Button(text="Save File", master=side_frame_01)
        button_save.pack()

    # TextArea

        textarea = tk.Text(master=main_frame, width=1980, height=1080)

    # Event Handlers

        def button_open_h(event):
            file_path = filedialog.askopenfilename()
        button_open.bind("<Button-1>", button_open_h)

        def button_new_h(event):
            textarea.pack(fill=tk.Y, side=tk.RIGHT)
        button_new.bind("<Button-1>", button_new_h)

        def button_save_h(event):
            file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        button_save.bind("<Button-1>", button_save_h)

    def removethis(self):
        self.frame.destroy()
