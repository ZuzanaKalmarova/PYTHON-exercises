# template for "Stopwatch: The Game"
import simplegui
# define global variables
msec = 0
x = 0
y = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = t//600
    B = ((t//10)%60)//10
    C = ((t//10)%60)%10
    D = t % 10
    return str(A) + ':' + str(B) + str(C) + '.' + str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    if timer.is_running():
        timer.stop()
        global x, y
        y += 1
        if (msec % 10) == 0:
            x += 1
    
def reset():
    global msec, x, y
    timer.stop()
    msec = 0
    x = 0
    y = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global msec
    msec += 1
    

# define draw handler
def draw(canvas):
    canvas.draw_text(format(msec),[120,160],30,'White')
    canvas.draw_text((str(x)+'/'+str(y)), [250,30], 20, 'White')
    
# create frame
frame = simplegui.create_frame('Stopwatch', 300, 300)

# register event handlers
timer = simplegui.create_timer(100, tick)
frame.set_draw_handler(draw)
frame.add_button('Start', start, 100)
frame.add_button('Stop', stop, 100)
frame.add_button('Reset', reset, 100)

# start frame
frame.start()

# Please remember to review the grading rubric
