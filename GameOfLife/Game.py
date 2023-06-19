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

    def create_menu(self):
        """
        Tworzenie paska menu

        Pasek menu zawiera opcje rozpoczęcia, zatrzymania, losowego ustawienia planszy oraz zamknięcia aplikacji.
        """
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        game_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Gra", menu=game_menu)
        game_menu.add_command(label="Start", command=self.start_game)
        game_menu.add_command(label="Stop", command=self.stop_game)
        game_menu.add_separator()
        game_menu.add_command(label="Losuj planszę", command=self.randomize_board)
        game_menu.add_separator()
        game_menu.add_command(label="Zamknij", command=self.root.quit)

    def create_board(self):
        """
        Tworzy planszę gry.

        Plansza gry to siatka przycisków, gdzie każdy przycisk reprezentuje komórkę w grze w życie.
        """
        board_frame = tk.Frame(self.root)
        board_frame.pack()

        for i in range(self.game.height):
            row = []
            for j in range(self.game.width):
                button = tk.Button(board_frame, width=2, relief="solid",
                                   command=lambda i=i, j=j: self.toggle_cell(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.board_buttons.append(row)

    def update_board(self):
        """
        Aktualizuje kolory przycisków na planszy gry na podstawie aktualnego stanu komórek.
        """
        for i in range(self.game.height):
            for j in range(self.game.width):
                state = self.game.board[i][j]
                color = "white" if state == 0 else "black"
                self.board_buttons[i][j].configure(bg=color)

    def toggle_cell(self, i, j):
        """
        Przełącza stan komórki, gdy kliknięty zostaje odpowiadający jej przycisk.

        Parametry:
            i (int): Indeks wiersza komórki.
            j (int): Indeks kolumny komórki.
        """
        state = self.game.board[i][j]
        self.game.board[i][j] = 0 if state == 1 else 1
        self.update_board()

    def randomize_board(self):
        """
        Losowo ustawia stany komórek na planszy gry.
        """
        self.game.randomize_board()
        self.update_board()

    def start_game(self):
        """
        Rozpoczyna główną pętlę gry, która ciągle aktualizuje stany komórek i planszę gry.
        """
        if not self.game.running:
            self.game.running = True
