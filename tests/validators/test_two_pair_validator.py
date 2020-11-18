
import unittest

from poker.card import Card
from poker.validators import TwoPairValidator

class TwoPairValidatorTest(unittest.TestCase):
    def setUp(self):
        self.eight_of_clubs = Card(rank='8', suit='Clubs')
        self.eight_of_diamonds = Card(rank='8', suit='Diamonds')
        self.ten_of_clubs = Card(rank='10', suit='Clubs')
        self.ten_of_spades = Card(rank='10', suit='Spades')
        self.king_of_spades = Card(rank='King', suit='Spades')

        self.cards = [
            self.eight_of_clubs,
            self.eight_of_diamonds,
            self.ten_of_clubs,
            self.ten_of_spades,
            self.king_of_spades
        ]

    def test_validates_that_cards_have_at_least_two_pairs_of_same_rank(self):
        validator = TwoPairValidator(cards=self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_collection_of_cards_that_have_pairs(self):
        validator = TwoPairValidator(cards=self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.eight_of_clubs,
                self.eight_of_diamonds,
                self.ten_of_clubs,
                self.ten_of_spades
            ]
        )
