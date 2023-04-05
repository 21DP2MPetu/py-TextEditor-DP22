import tkinter as tk
import os
from tkinter import filedialog

GLOBAL_COUNTER = 0
PATH_ARRAY = []

class GUI:
    
    def __init__(self, root):
    # Attributes
        self.root = root
        # self.root.state("zoomed")
        self.root.geometry("750x250")
        self.root.title("Tt-Edit: BETA")
        self.root.configure(bg="#e0e0e0")

    #  Getting screen sizes
        SCREEN_HEIGHT = self.root.winfo_screenheight()
        SCREEN_WIDTH = self.root.winfo_screenwidth()

    # Event Handlers

        def GetPathToOpen():
            path = filedialog.askopenfilename()
            if not path:
                return
            return path

        # Open file system

        def button_open_h():
            global GLOBAL_COUNTER
            global PATH_ARRAY
            file_path = GetPathToOpen()
            PATH_ARRAY.append(file_path)
            file_text = open(file_path, "r")
            textarea.delete("1.0", tk.END)
            create_area(file_text)
            file_text.close()
            file_name = os.path.basename(file_path) # os.path.basename()
            tab = create_tab(file_name, GLOBAL_COUNTER)
            GLOBAL_COUNTER += 1
            # self.root.title(file_name)

        # New file system

        def button_new_h():
            global GLOBAL_COUNTER
            create_area()
            create_tab("New file", GLOBAL_COUNTER)
            GLOBAL_COUNTER += 1
            # self.root.title("New file")

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

        def create_tab(tab_name, position):
            
            global PATH_ARRAY
    
            label = tk.Label(master=tab_frame, text=tab_name, foreground="black", background="#d7dbe0", width=20)
            label.grid(row=0, column=position, padx=1)
            def label_close(event):
                if label.cget("text") == "New file":
                    label.destroy()
                for i in range(len(PATH_ARRAY)):
                    if label.cget("text") == os.path.basename(PATH_ARRAY[i]):
                        label.destroy()
                        del PATH_ARRAY[i]
                        textarea.delete("1.0", tk.END)

            label.bind("<Button-3>", label_close)

        # Create Area

        def create_area(file_text=None):
            if file_text != None:
                textarea.insert(tk.END, file_text.read())
            else:
                textarea.delete("1.0", tk.END)


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

        textarea = tk.Text(master=area_frame, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        textarea.pack()

    def removethis(self):
        self.frame.destroy()