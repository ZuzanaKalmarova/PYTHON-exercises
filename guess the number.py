# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
range_upper = 100
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number = random.randrange(0,range_upper)
    print
    print "New game. Range is from 0 to", range_upper
    global allowed_guesses
    if range_upper == 100:
        allowed_guesses = 7
    else:
        allowed_guesses = 10
    print "Number of remaining guesses is", allowed_guesses
    # remove this when you add your code    
    


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range_upper
    range_upper = 100
    new_game()
    # remove this when you add your code    
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range_upper
    range_upper = 1000
    new_game()
    
    
def input_guess(guess):
    # main game logic goes here	
    guess = int(guess)
    print"Guess was" , guess
    if guess < secret_number:
        print "Higher"
        global allowed_guesses
        allowed_guesses = allowed_guesses - 1
        print "Number of remaining guesses is", allowed_guesses
    elif guess > secret_number:
        print "Lower"
        allowed_guesses = allowed_guesses - 1
        print "Number of remaining guesses is", allowed_guesses
    else:
        print "Correct"
        new_game()
    if allowed_guesses == 0:
        print "You lost. The secret number was", secret_number
        new_game()
    
    # remove this when you add your code
    

    
# create frame
frame = simplegui.create_frame('Guess the number', 300, 300)

# register event handlers for control elements and start frame
frame.add_input('Enter number', input_guess, 80)
frame.add_button("Range is [0,100)", range100)
frame.add_button("Range is [0,1000)", range1000)
frame.start()
# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
