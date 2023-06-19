import tkinter as tk
from GameController import *


class Game:
    def __init__(self, root, height, width):
        self.root = root
        self.root.title("Gra w życie")

        self.game = GameController(width, height)
        self.board_buttons = []

        self.create_menu()
        self.create_board()


