import tkinter as tk

class MainGUI:

    def __init__(self, root):
        self.root = root 
        self.button = tk.Button(self.root, text="Push me", command=self.removethis)
        self.button.pack()
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.label = tk.Label(self.frame, text="I'll be destroyed soon!")
        self.label.pack()

    def removethis(self):
        self.frame.destroy()