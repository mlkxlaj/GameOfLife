import random


class GameController:
    def __init__(self, width, height):
        """
        Inicjalizuje klasę GameController.

        Parametry:
            width (int): Szerokość planszy.
            height (int): Wysokość planszy.
        """
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.next_board = [[0] * width for _ in range(height)]
        self.running = False


def randomize_board(self):
    """
    Losowo ustawia stany komórek na planszy.
    """
    for i in range(self.height):
        for j in range(self.width):
            self.board[i][j] = random.randint(0, 1)


def update(self):
    """
    Aktualizuje stan planszy na podstawie zasad Gry w życie.
    """
    for i in range(self.height):
        for j in range(self.width):
            self.next_board[i][j] = self.get_next_state(i, j)
    self.board, self.next_board = self.next_board, self.board


def get_next_state(self, i, j):
    """
    Zwraca stan komórki (żywa lub martwa) na podstawie jej sąsiadów.
    """
    live_neighbors = self.count_live_neighbors(i, j)
    if self.board[i][j] == 1:
        if live_neighbors < 2 or live_neighbors > 3:
            return 0
        else:
            return 1
    else:
        if live_neighbors == 3:
            return 1
        else:
            return 0


def count_live_neighbors(self, i, j):
    """
    Liczy liczbę żywych sąsiadów dla komórki o współrzędnych (i, j).
    """
    count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            ni = (i + dx + self.height) % self.height
            nj = (j + dy + self.width) % self.width
            count += self.board[ni][nj]
    count -= self.board[i][j]
    return count
