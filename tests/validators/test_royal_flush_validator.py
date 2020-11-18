import unittest

from poker.card import Card
from poker.validators import RoyalFlushValidator


class RoyalFlushValidatorTest(unittest.TestCase):
    def test_validates_that_cards_do_not_have_straight_flush_ending_in_ace(self):
        cards = [
            Card(rank='9', suit='Diamonds'),
            Card(rank='10', suit='Diamonds'),
            Card(rank='Jack', suit='Diamonds'),
            Card(rank='Queen', suit='Diamonds'),
            Card(rank='King', suit='Diamonds'),
            Card(rank='Ace', suit='Clubs')
            ]

        validator = RoyalFlushValidator(cards=cards)

        self.assertEqual(
            validator.is_valid(),
            False
        )

    def test_validates_that_cards_have_straight_flush_ending_in_ace(self):
        cards = [
            Card(rank='2', suit='Spades'),
            Card(rank='10', suit='Diamonds'),
            Card(rank='Jack', suit='Diamonds'),
            Card(rank='Queen', suit='Diamonds'),
            Card(rank='King', suit='Diamonds'),
            Card(rank='Ace', suit='Diamonds'),
            Card(rank='Ace', suit='Clubs')
            ]

        validator = RoyalFlushValidator(cards=cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_five_straight_cards_with_same_rank_ending_in_ace(self):
        cards = [
            Card(rank='2', suit='Spades'),
            Card(rank='10', suit='Diamonds'),
            Card(rank='Jack', suit='Diamonds'),
            Card(rank='Queen', suit='Diamonds'),
            Card(rank='King', suit='Diamonds'),
            Card(rank='Ace', suit='Diamonds'),
            Card(rank='Ace', suit='Clubs')
            ]

        validator = RoyalFlushValidator(cards=cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                Card(rank='10', suit='Diamonds'),
                Card(rank='Jack', suit='Diamonds'),
                Card(rank='Queen', suit='Diamonds'),
                Card(rank='King', suit='Diamonds'),
                Card(rank='Ace', suit='Diamonds')
            ]
        )



