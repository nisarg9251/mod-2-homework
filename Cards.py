import random

class Object:
    def __init__(self):
        '''
        initialize object from Object
        '''
        pass

class Card(Object):
    def __init__(self, value, suit):
        '''
        initialize  value & suit of card
        '''
        self.value = value
        self.suit = suit
    def __repr__(self):
        '''
        printation  of the card
        '''
        return f"Card({self.value} of {self.suit})"
    def __lt__(self, other):
        '''
        sorting of cards by suit, then value
        '''
        if self.suit < other.suit:
            return True
        elif self.suit == other.suit:
            return self.value < other.value
        else:
            return False
    def __eq__(self, other):
        '''
        returns if cards are equal to one another
        '''
        if self.suit == other.suit:
            return self.value == other.value
        else:
            return False

class Deck(Object):
    def __init__(self, values = None, suits = None):
        '''
        initialize a deck based on collection of values and suits passed in
        '''
        self.values = values
        self.suits = suits
        if values is None and suits is None:
            self.card_list = [Card(value, 'clubs') for value in range(13, 0, -1)]
            self.card_list += ([Card(value, 'diamonds') for value in range(13, 0, -1)])
            self.card_list += ([Card(value, 'hearts') for value in range(13, 0, -1)])
            self.card_list += ([Card(value, 'spades') for value in range(13, 0, -1)])
        else:
            self.card_list = []
            suits.sort()
            values.sort()
            for i in suits:
                for j in values:
                    self.card_list.append(Card(j, i))
    def __len__(self):
        '''
        returns number of cards in the deck
        '''
        return len(self.card_list)
    def sort(self):
        '''
        sorts cards in the deck
        '''
        self.card_list.sort()
        return self.card_list
    def __repr__(self):
        '''
        printation of the deck
        '''
        n = "Deck: ["
        for i in self.card_list:
            x = "Card(" + str(i.value) + " of " + str(i.suit) + "), "
            if i == self.card_list[len(self.card_list)-1]:
                x = "Card(" + str(i.value) + " of " + str(i.suit) + ")]"
            n += x
        return n
    def shuffle(self):
        '''
        returns deck in randomized order
        '''
        return random.shuffle(self.card_list)
    def draw_top(self):
        '''
        removes and returns top card in the deck
        raises Runtime Error if someone draws from an empty deck
        '''
        x = self.card_list.pop()
        if len(self.card_list) == 0:
            raise RuntimeError ("Deck is Empty")
        return x

class Hand(Deck):
    def __init__(self, card_list):
        '''
        initialize hand from passed in collection of cards
        '''
        self.card_list = card_list
    def __repr__(self):
        '''
        printation of the hand
        '''
        return f"Hand: {self.card_list}"
    def play(self, card):
        '''
        removes and returns card from hand
        raises Runtime Error if card is not in hand
        '''
        if card in self.card_list:
            self.card_list.remove(card)
            return card
        if card not in self.card_list:
            raise RuntimeError ("Card is not in Hand")
