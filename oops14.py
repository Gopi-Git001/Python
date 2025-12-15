suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True
import random

class Card():
    
    def __init__(self,suit,rank):
        self.rank = rank
        self.suit = suit 
        
    def __str__(self):
         return f" {self.rank} of {self.suit }"
     
class Deck():
    
    def __init__(self):
        self.all_cards = [ Card(suit,rank) for suit in suits for rank in ranks]
        
    def shuffle(self):
        return random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop(0)

class Hand():
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        
    def add_cards(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        
        if card.rank == 'Aces':
            self.aces +=1
        
    def adjust_aces(self) :    
        while self.value >21 and self.aces:
            self.value -=10 
            self.aces -= 1
            
            
        
class Chips():
    
    def __init__(self):        
        self.total = 100
        self.bet = 0
        
    def win_bet(self):
        self.total +=self.bet
    
    def lose_bet(self):
        self.total -= self.bet 
        

def take_bet(chips):
    
    while True:
        try :
            chips.bet = int(input('How many chips would you like to bet : '))            
        except:             
            print('Please enter correct bet value ')
            continue    
        else:            
            if chips.bet > chips.total :
                    print("sorry your can't exceed total",chips.total)
            else:
                break
                              
def hit(deck,hand):
        hand.add_cards(deck.deal_one())
        hand.adjust_aces()
        
def hit_or_stand(deck,hand):
    global playing
    
    while playing:        
        x = input("would you like to hit or stand plaese enter h or s")
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print('You are on the stand mode ')
            playing = False
        else:
            print('sorry, please try again')
            continue
        break
def show_some(player,dealer):
    
    print("Dealer's hand")    
    print(dealer.cards[1])
    print('PLayer hand:')
    for i in player.cards:
        print(i)
        
def show_all(player,dealer):
    print("dealer's hand:")
    for card in dealer.cards:
        print(card)
    print("player's hand")
    for card in player.cards:
        print(card)


def player_busts(player,dealer,chips):
    print('Player busts!')
    print('Dealer wins')
    chips.lose_bet()
    
def player_win(player,dealer,chips):
    print("player wins")
    chips.win_bet()
    
def dealer_win(player,dealer,chips):
    print('Dealer wins')
    chips.lose_bet()
    
def dealer_busts(player,dealer,chips):
    print('Dealer busts')
    chips.win_bet()
    
    
def push(delaer,player):
    print("Player and dealer tie! It's time to push")
    
    

while True:
    
    new_deck = Deck()
    new_deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_cards(new_deck.deal_one())
    player_hand.add_cards(new_deck.deal_one())
    
    dealer_hand = Hand()
    dealer_hand.add_cards(new_deck.deal_one())
    dealer_hand.add_cards(new_deck.deal_one())
    
    player_chips = Chips()
    take_bet(player_chips)
    
    
    show_some(player_hand,dealer_hand)
    
    while playing:
        
        hit_or_stand(new_deck,player_hand)
        show_some(player_hand,dealer_hand)
        
        if player_hand.value >21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
        
    if player_hand.value <=21:
        
        while dealer_hand.value < 17:
            hit(new_deck,dealer_hand)
            
        if dealer_hand.value >21:
            dealer_busts(dealer_hand,player_hand,player_chips)
        
        elif dealer_hand.value > player_hand.value:
            dealer_win(player_hand,dealer_hand,player_chips)
        
        elif dealer_hand.value < player_hand.value:
            player_win(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
            
            
    new_game  = input('Would you like to play again y or n:')
    
    if new_game[0].lower()== 'y':
        playing = True
        continue        
    elif new_game[0].lower() == 'n':
        print('Thank you!')
        playing = False
        break
    else:
        print('Hey you entered wrong details ')
        continue
    
        
    
    
    
    
    
    