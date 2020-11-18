
import unittest

from poker.card import Card
from poker.validators import FullHouseValidator


class FullHouseValidatorTest(unittest.TestCase):
    def setUp(self):
        self.eight_of_diamonds = Card(rank='8', suit='Diamonds')
        self.eight_of_clubs = Card(rank='8', suit='Clubs')
        self.ten_of_spades = Card(rank='10', suit='Spades')
        self.ten_of_diamonds = Card(rank='10', suit='Diamonds')
        self.ten_of_clubs = Card(rank='10', suit='Clubs')

        self.cards = [
            self.eight_of_clubs,
            self.eight_of_diamonds,
            self.ten_of_clubs,
            self.ten_of_diamonds,
            Card(rank='5', suit='Clubs'),
            self.ten_of_spades,
            Card(rank='Queen', suit='Hearts')
        ]

    def test_validates_that_cards_have_two_of_the_same_rank_and_three_of_another_rank(self):
        validator = FullHouseValidator(cards=self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_collection_of_two_cards_of_the_same_rank_and_three_cards_of_the_same_rank(self):
        validator = FullHouseValidator(cards=self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.eight_of_clubs,
                self.eight_of_diamonds,
                self.ten_of_clubs,
                self.ten_of_diamonds,
                self.ten_of_spades
            ]
        )