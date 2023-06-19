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
        Tworzy menu gry.
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
        Aktualizuje wygląd planszy gry na podstawie stanu komórek.
        """
        for i in range(self.game.height):
            for j in range(self.game.width):
                state = self.game.board[i][j]
                color = "white" if state == 0 else "black"
                self.board_buttons[i][j].configure(bg=color)


    def toggle_cell(self, i, j):
        """
        Przełącza stan komórki o określonych współrzędnych (i, j).
        """
        state = self.game.board[i][j]
        self.game.board[i][j] = 0 if state == 1 else 1
        self.update_board()


    def randomize_board(self):
        """
        Losowo ustawia stan komórek na planszy.
        """
        self.game.randomize_board()
        self.update_board()


    def start_game(self):
        """
        Rozpoczyna grę, jeśli jeszcze nie jest uruchomiona.
        """
        if not self.game.running:
            self.game.running = True
            self.game_loop()


    def stop_game(self):
        """
        Zatrzymuje działanie gry.
        """
        self.game.running = False


    def game_loop(self):
        """
        Pętla główna gry, która aktualizuje planszę i wywołuje samą siebie w odpowiednich odstępach czasu.
        """
        if self.game.running:
            self.game.update()
            self.update_board()
            self.root.after(1000, self.game_loop)


    def drag(self, event, i, j):
        """
        Obsługuje zdarzenie przeciągania (drag) komórki o określonych współrzędnych (i, j).
        """
        print(event, i, j)
