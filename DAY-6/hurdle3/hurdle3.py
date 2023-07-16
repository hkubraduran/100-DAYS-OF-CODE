"""
Project Name:Hurdle 3
Project Description: Reeborg has entered a hurdle race.
Make him run the course, following the path shown.
The position and number of hurdles changes each time this world is reloaded.
Your program should also be valid for worlds Hurdles 1 and Hurdles 2.
The final position of the robot must be (x, y) = (13, 1)
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():

    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while at_goal() != True:  # while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()