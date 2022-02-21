from .card import Card

class Player:
    def __init__(self, name, turn_count, number_of_cards, history):
        self.name = name
        self.turn_count = turn_count
        self.number_of_cards = number_of_cards
        self.history = history