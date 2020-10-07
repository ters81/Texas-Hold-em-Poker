import unittest
from unittest.mock import patch

from poker.card import Card
from poker.deck import Deck

class DeckTest(unittest.TestCase):

    def test_stores_no_cards_at_start(self):
        deck = Deck()
        self.assertEqual(
            deck.cards,
            []
        )

    def test_adds_cards_to_its_collection(self):
        card = Card(rank="2", suit="Clubs")
        deck = Deck()
        deck.add_cards([card])
        self.assertEqual(
            deck.cards,
            [card]
        )

    @patch('random.shuffle')
    def test_shuffles_card_in_random_order(self, mock_shuffle):
        deck = Deck()

        cards = [
            Card(rank="2", suit="Clubs"),
            Card(rank="Ace", suit="Spades")
        ]

        deck.add_cards(cards)
        deck.shuffle()
        mock_shuffle.assert_called_once_with(cards)

    def test_removes_specified_number_of_cards_from_deck(self):
      two = Card(rank="2", suit="Clubs"),
      ace = Card(rank="Ace", suit="Spades")
      cards = [two, ace]

      deck = Deck()

      deck.add_cards(cards)

      self.assertEqual(
          deck.remove_cards(1),
          [two]
      )

      self.assertEqual(
          deck.cards,
          [ace]
      )




