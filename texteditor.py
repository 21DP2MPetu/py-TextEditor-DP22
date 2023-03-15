
import tkinter as tk

class TextEditor:
    def ShowComm():
        window = tk.Tk()
        window.title("Text Editor: DEMO")
        window.rowconfigure(0, minsize=800, weight=1)
        window.columnconfigure(1, minsize=800, weight=1)
        window.mainloop()

# https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter