
import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def ShowWindow():

        window = tk.Tk()
        window.withdraw()
        window.title("Text Editor: DEMO")

        # window.attributes("-fullscreen", True)
        window.state("zoomed")

        # for i in range(1):
        #     for j in range(1):
        #         frame = tk.Frame(
        #             master=window,
        #             relief=tk.RAISED,
        #             borderwidth=1
        #         )
        #         frame.grid(row=i, column=j)

        frame_01 = tk.Frame(master=window)
        frame_01.pack(side=tk.LEFT)

        frame_02 = tk.Frame(master=window)
        frame_02.pack(side=tk.RIGHT)

        button_open = tk.Button(text="Open File", master=frame_01)
        button_open.pack()

        button_new = tk.Button(text="New File", master=frame_01)
        button_new.pack()

        button_save = tk.Button(text="Save File", master=frame_01)
        button_save.pack()

        def button_open_h(event):
            file_path = filedialog.askopenfilename()
        button_open.bind("<Button-1>", button_open_h)

        def button_new_h(event):
            file_path = filedialog.askopenfilename()
        button_new.bind("<Button-1>", button_new_h)

        def button_save_h(event):
            file_path = filedialog.askopenfilename()
        button_save.bind("<Button-1>", button_save_h)


        window.mainloop()
