from abc import ABC


class Game(ABC):
    def init_game(self):
        pass

    def play_game(self):
        pass

    def end_game(self):
        pass

    def play(self):
        self.init_game()
        self.play_game()
        self.end_game()


class Chess(Game):
    def init_game(self):
        print("Initializing chess game...")

    def play_game(self):
        print("Playing chess game...")

    def end_game(self):
        print("Chess game ended.")

    def play(self):
        super().play()


class Football(Game):
    def init_game(self):
        print("Initializing football game...")

    def play_game(self):
        print("Playing football game...")

    def end_game(self):
        print("Football game ended.")

    def play(self):
        super().play()



if __name__ == '__main__':
    chess = Chess()
    football = Football()

    chess.play()
    print()
    football.play()