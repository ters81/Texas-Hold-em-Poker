import unittest

from poker.card import Card
from poker.validators import StraightValidator


class StraightValidatorTest(unittest.TestCase):
    def setUp(self):
        two_of_diamonds = Card(rank='2', suit='Diamonds')
        six_of_diamonds = Card(rank='6', suit='Diamonds')
        self.seven_of_clubs = Card(rank='7', suit='Clubs')
        self.eight_of_spades = Card(rank='8', suit='Spades')
        self.nine_of_spades = Card(rank='9', suit='Spades')
        self.ten_of_clubs = Card(rank='10', suit='Clubs')
        self.jack_of_spades = Card(rank='Jack', suit='Spades')

        self.cards = [
            two_of_diamonds,
            six_of_diamonds,
            self.seven_of_clubs,
            self.eight_of_spades,
            self.nine_of_spades,
            self.ten_of_clubs,
            self.jack_of_spades
        ]

    def test_determines_if_there_are_five_cards_in_a_row(self):
        validator = StraightValidator(cards=self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_does_not_deem_two_consecutive_cards_as_straight(self):
        cards = [
            Card(rank="6", suit="Hearts"),
            Card(rank="7", suit="Diamonds")
        ]

        validator = StraightValidator(cards=cards)

        self.assertEqual(
            validator.is_valid(),
            False
        )

    def test_returns_five_highest_cards_in_a_row(self):
        validator = StraightValidator(cards=self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.seven_of_clubs,
                self.eight_of_spades,
                self.nine_of_spades,
                self.ten_of_clubs,
                self.jack_of_spades
            ]
        )
