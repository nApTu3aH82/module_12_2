# -*- coding: utf-8 -*-

from runner_and_tournament import Runner, Tournament
import unittest
from pprint import pprint




class TournamentTest(unittest.TestCase):

    def setUp(self):
        self.runner1 = Runner('Усейн', speed = 10)
        self.runner2 = Runner('Андрей', speed=9)
        self.runner3 = Runner('Ник', speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def test_1(self):
        start1 = Tournament(90, self.runner1, self.runner3)
        result = start1.start()
        TournamentTest.all_results['1'] = {place: str(runner) for place, runner in result.items()}
        self.assertTrue(result[len(result)] == 'Ник')

    def test_2(self):
        start2 = Tournament(90, self.runner2, self.runner3)
        result = start2.start()
        TournamentTest.all_results['2'] = {place: str(runner) for place, runner in result.items()}
        self.assertTrue(result[len(result)] == 'Ник')

    def test_3(self):
        start3 = Tournament(90, self.runner1, self.runner2, self.runner3)
        result = start3.start()
        TournamentTest.all_results['3'] = {place: str(runner) for place, runner in result.items()}
        self.assertTrue(result[len(result)] == 'Ник')


if __name__ == '__main__':
    TournamentTest.main()
