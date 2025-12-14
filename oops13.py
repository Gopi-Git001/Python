suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

import random 

class Card():
    
    def __init__(self,suit,rank):
        
        self.rank = rank
        
        self.suit = suit 
        
        self.value = values[rank]
        
    def __str__(self):
        return f" {self.rank} of {self.suit}"


class Deck():
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits :        
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
                
    def shuffle(self):
        
        return random.shuffle(self.all_cards)
                
    def deal_one(self):
        
        return self.cards.pop(0)


class Player():
    
    def __init__(self,name):
        
        self.name = name
        self.cards = []
        
    def add_cards(self,cards):
        
        if type[cards] == type([]):
            
            self.cards.extend(cards) 
            
        else:
            
            self.cards.append(cards)
    
    def remove_one(self):
        
        return self.cards.pop()
    
    


player_one = Player('One')

player_two = Player('Two')

new_deck = Deck()

new_deck.shuffle()


for i in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
    

game_on = True

while game_on:
    
    if len(player_one.cards) == 0:
        print("Player One has unabel to play the game")
        print("Player Two WINS")
        game_on = True
        break
    if len(player_two.cards) == 0:
        print("Player two has unable to play the Game")
        print("Player One WINS")
        game_on = True
        break
    
    
            


                
           
        