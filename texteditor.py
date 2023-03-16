
import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def ShowWindow():

    # Window/Window title

        window = tk.Tk()
        window.withdraw()
        window.title("Text Editor: DEMO")

    # Window Size

        # window.attributes("-fullscreen", True)
        window.state("zoomed")

    # Frames

        frame = tk.Frame(master=window, bg="red", width=180, height=1080)
        frame.pack(side=tk.LEFT, fill=tk.Y)

        frame_01 = tk.Frame(master=window, bg="blue", height=1080, width=1800)
        frame_01.pack(side=tk.RIGHT, fill=tk.Y)

    # Buttons

        button_open = tk.Button(text="Open File", master=frame)
        button_open.pack()

        button_new = tk.Button(text="New File", master=frame)
        button_new.pack()

        button_save = tk.Button(text="Save File", master=frame)
        button_save.pack()

    # TextArea

        textarea = tk.Text(master=frame_01, width=200, height=50)
        textarea.pack(fill=tk.Y, side=tk.RIGHT)

    # Event Handlers

        # def button_open_h(event):
        #     file_path = filedialog.askopenfilename()
        # button_open.bind("<Button-1>", button_open_h)

        # def button_new_h(event):
        #     file_path = filedialog.askopenfilename()
        # button_new.bind("<Button-1>", button_new_h)

        # def button_save_h(event):
        #     file_path = filedialog.askopenfilename()
        # button_save.bind("<Button-1>", button_save_h)

    #  Close Window

        window.mainloop()
