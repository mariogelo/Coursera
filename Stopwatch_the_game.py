# template for "Stopwatch: The Game"
import simplegui

# define global variables
time = 0
start_count = 0
stop_count = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format_time(time):
    a = int(time/600)
    b = int(time/100)%6
    c = int(time/10)%10
    d = int(time%10)
    
    return str(a) + ":" + str(b) + str(c) + "." + str(d)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start_time():
    global start_count
    if timer.is_running == False:
        start_count += 1
        timer.is_running = True
    print "Start= ", start_count
    timer.start()

def stop_time():
    global stop_count
    print "Timer status: ", timer.is_running
    if timer.is_running == True:
        stop_count += 1
        timer.is_running = False
    print "Stop= ", stop_count
    timer.stop()
    
def reset_time():
    timer.stop()
    global time
    global start_count
    global stop_count
    time = 0
    start_count = 0
    stop_count = 0
    

# define event handler for timer with 0.1 sec interval
def create_timer():
    global time
    time = time + 1 

# define draw handler
def draw(canvas):
    canvas.draw_text(format_time(time), [30,30], 20, "green")
    canvas.draw_text("Start count: " + str(start_count), [140,30], 15, "red")
    canvas.draw_text("Stop count: " + str(stop_count), [140, 50], 15, "red")
    
# create frame
frame = simplegui.create_frame("Digital Watch", 300, 200)

# register event handlers
timer = simplegui.create_timer(100,create_timer)
frame.set_draw_handler(draw)
start_button = frame.add_button("Start", start_time, 50)
reset_button = frame.add_button("Reset", reset_time, 50)
stop_button =  frame.add_button("Stop", stop_time, 50)

# start frame
frame.start()
timer.is_running = False

# Please remember to review the grading rubric
