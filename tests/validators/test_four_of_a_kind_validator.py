import unittest

from poker.card import Card
from poker.validators import FourOfAKindValidator


class FourOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):
        self.eight_of_clubs = Card(rank='8', suit='Clubs')
        self.eight_of_diamonds = Card(rank='8', suit='Diamonds')
        self.eight_of_hearts = Card(rank='8', suit='Hearts')
        self.eight_of_spades = Card(rank='8', suit='Spades')

        self.cards = [
            self.eight_of_clubs,
            self.eight_of_diamonds,
            self.eight_of_hearts,
            self.eight_of_spades,
            Card(rank='10', suit='Hearts'),
            Card(rank='King', suit='Clubs'),
            Card(rank='Ace', suit='Spades')

        ]

    def test_determines_that_four_cards_of_one_rank_are_present(self):
        validator = FourOfAKindValidator(cards=self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_the_four_cards_with_the_same_rank(self):
        validator = FourOfAKindValidator(cards=self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.eight_of_clubs,
                self.eight_of_diamonds,
                self.eight_of_hearts,
                self.eight_of_spades
            ]
        )