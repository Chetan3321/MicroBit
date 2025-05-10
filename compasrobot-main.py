# Imports go at the top
from microbit import *

def fwd(speed):
    # M1
    pin12.write_analog(speed)
    pin13.write_analog(0)
    # M2
    pin15.write_analog(speed)
    pin16.write_analog(0)

def bwd(speed):
    # M1
    pin12.write_analog(0)
    pin13.write_analog(speed)
    # M2
    pin15.write_analog(0)
    pin16.write_analog(speed)

def left(speed):
    # M1
    pin12.write_analog(speed)
    pin13.write_analog(0)
    # M2
    pin15.write_analog(0)
    pin16.write_analog(speed)

def right(speed):
    # M1
    pin12.write_analog(0)
    pin13.write_analog(speed)
    # M2
    pin15.write_analog(speed)
    pin16.write_analog(0)

heading_at_beginning = compass.heading()
display.scroll (heading_at_beginning)

while True:
    current_hedding = compass.heading()
    hedding_diff = heading_at_beginning - current_hedding
    if hedding_diff < -5:
        display.show (Image. ARROW_E)
        left(255)
    elif hedding_diff > 5:
        display.show (Image. ARROW_W)
        right (255)
    else:
        fwd(255)