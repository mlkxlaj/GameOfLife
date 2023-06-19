"""
To jest główna klasa odpowiedzialna za uruchomienie gry.

Program rozpoczyna się tworzeniem instancji klasy StartScreen i uruchamianiem jej głównej pętli zdarzeń.

Sposób użycia:
    Uruchom ten skrypt, aby uruchomić program. Użytkownik bedzie przywitany 2 okienkami opcji w ktorych bedzie mogł wpisać rozmiar planszy i zatwierdzić.

    Nastepnie gracze moze pomalowac w dowolnym miejscu plansze na ktorej bedzie rozgrywała się gra.

    Aby uruchomić program należy w górnym lewym rogu najechac na menu i kliknac przycisk start.

    W menu są też możliwosci zastopowania, losowo pomalowania planszy oraz zamknięcia okienka i programu.

Autor: Mikolaj Kowaszewicz, Jakub Malewicz
"""

from StartScreen import *

if __name__ == "__main__":
    start_screen = StartScreen()  # Tworzenie instancji klasy StartScreen
    start_screen.root.mainloop()  # Uruchomienie głównej pętli zdarzeń okna tkinter
