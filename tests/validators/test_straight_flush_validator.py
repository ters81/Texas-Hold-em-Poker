import unittest

from poker.card import Card
from poker.validators import StraightFlushValidator


class StraightFlushValidatorTest(unittest.TestCase):
    def test_determines_that_there_are_not_five_consecutive_cards_with_the_same_suit(self):
        cards = [
            Card(rank='7', suit='Diamonds'),
            Card(rank='8', suit='Diamonds'),
            Card(rank='9', suit='Diamonds'),
            Card(rank='10', suit='Diamonds'),
            Card(rank='Jack', suit='Hearts'),
            Card(rank='King', suit='Diamonds'),
            Card(rank='Ace', suit='Clubs'),
        ]

        validator = StraightFlushValidator(cards=cards)

        self.assertEqual(
            validator.is_valid(),
            False
        )

    def test_determines_that_there_are_five_consecutive_cards_with_the_same_suit(self):
        cards = [
            Card(rank='7', suit='Diamonds'),
            Card(rank='8', suit='Diamonds'),
            Card(rank='9', suit='Diamonds'),
            Card(rank='10', suit='Diamonds'),
            Card(rank='Jack', suit='Diamonds'),
            Card(rank='King', suit='Diamonds'),
            Card(rank='Ace', suit='Clubs'),
        ]

        validator = StraightFlushValidator(cards=cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_determines_that_there_are_five_consecutive_cards_with_the_same_suit(self):
        seven_of_diamonds = Card(rank='7', suit='Diamonds')
        eight_of_diamonds = Card(rank='8', suit='Diamonds')
        nine_of_diamonds = Card(rank='9', suit='Diamonds')
        ten_of_diamonds = Card(rank='10', suit='Diamonds')
        jack_of_diamonds = Card(rank='Jack', suit='Diamonds')

        cards = [
            seven_of_diamonds,
            eight_of_diamonds,
            nine_of_diamonds,
            ten_of_diamonds,
            jack_of_diamonds,
            Card(rank='King', suit='Diamonds'),
            Card(rank='Ace', suit='Clubs'),
        ]

        validator = StraightFlushValidator(cards=cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                seven_of_diamonds,
                eight_of_diamonds,
                nine_of_diamonds,
                ten_of_diamonds,
                jack_of_diamonds
            ]
        )