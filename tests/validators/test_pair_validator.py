import unittest

from poker.card import Card
from poker.validators import PairValidator

class PairValidatorTest(unittest.TestCase):
    def test_validates_that_cards_have_exectly_one_pair(self):
        cards = [
            Card(rank='8', suit='Diamonds'),
            Card(rank='8', suit='Clubs')
        ]

        validator = PairValidator(cards=cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_pair_from_card_collection(self):
        ten_of_spades = Card(rank='10', suit='Spades')
        ten_of_clubs = Card(rank='10', suit='Clubs')

        cards = [
            Card(rank='3', suit='Hearts'),
            Card(rank='8', suit='Diamonds'),
            ten_of_spades,
            ten_of_clubs,
            Card(rank='Queen', suit='Spades')
        ]

        validator = PairValidator(cards=cards)

        self.assertEqual(
            validator.valid_cards(),
            [ten_of_spades, ten_of_clubs]
        )

