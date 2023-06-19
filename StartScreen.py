from Game import *
import tkinter as tk


class StartScreen:
    """
    Konstruktor ekranu startowego.
    """
    def __init__(self):
        self.height_entry = None
        self.width_entry = None
        self.root = tk.Tk()
        self.root.title("Ekran startowy")

        self.create_widgets()


def create_widgets(self):
    """
    Tworzy elementy ekranu startowego. Wysokość i szerokość planszy, tytuł, przycisk do rozpoczęcia gry.
    """

    label = tk.Label(self.root, text="Gra w życie")
    label.pack(pady=20)

    height_label = tk.Label(self.root, text="Wysokość planszy:")
    height_label.pack()
    self.height_entry = tk.Entry(self.root)
    self.height_entry.pack()

    width_label = tk.Label(self.root, text="Szerokość planszy:")
    width_label.pack()
    self.width_entry = tk.Entry(self.root)
    self.width_entry.pack()

    start_button = tk.Button(self.root, text="Rozpocznij grę", command=self.start_game)
    start_button.pack(pady=20, padx=100)
