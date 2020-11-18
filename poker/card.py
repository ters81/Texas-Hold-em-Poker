
class Card():

    SUITS = ("Hearts", "Spades", "Diamonds", "Clubs")
    RANKS = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")

    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise ValueError(f"Нет такого достоинства карты, должно быть одно из {self.RANKS}")
        if suit not in self.SUITS:
            raise ValueError(f"Нет такой масти карты, должна быть одна из {self.SUITS}")

        self.rank = rank
        self.rank_index = self.RANKS.index(rank)
        self.suit = suit

    def __str__(self):
        # return self.rank + " of " + self.suit
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f'Card("{self.rank}", "{self.suit}")'

    @classmethod
    def create_standart_52_cards(cls):
        cards = []
        for suit in cls.SUITS:
            for rank in cls.RANKS:
                cards.append(cls(suit=suit, rank=rank))

        return cards

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        if self.rank == other.rank:
            return self.suit < other.suit

        return self.rank_index < other.rank_index






