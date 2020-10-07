from poker.card import Card
from poker.deck import Deck
from poker.hand import Hand
from poker.player import Player


deck = Deck()
cards = Card.create_standart_52_cards()
deck.add_cards(cards)

hand1 = Hand()
hand2 = Hand()


player1 = Player(name="Serhii", hand=hand1)
player2 = Player(name="Boris", hand=hand2)
players = [player1, player2]
