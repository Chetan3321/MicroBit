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
    pin16.write_analog(0)

def right(speed):
    # M1
    pin12.write_analog(0)
    pin13.write_analog(0)
    # M2
    pin15.write_analog(speed)
    pin16.write_analog(0)

def turn_left(speed):
    # M1
    pin12.write_analog(speed)
    pin13.write_analog(0)
    # M2
    pin15.write_analog(0)
    pin16.write_analog(speed)

def turn_right(speed):
    # M1
    pin12.write_analog(0)
    pin13.write_analog(speed)
    # M2
    pin15.write_analog(speed)
    pin16.write_analog(0)

def stop():
    # M1
    pin12.write_digital(0)
    pin13.write_digital(0)
    # M2
    pin15.write_digital(0)
    pin16.write_digital(0)

floor_brightness = 0
threshold_value = 100
brightness_white = 0
brightness_black = 0
observed_data = []

def learning_brightness(current_brightness):
    observed_data.clear()

    for i in range(11):
        observed_data.append(pin0.read_analog())
    observed_data.append(current_brightness)
    print(observed_data)
    observed_data.sort()
    print(observed_data)
    observed_data.pop(0)
    print(observed_data)
    observed_data.pop(len(observed_data)-1)
    print(observed_data)
    observed_data_total = 0
    for i in observed_data:
        observed_data_total = observed_data_total + i
    return observed_data_total/len(observed_data)

# Code in a 'while True:' loop repeats forever
while True:
    #display.show(floor_brightness)
    if button_a.is_pressed() and button_b.is_pressed():
        display.scroll('C')
        brightness_black = 0
        brightness_white = 0

    if button_a.was_pressed():
        # Learn white area's brightness
        display.scroll('B')
        brightness_black = learning_brightness(brightness_black)
        print(brightness_black)

    if button_b.was_pressed():
        # Learn white area's brightness
        display.scroll('W')
        brightness_white = learning_brightness(brightness_white)
        print(brightness_white)

    if pin_logo.is_touched():
        # Line folloing mode
        display.show(Image.HAPPY)
        sleep(1000)

        threshold_value = (brightness_white + brightness_black)/2
        display.scroll(str(threshold_value))
        print(threshold_value)

        while True:
            if pin_logo.is_touched():
                sleep(1000)
                break

            floor_brightness = pin0.read_analog()
            print(floor_brightness)

            if floor_brightness > threshold_value:
                display.show(Image.ARROW_E)
                left(200)
            else:
                display.show(Image.ARROW_W)
                right(200)
