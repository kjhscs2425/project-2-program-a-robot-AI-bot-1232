# Import the robot control commands from the library
from simulator import robot
import time

def forward(distance):
    robot.motors(1, 1, distance)
def backward(distance):
    robot.motors(-1, -1, distance)
def turn_left(distance):
    robot.motors(-1, 1, distance)
def turn_right(distance):
    robot.motors(1, -1, distance)
def dance():
    robot.motors(1,1,3)
    robot.motors(-1,-1,3)
    robot.motors(-1,1,3)
    robot.motors(1,-1,3)



while True: 
    age = input("How old are you: ")
    if age == "exit":
        robot.exit()
        break
    name = input("What is your name: ")
    if name == "exit":
        robot.exit()
        break
    location = input("Where are you from: ")
    if location == "exit":
        robot.exit()
        break
    favorite_color = input("What is your favorite color: ")
    if favorite_color == "exit":
        robot.exit()
        break
    hobby = input("What is your hobby: ")
    if hobby == "exit":
        robot.exit()
        break
    else:
        for i in range(1000):
            left, right = robot.sonars()
            print(left, right)
            backward(1)
            forward(1)
            
# New function to return if the robot can move forward based on sonar readings


def can_move_forward():
    right, left = robot.sonars()
    if left > 10 and right > 10:
        return True 
    else:
        return False
def autonomous_movement():
    start_time = time.time()
    while time.time() - start_time <20:
         left, right = robot.sonars




        