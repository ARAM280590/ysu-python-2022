"""
lecture 7 homework
"""

from abc import ABC, abstractmethod
from itertools import product
from random import shuffle
from time import sleep


class CardABC(ABC):

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def value(self):
        pass


class DeckABC(ABC):

    @abstractmethod
    def create_deck(self):
        pass

    @abstractmethod
    def shuffle(self, deck):
        pass


class Card(CardABC):

    def __init__(self, suit, rank):
        pass

    def __repr__(self):
        pass

    def value(self):
        pass


class FaceCard(Card):


    def __init__(self, suit, rank):
        pass

    def value(self):
        pass


class AceCard(Card):


    def __init__(self, suit, rank):
        pass

    def value(self):
        pass


class NumCard(Card):

    def __init__(self, suit, rank):
        pass

    def value(self):
        pass


class Deck(DeckABC):

    def __init__(self):
        pass

    def __len__(self):
        pass

    def deal(self):
        pass

    def create_deck(self):
        pass

    @staticmethod
    def shuffle(self, deck_):
        pass


class Player:

    def __init__(self, name):
        pass

    def __repr__(self):
        pass


class Game:

    def __init__(self, deck):
        pass

    @staticmethod
    def add_player(self):
        pass

    @staticmethod
    def initial_deal(self):
        pass

    def show_status(self):
        for player in [self.dealer] + self.users:
            print(player)

    @staticmethod
    def check_hand(self, hand):
        pass

    def ask_user(self, user: Player):
        pass

    def ask_dealer(self):
        pass

    @staticmethod
    def start_again():
        pass


def main():
    def looping():
        deck = Deck()
        game = Game(deck)
        for user in game.users:
            game.ask_user(user=user)
        game.show_status()
        game.ask_dealer()
        if game.start_again():
            looping()
    looping()
    print("Thanks. Bye!")


if __name__ == "__main__":
    main()
