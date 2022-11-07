import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_top1(self):
        self.assertTrue(self.statistics.top(1)[0].name == "Gretzky")
    def test_top3(self):
        self.assertTrue(self.statistics.top(1,3)[0].name == "Gretzky")
    def test_top2(self):
        self.assertTrue(self.statistics.top(1,2)[0].name == "Lemieux")
    def test_top4(self):
        self.assertTrue(self.statistics.top(1,10)[0].name == "Gretzky")

    def test_search(self):
        player1 = self.statistics.search("Gretzky")
        self.assertTrue(player1.name == "Gretzky")

        player2 = self.statistics.search("dippaa")
        self.assertTrue(player2 == None)

    def test_team(self):
        players = self.statistics.team("PIT")
        self.assertAlmostEqual(len(players), 1)
        self.assertTrue(players[0].name == "Lemieux")
