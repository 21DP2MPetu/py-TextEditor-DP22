import tkinter as tk
from tkinter import filedialog

class GUI:
    def __init__(self, root):
    # Attributes
        self.root = root
        # self.root.state("zoomed")
        self.root.geometry("750x250")
        self.root.title("Text Editor: DEMO")
        self.root.configure(bg="purple")

    #  Getting screen sizes
        SCREEN_HEIGHT = self.root.winfo_screenheight()
        SCREEN_WIDTH = self.root.winfo_screenwidth()

    # Frames

        # Side Frame hierarchy

        side_frame = tk.Frame(master=self.root, bg="black")
        side_frame.pack(fill=tk.BOTH, expand=True)   
        side_frame.place(width=75)

        # Main Frame hierarchy (Tabs, Area)

        main_frame = tk.Frame(master=self.root, bg="yellow")
        main_frame.pack(fill=tk.BOTH, expand=True)
        main_frame.place()

        # Tabs Frame

        # tab_frame = tk.Frame(master=main_frame, bg="red")
        # tab_frame.grid(row=0, column=0)

        # Area Frame

        # area_frame = tk.Frame(master=main_frame, bg="green")
        # area_frame.grid(row=1, column=0)

    # Buttons

        # Side buttons

        button_open = tk.Button(text="Open File", master=side_frame, width=8)
        button_open.grid(row=0, column=0, sticky="W", pady=1)

        button_new = tk.Button(text="New File", master=side_frame, width=8)
        button_new.grid(row=1, column=0, sticky="W", pady=1)

        button_save = tk.Button(text="Save File", master=side_frame, width=8)
        button_save.grid(row=2, column=0, sticky="W", pady=1)

        button_about = tk.Button(text="About", master=side_frame, width=8)
        button_about.grid(row=3, column=0, sticky="W", pady=1)

    # TextArea

        # Area textarea

        # textarea = tk.Text(master=area_frame, width=1980)
        # textarea.grid(row=0, column=0)

    # Labels

        # Tabs labels

        # label_tab = tk.Label(master=tab_frame, text="Hello, Tkinter", foreground="white", background="black")
        # label_tab.grid(row=0, column=0, sticky="W")

    # Event Handlers

        # Open file system

        # def button_open_h(event):
        #     file_path = filedialog.askopenfilename()
        #     if not file_path:
        #         return
        #     textarea.delete("1.0", tk.END)
        #     file_text = open(file_path, "r")
        #     textarea.insert(tk.END, file_text.read())
        #     file_text.close()
        # button_open.bind("<Button-1>", button_open_h)

        # # New file system

        # def button_new_h(event):
        #     textarea.delete("1.0", tk.END)
        # button_new.bind("<Button-1>", button_new_h)

        # # Save file system

        # def button_save_h(event):
        #     file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        #     if not file_path:
        #         return
        #     file_text = open(file_path, mode="w", encoding="utf=8")
        #     text = textarea.get("1.0", tk.END)
        #     file_text.write(text)

        # button_save.bind("<Button-1>", button_save_h)

        # # About button handler

        # def about_button(event):
            
        #     root = tk.Tk()
        #     root.title("About: Text Editor")
        #     root.geometry("270x72")

        #     about0 = tk.Label(root, text="Name: Text Editor: Canary")
        #     about1 = tk.Label(root, text="Version: Canary")
        #     about2 = tk.Label(root, text="Year: 2023")
        #     about0.pack()
        #     about1.pack()
        #     about2.pack()

        #     root.mainloop

        # button_about.bind("<Button-1>", about_button)

    # def removethis(self):
    #     self.frame.destroy()
