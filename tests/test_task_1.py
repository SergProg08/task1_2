import unittest

from task_1 import get_score

class Test_task_1(unittest.TestCase):

    def setUp(self):
        self.game_stamps = [
            {"offset": 0, "score": {"home": 0, "away": 0}},
            {"offset": 150, "score": {"home": 1, "away": 0}},
            {"offset": 300, "score": {"home": 1, "away": 1}},
            {"offset": 500, "score": {"home": 2, "away": 1}},
        ]

    def test_exact_offset(self):
        home, away = get_score(self.game_stamps, 300)
        self.assertEqual((home, away), (1, 1))

    def test_between_offsets(self):
        home, away = get_score(self.game_stamps, 200)
        self.assertEqual((home, away), (1, 0))

    def test_before_first_offset(self):
        home, away = get_score(self.game_stamps, -5)
        self.assertEqual((home, away), (0, 0))

    def test_after_last_offset(self):
        home, away = get_score(self.game_stamps, 600)
        self.assertEqual((home, away), (2, 1))

    def test_exact_zero_offset(self):
        home, away = get_score(self.game_stamps, 0)
        self.assertEqual((home, away), (0, 0))

    def test_empty_game_stamps(self):
        home, away = get_score([], 10)
        self.assertEqual((home, away), (0, 0))

    def test_edge_case_single_stamp(self):
        single_stamp = [{"offset": 0, "score": {"home": 0, "away": 0}}]
        home, away = get_score(single_stamp, 10)
        self.assertEqual((home, away), (0, 0))

    
if __name__ == '__main__':
    unittest.main()