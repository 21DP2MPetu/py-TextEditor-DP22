
import tkinter as tk
from tkinter import filedialog

class TextEditor:

    def ShowWindow():

    # Window/Window title

        window = tk.Tk()
        # window.withdraw()
        window.title("Text Editor: DEMO")

    # Getting Screen Sizes

        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

    # Window Size

        # window.attributes("-fullscreen", True)
        window.state("zoomed")

    # Frames

        side_frame = tk.Frame(master=window, bg="red", height=screen_height)
        side_frame.pack(side=tk.LEFT, fill=tk.Y)

        side_frame_01 = tk.Frame(master=side_frame, bg="green")
        side_frame_01.pack()

        # Main Frame hierarchy

        main_frame = tk.Frame(master=window, bg="blue", height=screen_height, width=screen_width)
        main_frame.pack(side=tk.RIGHT, fill=tk.Y)

    # Buttons

        button_open = tk.Button(text="Open File", master=side_frame_01)
        # button_open.pack(fill=tk.Y, side=tk.LEFT)
        button_open.pack()

        button_new = tk.Button(text="New File", master=side_frame_01)
        # button_new.pack(fill=tk.Y, side=tk.LEFT)
        button_new.pack()

        button_save = tk.Button(text="Save File", master=side_frame_01)
        # button_save.pack(fill=tk.Y, side=tk.LEFT)
        button_save.pack()

    # TextArea

        textarea = tk.Text(master=main_frame, width=screen_width , height=screen_height)
        textarea.pack(fill=tk.Y, side=tk.RIGHT)

    # Event Handlers

        def button_open_h(event):
            file_path = filedialog.askopenfilename()
        button_open.bind("<Button-1>", button_open_h)

        def button_new_h(event):
            file_path = filedialog.askdirectory(title='Select Folder')
        button_new.bind("<Button-1>", button_new_h)

        def button_save_h(event):
            file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        button_save.bind("<Button-1>", button_save_h)

    #  Close Window

        window.mainloop()
