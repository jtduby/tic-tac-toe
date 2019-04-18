from os import system
import time

class TTT:
    def __init__(self):
        self._board = [None for _ in range(9)]

    def __getitem__(self, space):
        return self._board[space - 1]

    def __setitem__(self, space, piece):
        if self[space]:
            raise IndexError("Space not empty")
        self._board[space - 1] = piece

    def __str__(self):
        template = " {0} | {1} | {2} \n"\
                   "-----------\n"\
                   " {3} | {4} | {5} \n"\
                   "-----------\n"\
                   " {6} | {7} | {8} \n"
        return template.format(*[s if s else str(i+1) for i,s in enumerate(self._board)])

    def _reset(self):
        self.__init__()

    def game_won(self):
        win_scenarios = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                         [1, 4, 7], [2, 5, 8], [3, 6, 9],
                         [1, 5, 9], [3, 5, 7]
        ]
        for s in win_scenarios:
            if self[s[0]]:
                a, b, c = s
                if self[a] == self[b] == self[c]:
                    return True
        return False

    def stalemate(self):
        if self.game_won():
            return False
        for space in self._board:
            if not space:
                return False
        return True


class Game:
    def __init__(self):
        self._ttt = TTT()
        self._curr_player = ['X', 'O']
        self._playing = True
        self._play()

    def _play(self):
        while self._playing:
            _ = system('clear')
            print(str(self._ttt))
            print
            s = input("{0} to play:".format(self._curr_player[0]))
            try:
                self._ttt[int(s)] = self._curr_player[0]
            except (IndexError, TypeError, ValueError):
                print("Ya can't move there ya dingus")
                time.sleep(3)
                continue
            self._curr_player.reverse()
            if self._ttt.game_won():
                print("{0} won the game!".format(self._curr_player[1]))
                self._playing = False
            if self._ttt.stalemate():
                print("Stalemate. Congratulations, you both suck.")
                self._playing = False


if __name__ == '__main__':
    game = Game()
