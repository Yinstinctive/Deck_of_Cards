from random import shuffle

class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

class Deck:
    suits = ("Hearts","Diamonds","Clubs","Spades")
    values = ("A","2","3","4","5","6","7","8","9","10","J","Q","K")

    def __init__(self):
        self.cards = []
        for suit in Deck.suits:
            for value in Deck.values:
                self.cards.append(Card(suit,value))
	
    def count(self):
        return len(self.cards)

    def __repr__(self):
        return "Deck of {} cards".format(self.count())

    def _deal(self, remove_num):
        if self.count()==0:
            raise ValueError("All cards have been dealt")
        final_remove_num = min(self.count(), remove_num)
        if final_remove_num ==1:
            return self.cards.pop()
        else:
            list_of_cards = []
            for i in range(final_remove_num):
                list_of_cards.append(self.cards.pop())
            return list_of_cards

    def shuffle(self):
        if self.count() != 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self

    def deal_card(self):
        return self._deal(1)

    def deal_hand(self, num):
        return self._deal(num)
