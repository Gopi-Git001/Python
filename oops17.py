suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

import random 

playing = True

class Card():

    def __init__(self,suit,rank):
        self.rank = rank 
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit} "

# my_cards = Card('Hearts','Two')

# print(my_cards.rank)

# print(my_cards.suit)

# print(my_cards)


class Deck():
    def __init__(self):
        # self.all_cards = [Card(suit,rank) for suit in suits for rank in ranks ]

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))

    def shuffle(self):
        return random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop(0)

# new_deck = Deck()

# print(new_deck.all_cards[1])

class Hand():

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_cards(self,card):

        self.cards.append(card)
        self.value += values[card.rank]

        if self.aces == 'Ace':
            self.aces +=1

    def adjust_aces(self):

        while self.value >21 and self.aces:
            self.value -=10
            self.aces -=1

class Chips():

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

    
def take_bet(chips):

    while True:

        try:
            chips.bet = input("How much would you like to bet (0 to 100) :")
        except :
            print('You Entered wrong Value')
            continue        
        else:
            if chips.bet > chips.total:
                print('You exceed the limit {chips.total}')
            else:
                break

def hit(deck,hand):
    hand.add_cards(deck.deal_one())
    hand.adjust_aces()

def hit_stand(deck,hand):
    global playing

    while playing:

        x = input('would you like to hit or stand please enter h or s')

        if x[0].lower() == 'h':
            print('Player selct hit mode')
            hit(deck,hand)
        elif x[0].lower()=='s':
            print('Player on stand mode')
            playing = False
        else:
            print('Please choose a correct value')
            continue
        break

