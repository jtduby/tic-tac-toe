import unittest

from ttt import TTT

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.game = TTT()

    def test_make_empty_board(self):
        expected_str = " 1 | 2 | 3 \n"\
                       "-----------\n"\
                       " 4 | 5 | 6 \n"\
                       "-----------\n"\
                       " 7 | 8 | 9 \n"
        self.assertEqual(str(self.game), expected_str)

    def test_place_piece(self):
        expected_str = " 1 | 2 | 3 \n"\
                       "-----------\n"\
                       " 4 | X | 6 \n"\
                       "-----------\n"\
                       " 7 | 8 | 9 \n"
        self.game[5] = 'X'
        self.assertEqual(str(self.game), expected_str)

    def test_show_piece_by_index(self):
        self.game[5] = 'X'
        self.game[7] = 'O'
        self.assertEqual('X', self.game[5])
        self.assertEqual('O', self.game[7])


class TestRuleViolations(unittest.TestCase):
    def setUp(self):
        self.game = TTT()

    def test_occupied_space(self):
        self.game[1] = 'X'
        with self.assertRaises(IndexError):
            self.game[1] = 'O'

class TestGameOver(unittest.TestCase):
    def setUp(self):
        self.game = TTT()

    def test_won_across(self):
        for i in range(1, 4):
            self.game[i] = 'X'
        self.assertTrue(self.game.game_won())
        self.game._reset()
        for i in range(4, 7):
            self.game[i] = 'X'
        self.assertTrue(self.game.game_won())
        self.game._reset()
        for i in range(7, 10):
            self.game[i] = 'X'
        self.assertTrue(self.game.game_won())

    def test_won_down(self):
        for i in [1, 4, 7]:
            self.game[i] = 'X'
        self.assertTrue(self.game.game_won())
        self.game._reset()
        for i in [2, 5, 8]:
            self.game[i] = 'X'
        self.assertTrue(self.game.game_won())
        self.game._reset()
        for i in [3, 6, 9]:
            self.game[i] = 'X'
        self.assertTrue(self.game.game_won())
        self.game._reset()

    def test_won_across(self):
        for i in [1, 5, 9]:
            self.game[i] = 'X'
        self.assertTrue(self.game.game_won())
        self.game._reset()
        for i in [3, 5, 7]:
            self.game[i] = 'X'
        self.assertTrue(self.game.game_won())
        self.game._reset()

    def test_stalemate(self):
        moves = ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'O']
        for i, m in enumerate(moves):
            self.game[i+1] = m
        self.assertTrue(self.game.stalemate())


if __name__ == '__main__':
    unittest.main()
