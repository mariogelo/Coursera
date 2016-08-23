# Examples of mouse input

import simplegui
import math

# intialize globals
WIDTH = 450
HEIGHT = 300
ball_list = []
BALL_RADIUS = 15

# helper function
def distance(p, q):
    return math.sqrt( (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define event handler for mouse click, draw
def click(pos):
    changed = False
    for ball in ball_list:        
        if distance([ball[0], ball[1]], pos) < BALL_RADIUS:
            ball[2] = "Green"
            changed = True

    if not changed:
        ball_list.append([pos[0], pos[1], "Red"])
        print "Ball list dole: ", ball_list

        
def draw(canvas):
    for ball in ball_list:
        canvas.draw_circle([ball[0], ball[1]], BALL_RADIUS, 1, "Black", ball[2])

# create frame
frame = simplegui.create_frame("Mouse selection", WIDTH, HEIGHT)
frame.set_canvas_background("White")

# register event handler
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()
    