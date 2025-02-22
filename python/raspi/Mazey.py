# Example code for IMRT100 robot project


# Import some modules that we need
import imrt_robot_serial
import signal
import time
import sys
import random

LEFT = -1
RIGHT = 1
FORWARDS = 1
BACKWARDS = -1
DRIVING_SPEED = 190
TURNING_SPEED = 90
FAST_TURNING_SPEED = 140
MEDIUM_TURNING_SPEED = 120
SLOW_TURNING_SPEED = 70
LEFT_DISTANCE = 15
LEFT_STOP_DISTANCE = 15
RIGHT_STOP_DISTANCE = 19
RIGHT_DISTANCE = 12

def stop_robot(duration):

    iterations = int(duration * 10)
    
    for i in range(iterations):
        motor_serial.send_command(0, 0)
        time.sleep(0.10)



def drive_robot(direction, duration):
    
    speed = DRIVING_SPEED * direction
    iterations = int(duration * 10)

    for i in range(iterations):
        motor_serial.send_command(speed, speed)
        time.sleep(0.10)


def turn_robot_right():

    direction = 1
    iterations = (11)
    
    for i in range(iterations):
        motor_serial.send_command(TURNING_SPEED * direction, -TURNING_SPEED * direction)
        time.sleep(0.10)

def turn_robot_left():

    direction = -1
    iterations = (11)
    
    for i in range(iterations):
        motor_serial.send_command(TURNING_SPEED * direction, -TURNING_SPEED * direction)
        time.sleep(0.10)

def turn_robot_around():

    direction = -1
    iterations = (14)
    
    for i in range(iterations):
        motor_serial.send_command(TURNING_SPEED * direction, -TURNING_SPEED * direction)
        time.sleep(0.10)

def turn_robot_slight_left():

    direction = 1
    iterations = (1)
    
    for i in range(iterations):
        motor_serial.send_command(-SLOW_TURNING_SPEED * direction, FAST_TURNING_SPEED * direction)
        time.sleep(0.05)

def turn_robot_slight_right():

    direction = 1
    iterations = (1)
    
    for i in range(iterations):
        motor_serial.send_command(TURNING_SPEED * direction, -TURNING_SPEED * direction)
        time.sleep(0.05)
        

def turn_robot_medium_right():

    direction = 1
    iterations = (2)
    
    for i in range(iterations):
        motor_serial.send_command(FAST_TURNING_SPEED * direction, SLOW_TURNING_SPEED * direction)
        time.sleep(0.05)
        

# We want our program to send commands at 10 Hz (10 commands per second)
execution_frequency = 10 #Hz
execution_period = 1. / execution_frequency #seconds


# Create motor serial object
motor_serial = imrt_robot_serial.IMRTRobotSerial()


# Open serial port. Exit if serial port cannot be opened
try:
    motor_serial.connect("/dev/ttyACM0")
except:
    print("Could not open port. Is your robot connected?\nExiting program")
    sys.exit()

    
# Start serial receive thread
motor_serial.run()


# Now we will enter a loop that will keep looping until the program terminates
print("Entering loop. Ctrl+c to terminate")
while not motor_serial.shutdown_now :


    # Get and print readings from distance sensors
    dist_1 = motor_serial.get_dist_1()
    dist_2 = motor_serial.get_dist_2()
    dist_3 = motor_serial.get_dist_3()
    dist_4 = motor_serial.get_dist_4()
    print("Dist 1:", dist_1, "   Dist 2:", dist_2, "  Dist 3:", dist_3, "   Dist 4:", dist_4)

    # Check if there is an obstacle in the way
    
    # Obstacle on the left side
    if dist_1 < LEFT_DISTANCE or dist_2 < LEFT_STOP_DISTANCE:
        # Too close, back up and turn 180 degrees
        if dist_2 < LEFT_STOP_DISTANCE:
            drive_robot(BACKWARDS, 0.3)
            turn_robot_right()
        else:
            turn_robot_slight_right()
            
    # Obstacle on the right side
    elif dist_3 < RIGHT_STOP_DISTANCE or dist_4 < RIGHT_DISTANCE:
        # Too close, back up and turn left
        if dist_3 < RIGHT_STOP_DISTANCE:
            drive_robot(BACKWARDS, 0.3)
            turn_robot_left()
        else:
            turn_robot_slight_left()

    # Too much room to the right        
    elif dist_4 < 150:
        if dist_4 > 51:
            turn_robot_medium_right()
        else:
            drive_robot(FORWARDS, 0.1)
            
    # If there is nothing in front of the robot it continues driving forwards        
    else:
        drive_robot(FORWARDS, 0.1)

# motor_serial has told us that its time to exit
# we have now exited the loop
# It's only polite to say goodbye
print("Goodbye")
