import random


class GameController:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.next_board = [[0] * width for _ in range(height)]
        self.running = False

