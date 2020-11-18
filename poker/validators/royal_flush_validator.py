from poker.validators import StraightFlushValidator

class RoyalFlushValidator():
    def __init__(self, cards):
        self.cards = cards
        self.name = 'Royal Flush'

    def is_valid(self):
        straight_flash_validator = StraightFlushValidator(cards=self.cards)
        if straight_flash_validator.is_valid():
            straight_flash_cards = straight_flash_validator.valid_cards()
            is_royal = straight_flash_cards[-1].rank == 'Ace'
            return is_royal

        return False


    def valid_cards(self):
        return StraightFlushValidator(cards=self.cards).valid_cards()