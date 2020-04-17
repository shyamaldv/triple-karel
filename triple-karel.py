from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def main():
    """
    Building Karel for all worlds.
    """
    paint_firstbox()
    paint_secondbox()
    paint_thirdbox()


def paint_firstbox():
    while left_is_blocked():
        put_beeper()
        move()
    if left_is_clear():
        turn_left()
        move()
    while left_is_blocked():
        put_beeper()
        move()
    if left_is_clear():
        turn_left()
        move()
    while left_is_blocked():
        put_beeper()
        move()

def paint_secondbox():
    if front_is_blocked():
        turn_right()
    while left_is_blocked():
        put_beeper()
        move()
    if left_is_clear():
        turn_left()
        move()
    while left_is_blocked():
        put_beeper()
        move()
    if left_is_clear():
        turn_left()
        move()
    while left_is_blocked():
        put_beeper()
        move()

def paint_thirdbox():
    if front_is_blocked():
        turn_right()
    while left_is_blocked():
        put_beeper()
        move()
    if left_is_clear():
        turn_left()
        move()
    while left_is_blocked():
        put_beeper()
        move()
    if front_is_clear():
        turn_left()
        move()
    while left_is_blocked():
        put_beeper()
        move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()





# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
