# template for "Stopwatch: The Game"
import simplegui

# define global variables
time = 0
pocetak = 0
kraj = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    a = int(time/600)
    b = int(time/100)%6
    c = int(time/10)%10
    d = int(time%10)
    
    formatirano = str(a) + ":" + str(b) + str(c) + "." + str(d)
    return formatirano

# define event handlers for buttons; "Start", "Stop", "Reset"
def start_time():
    global pocetak
    if timer.is_running != True:
        pocetak += 1
        timer.is_running = True
    print "Start: ", pocetak
    timer.start()

def stop_time():
    global kraj
    print "Trenutni status: ", timer.is_running
    if timer.is_running != False:
        kraj += 1
        timer.is_running = False
    print "Stop: ", kraj
    timer.stop()
    
def reset():
    timer.stop()
    global time, pocetak, kraj
    #global pocetak
    #global kraj
    time = 0
    pocetak = 0
    kraj = 0
    

# define event handler for timer with 0.1 sec interval
def create_timer():
    global time
    time += 1 

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), [10,20], 26, "blue")
    canvas.draw_text("Pocni: " + str(pocetak), [10,50], 18, "red")
    canvas.draw_text("Stani: " + str(kraj), [10, 70], 18, "red")
    
# create frame
frame = simplegui.create_frame("Stoperica", 150, 150)

# register event handlers
timer = simplegui.create_timer(100,create_timer)
frame.set_canvas_background("white")
frame.set_draw_handler(draw)
start_button = frame.add_button("Start", start_time, 50)
reset_button = frame.add_button("Reset", reset, 50)
stop_button =  frame.add_button("Stop", stop_time, 50)


# start frame
frame.start()
timer.is_running = False
