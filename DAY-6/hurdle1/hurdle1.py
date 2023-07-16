"""
Project Name:Hurdle 1
Project Description: Reeborg has entered a hurdles race.
Make him run the course, following the path shown.
The final position of the robot must be (x, y) = (13, 1)
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

for i in range(0, 6):
    jump()