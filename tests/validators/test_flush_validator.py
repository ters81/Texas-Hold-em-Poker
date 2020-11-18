import unittest

from poker.card import Card
from poker.validators import FlushValidator


class FlushValidatorTest(unittest.TestCase):
    def setUp(self):
        self.two_of_diamonds = Card(rank='2', suit='Diamonds')
        self.three_of_diamonds = Card(rank='3', suit='Diamonds')
        self.five_of_diamonds = Card(rank='5', suit='Diamonds')
        self.seven_of_diamonds = Card(rank='7', suit='Diamonds')
        self.eight_of_diamonds = Card(rank='8', suit='Diamonds')
        self.queen_of_diamonds = Card(rank='Queen', suit='Diamonds')

        self.cards = [
            self.two_of_diamonds,
            self.three_of_diamonds,
            self.five_of_diamonds,
            self.seven_of_diamonds,
            self.eight_of_diamonds,
            Card(rank='Jack', suit='Hearts'),
            self.queen_of_diamonds
        ]

    def test_validates_that_five_cards_of_same_suit_exist_in_collections(self):
        validator = FlushValidator(cards=self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_the_five_highest_cards_with_the_same_suit(self):
        validator = FlushValidator(cards=self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.three_of_diamonds,
                self.five_of_diamonds,
                self.seven_of_diamonds,
                self.eight_of_diamonds,
                self.queen_of_diamonds
            ]
)