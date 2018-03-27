# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
message = ""

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.hand = []

    def __str__(self):
        # return a string representation of a hand
        s = "Hand contains "
        for i in self.hand:
            s += i.suit + i.rank + " "
        return s

    def add_card(self, card):
        # add a card object to a hand
        return self.hand.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        hand_value = 0
        ranks = []
        for card in self.hand:
            hand_value += VALUES[card.rank]
            ranks.append(card.rank)
        if "A" not in ranks:
            return hand_value
        else:
            if hand_value + 10 <= 21:
                return hand_value + 10
            else:
                return hand_value
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for card in self.hand:
            card.draw(canvas, pos)
            pos[0] = pos[0] + CARD_SIZE[0] + 10
 
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []
        for i in SUITS:
            for j in RANKS:
                self.deck.append(Card(i,j))

    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        return random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        return self.deck.pop()
    
    def __str__(self):
        pass	# return a string representing the deck
        s = "Deck contains "
        for i in self.deck:
            s += i.suit + i.rank + " "
        return s


#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player_hand, dealer_hand, message, score

    # your code goes here
    if in_play:
        message = "You lost the round."
        score -= 1
        outcome = "New deal?"
        in_play = False
    else: 
        deck = Deck()
        player_hand = Hand()
        dealer_hand = Hand()
        deck.shuffle()
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
    #print "Player hand is: " , player_hand
    #print "Dealer hand is: " , dealer_hand
        outcome = "Hit or Stand?"
        message = ""
        in_play = True

def hit():
    # replace with your code below
    global outcome, in_play, message, score
    if in_play:
        player_hand.add_card(deck.deal_card())
        #print player_hand
        if player_hand.get_value() > 21:
            message = "You have busted and you lost"
            score -= 1
            outcome = "New deal?"
            in_play = False
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global outcome, in_play, message,score
    # replace with your code below
    #if player_hand.get_value() > 21:
        #print "You have busted"
    if in_play:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
        #print dealer_hand
        if dealer_hand.get_value() > 21:
            message = "Dealer has busted and you won."
            score += 1
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                message = "You won"
                score += 1
            else:
                message = "Dealer won"
                score -= 1
        outcome = "New deal?"
        in_play = False
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    #card = Card("S", "A")
    #card.draw(canvas, [300, 300])
    player_hand.draw(canvas, [50, 400])
    dealer_hand.draw(canvas, [50, 170])
    canvas.draw_text('Blackjack', [70,70], 40, "aqua")
    canvas.draw_text('Dealer', [50, 150], 30, "black")
    canvas.draw_text('Player', [50, 380], 30, "black")
    canvas.draw_text(outcome, [200, 380], 30, "black")
    canvas.draw_text("Score " + str(score), [400,70], 30, "black")
    canvas.draw_text(message, [200, 150], 30, "black")
    if in_play:
        canvas.draw_image(card_back,CARD_BACK_CENTER,CARD_BACK_SIZE,
                          [50+CARD_BACK_CENTER[0],170+CARD_BACK_CENTER[1]],CARD_BACK_SIZE)


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric'