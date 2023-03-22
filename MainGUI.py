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
        button_open.pack(fill=tk.X)

        button_new = tk.Button(text="New File", master=side_frame_01)
        button_new.pack(fill=tk.X)

        button_save = tk.Button(text="Save File", master=side_frame_01)
        button_save.pack(fill=tk.X)

        button_about = tk.Button(text="About", master=side_frame_01)
        button_about.pack(fill=tk.X)

    # TextArea

        textarea = tk.Text(master=main_frame, width=1980, height=1080)
        textarea.pack()

    # Event Handlers

        def button_open_h(event):
            file_path = filedialog.askopenfilename()
            textarea.delete("1.0", tk.END)
            file_text = open(file_path, "r")
            textarea.insert(tk.END, file_text.read())
            file_text.close()
        button_open.bind("<Button-1>", button_open_h)

        def button_new_h(event):
            textarea.delete("1.0", tk.END)
        button_new.bind("<Button-1>", button_new_h)

        def button_save_h(event):
            file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        button_save.bind("<Button-1>", button_save_h)

        def about_button(event):
            
            root = tk.Tk()
            root.title("About: Text Editor")
            root.geometry("270x72")

            about0 = tk.Label(root, text="Name: Text Editor: Canary")
            about1 = tk.Label(root, text="Version: Canary")
            about2 = tk.Label(root, text="Year: 2023")
            about0.pack()
            about1.pack()
            about2.pack()

            root.mainloop

        button_about.bind("<Button-1>", about_button)

    def removethis(self):
        self.frame.destroy()
