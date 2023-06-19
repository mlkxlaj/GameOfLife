from Game import *
import tkinter as tk


class StartScreen:
    def __init__(self):
        self.height_entry = None
        self.width_entry = None
        self.root = tk.Tk()
        self.root.title("Ekran startowy")

        self.create_widgets()
