import unittest

from poker.hand import Hand
from poker.player import Player
from unittest.mock import MagicMock



class PlayerTest(unittest.TestCase):
    def test_stores_name_and_hand(self):
        hand = Hand(cards=[])
        player = Player(name="Serhii", hand=hand)
        self.assertEqual(player.name, "Serhii")
        self.assertEqual(player.hand, hand)

    def test_figures_out_own_best_hand(self):
        mock_hand = MagicMock()
        mock_hand.best_rank.return_value = "Straight Flush"


        player = Player(name="Serhii", hand=mock_hand)

        self.assertEqual(
            player.best_hand(),
            "Straight Flush"
        )
        mock_hand.best_rank.assert_called()
