
import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def ShowWindow():

    # Window/Window title

        window = tk.Tk()
        window.title("Text Editor: Dev")
        
    # Window Size(Maximized, NOT Fullscreen)

        # window.attributes("-fullscreen", True)
        window.state("zoomed")

    # Frames

        frame = tk.Frame(master=window, bg="red", width=180, height=1080)
        frame.pack(side=tk.LEFT, fill=tk.Y)

        frame_01 = tk.Frame(master=window, bg="blue", height=1080, width=1800)
        frame_01.pack(side=tk.RIGHT, fill=tk.Y)

    # Buttons

        button_open = tk.Button(text="Open File", master=frame)
        button_open.pack(fill=tk.X)

        button_new = tk.Button(text="New File", master=frame)
        button_new.pack(fill=tk.X)

        button_save = tk.Button(text="Save File", master=frame)
        button_save.pack(fill=tk.X)

        button_about = tk.Button(text="About", master=frame)
        button_about.pack(fill=tk.X)

        #greeting0 = tk.Label(text="About Text Editor:")
        #greeting1 = tk.Label(text="Name: Text Editor: Dev")
        #greeting2 = tk.Label(text="Version: 0.1")
        #greeting0.pack()
        #greeting1.pack()
        #greeting2.pack()

    # TextArea
    
        textarea = tk.Text(master=frame_01, width=200, height=50)
        textarea.pack(fill=tk.Y, side=tk.RIGHT)

    # Event Handlers

        def button_open_h(event):
            file_path = filedialog.askopenfilename()
        button_open.bind("<Button-1>", button_open_h)

        def button_new_h(event):
            file_path = filedialog.askopenfilename()
        button_new.bind("<Button-1>", button_new_h)

        def button_save_h(event):
            file_path = filedialog.askopenfilename()
        button_save.bind("<Button-1>", button_save_h)

        def about_button(event):
            
            root = tk.Tk()
            root.title("About: Text Editor")
            root.geometry("270x72")

            about0 = tk.Label(root, text="Name: TEST(Under Construction)")
            about1 = tk.Label(root, text="Version: Canary")
            about2 = tk.Label(root, text="Year: Redacted")
            about0.pack()
            about1.pack()
            about2.pack()

            root.mainloop

        button_about.bind("<Button-1>", about_button)

    #  Close Window

        window.mainloop()