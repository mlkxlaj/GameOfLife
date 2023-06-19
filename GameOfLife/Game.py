import tkinter as tk
from GameController import *


class Game:
    def __init__(self, root, height, width):
        """
        Inicjalizacja klasy game.

        Parametry:
            root (tk.Tk): Główne okno aplikacji.
            height (int): Wysokość planszy gry.
            width (int): Szerokość planszy gry.
        """
        self.root = root
        self.root.title("Gra w życie")

        self.game = GameController(width, height)
        self.board_buttons = []

        self.create_menu()
        self.create_board()

