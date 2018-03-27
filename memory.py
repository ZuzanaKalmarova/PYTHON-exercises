# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global cards, exposed, state, counter
    cards = list(range(8)) + list(range(8))
    random.shuffle(cards)
    exposed = [False]*16
    state = 0
    counter = 0
    label.set_text("Turns = " + str(counter))
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, a, b, counter
    if exposed[pos[0]//50] == False:
        if state == 0:
            a = pos[0]//50
            exposed[a] = True
            state = 1
        elif state == 1:
            counter += 1
            label.set_text("Turns = " + str(counter))
            b = pos[0]//50
            exposed[b] = True
            state = 2
        else:
            if cards[a] != cards[b]:
                exposed[a] = False
                exposed[b] = False
            state = 1
            a = pos[0]//50
            exposed[a] = True
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(len(cards)):
        if exposed[i]:
            canvas.draw_text(str(cards[i]), [10+i*50, 70], 60, "white")
        else:
            canvas.draw_polygon([[i*50,100],[(i+1)*50,100],[(i+1)*50,0],
                                 [i*50,0]], 1, "black", "green")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric