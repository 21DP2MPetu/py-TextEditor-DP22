import tkinter as tk
import os
from tkinter import filedialog

class GUI:
    
    def __init__(self, root):
    # Attributes
        self.root = root
        # self.root.state("zoomed")
        self.root.geometry("750x250")
        self.root.title("Text Editor: DEMO")
        self.root.configure(bg="#e0e0e0")

    #  Getting screen sizes
        SCREEN_HEIGHT = self.root.winfo_screenheight()
        SCREEN_WIDTH = self.root.winfo_screenwidth()

    # Event Handlers

        # Open file system

        def button_open_h():
            file_path = filedialog.askopenfilename()
            if not file_path:
                return
            textarea.delete("1.0", tk.END)
            file_text = open(file_path, "r")
            textarea.insert(tk.END, file_text.read())
            file_text.close()
            file_name = os.path.basename(file_path) # os.path.basename()
            create_tab(file_name)
            self.root.title(file_name)

        # New file system

        def button_new_h():
            textarea.delete("1.0", tk.END)
            create_tab("New file")
            self.root.title("New File")

        # Save file system

        def button_save_h():
            file_path = filedialog.asksaveasfilename(defaultextension=".txt")
            if not file_path:
                return
            file_text = open(file_path, mode="w", encoding="utf=8")
            text = textarea.get("1.0", tk.END)
            file_text.write(text)

        # About button handler

        def about_button():
            
            root = tk.Tk()
            root.title("About: Text Editor")
            root.geometry("270x72")

            about0 = tk.Label(root, text="Name: Text Editor: Beta")
            about1 = tk.Label(root, text="Version: Beta")
            about2 = tk.Label(root, text="Year: 2023")
            about0.pack()
            about1.pack()
            about2.pack()

            root.mainloop

        # Create Tab

        def create_tab(tab_name):

            tk.Label(master=tab_frame, text=tab_name, foreground="black", background="#d7dbe0", width=10).grid(row=0, column=0, padx=1)

    # Frames

        # Side Frame hierarchy

        side_frame = tk.Frame(master=self.root)
        side_frame.pack(side=tk.LEFT)

        # Main Frame hierarchy (Tabs, Area)

        main_frame = tk.Frame(master=self.root)
        main_frame.pack()

        # Tabs Frame

        tab_frame = tk.Frame(master=main_frame)
        tab_frame.pack()

        # Area Frame

        area_frame = tk.Frame(master=main_frame)
        area_frame.pack(side=tk.BOTTOM, fill=tk.Y)

    # Buttons

        # Side buttons

        button_open = tk.Button(text="Open File", master=side_frame, width=8, command=button_open_h)
        button_open.grid(row=0, column=0, sticky="W", pady=1)

        button_new = tk.Button(text="New File", master=side_frame, width=8, command=button_new_h)
        button_new.grid(row=1, column=0, sticky="W", pady=1)

        button_save = tk.Button(text="Save File", master=side_frame, width=8, command=button_save_h)
        button_save.grid(row=2, column=0, sticky="W", pady=1)

        button_about = tk.Button(text="About", master=side_frame, width=8, command=about_button)
        button_about.grid(row=3, column=0, sticky="W", pady=1)

    # TextArea

        # Area textarea

        textarea = tk.Text(master=area_frame, width=SCREEN_WIDTH, height=SCREEN_WIDTH)
        textarea.pack()

    # Labels

        # Tabs labels


    def removethis(self):
        self.frame.destroy()