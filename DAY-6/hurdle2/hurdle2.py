"""
Project Name:Hurdle 2
Project Description: Reeborg has entered a hurdle race, but he does not know in advance how long the race is.
Make him run the course, following a path similar to the one shown,
but stopping at the only flag that will be shown after the race has started.
Your program should also be valid for world Hurdles 1.
The final required position of the robot will be chosen at random.
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while at_goal() != True:  # while not at_goal():
    jump()