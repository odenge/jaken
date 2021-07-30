from card import Deck

class Player:
    def __init__(self, name, personality=0):
        self.wins = 0
        self.deck = Deck()
        self.card = None
        self.name = name
        self.personality = personality
