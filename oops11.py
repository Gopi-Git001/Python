class Card():
    
    def __init__(self,suit,rank):
        self.rank = rank
        self.suit = suit
        
    def __st__(self):
        
        return self.rank +' of '+self.suit


# class Deck():
    
#     def __init__(self):
        
#         self.all_cards = [Card(suit,rank) for suit in suits for rank in ranks]
        
        
        