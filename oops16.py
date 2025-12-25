suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}



class Card():
    
    def __init__(self,suit,rank):        
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        return f" {self.rank} of {self.suit} cards "
    

class Deck():
    
    def __init__(self):
        
        self.cards = [Card(suit,rank) for suit in suits for rank in ranks]

        
        # for suit in suits:
        #     for rank in ranks :
        #         self.cards.append(Card(suit,rank))
                
        
        
new_deck = Deck()

print(new_deck.cards[-1])


        