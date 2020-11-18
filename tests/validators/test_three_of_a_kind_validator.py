
import unittest

from poker.card import Card
from poker.validators import ThreeOfAKindValidator

class ThreeOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):
        self.eight_of_clubs = Card(rank='8', suit='Clubs')
        self.eight_of_diamonds = Card(rank='8', suit='Diamonds')
        self.eight_of_spades = Card(rank='8', suit='Spades')
        ten = Card(rank='10', suit='Clubs')
        king = Card(rank='King', suit='Spades')

        self.cards = [
            self.eight_of_clubs,
            self.eight_of_diamonds,
            self.eight_of_spades,
            ten,
            king
        ]

    def test_validates_that_cards_have_exactly_three_of_the_same_rank(self):
        validator = ThreeOfAKindValidator(cards=self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_three_of_a_kind_cards_from_card_collection(self):
        validator = ThreeOfAKindValidator(cards=self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.eight_of_clubs,
                self.eight_of_diamonds,
                self.eight_of_spades
            ]
        )

