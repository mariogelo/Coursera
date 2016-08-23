# Convert to dollars and cents
import simplegui

# globals
value = 3.12

# Handle single quantity
def convert_units(val, name):
    result = str(val) + " " + name
    if val > 1:
        result = result + "s"
    return result
        
# convert xx.yy to xx dollars and yy cents
def convert(val):
    # Split into dollars and cents
    dollars = int(val)
    cents = int(round(100 * (val - dollars)))

    # Convert to strings
    dollars_string = convert_units(dollars, "dollar")
    cents_string = convert_units(cents, "cent")

    # return composite string
    if dollars == 0 and cents == 0:
        return "Broke!"
    elif dollars == 0:
        return cents_string
    elif cents == 0:
        return dollars_string
    else:
        return dollars_string + " and " + cents_string
    
# helper functions
def draw(canvas):
    canvas.draw_text(convert(value), [30, 20], 29, "green")

# classes

# define event handlers
def user_input(text):
    global value
    value = float(text)
    return value

# register event handlers
frame = simplegui.create_frame("Converter", 300, 100)
frame.set_draw_handler(draw)
frame.add_input("Value", user_input,100)

# start frame

frame.start()
