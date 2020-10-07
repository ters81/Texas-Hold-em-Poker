import unittest
from poker.card import Card
from poker.hand import Hand

class HandTest(unittest.TestCase):

    def test_starts_out_with_no_cards(self):
        hand = Hand()
        self.assertEqual(hand.cards, [])

    def test_receives_and_stores_cards(self):
        ace_of_spades = Card(rank='Ace', suit='Diamonds')
        two_of_clubs = Card(rank='2', suit='Clubs')
        cards = [
            ace_of_spades,
            two_of_clubs
        ]
        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.cards,
            [
                two_of_clubs,
                ace_of_spades
            ]
        )

    def test_figures_out_no_cards_is_best_rank(self):
        hand = Hand()
        self.assertEqual(
            hand.best_rank(),
            "No Cards"
        )


    def test_figures_out_high_card_is_best_rank(self):
        cards = [
            Card(rank='7', suit='Diamonds'),
            Card(rank='9', suit='Clubs')
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "High Card"
        )

    def test_figures_out_pair_is_best_rank(self):
        cards = [
            Card(rank='8', suit='Diamonds'),
            Card(rank='8', suit='Clubs')
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Pair"
        )

    def test_figures_out_two_pair_is_best_rank(self):
        cards = [
            Card(rank='8', suit='Diamonds'),
            Card(rank='8', suit='Clubs'),
            Card(rank='10', suit='Spades'),
            Card(rank='King', suit='Spades'),
            Card(rank='10', suit='Clubs')
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Two Pair"
        )

    def test_figures_out_three_of_a_kind_is_best_rank(self):
        cards = [
            Card(rank='8', suit='Diamonds'),
            Card(rank='8', suit='Clubs'),
            Card(rank='8', suit='Spades'),
            Card(rank='King', suit='Spades'),
            Card(rank='10', suit='Clubs')
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Three of a Kind"
        )

    def test_figures_out_straight_is_best_rank(self):
        cards = [
            Card(rank='6', suit='Diamonds'),
            Card(rank='7', suit='Clubs'),
            Card(rank='8', suit='Spades'),
            Card(rank='9', suit='Spades'),
            Card(rank='10', suit='Clubs')
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Straight"
        )

    def test_does_not_deem_two_consecutive_cards_as_straight(self):
        cards = [
            Card(rank = "6", suit = "Hearts"),
            Card(rank = "7", suit = "Diamonds")
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "High Card"
        )

    def test_figures_best_rank_when_flush(self):
        cards = [
            Card(rank=rank, suit='Diamonds')
            for rank in ['2', '3', '5', '8', "Queen"]
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Flush"
        )

    def test_figures_full_house_is_best_rank(self):
        cards = [
            Card(rank='8', suit='Diamonds'),
            Card(rank='8', suit='Clubs'),
            Card(rank='10', suit='Spades'),
            Card(rank='10', suit='Diamonds'),
            Card(rank='10', suit='Clubs')
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Full house"
        )

    def test_figures_out_four_of_a_kind_is_best_rank(self):
        cards = [
            Card(rank='8', suit='Diamonds'),
            Card(rank='8', suit='Clubs'),
            Card(rank='8', suit='Spades'),
            Card(rank='8', suit='Hearts'),
            Card(rank='King', suit='Clubs')
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Four of a Kind"
        )

    def test_figures_best_rank_when_straight_flush(self):
        cards = [
            Card(rank='7', suit='Diamonds'),
            Card(rank='8', suit='Diamonds'),
            Card(rank='9', suit='Diamonds'),
            Card(rank='10', suit='Diamonds'),
            Card(rank='Jack', suit='Diamonds')
            ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Straight Flush"
        )

    def test_figures_best_rank_when_royal_flush(self):
        cards = [
            Card(rank='10', suit='Diamonds'),
            Card(rank='Jack', suit='Diamonds'),
            Card(rank='Queen', suit='Diamonds'),
            Card(rank='Ace', suit='Diamonds'),
            Card(rank='King', suit='Diamonds')
            ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Royal Flush"
        )
