import unittest
from poker.card import Card
from poker.hand import Hand

class HandTest(unittest.TestCase):

    def test_starts_out_with_no_cards(self):
        hand = Hand()
        self.assertEqual(hand.cards, [])

    def test_shows_all_its_cards_in_technical_representation(self):
        cards = [
            Card(rank='7', suit='Diamonds'),
            Card(rank='9', suit='Clubs')
        ]

        hand = Hand()
        hand.add_cards(cards)
        self.assertEqual(
            repr(hand),
            "7 of Diamonds, 9 of Clubs"
        )



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
