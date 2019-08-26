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
TURNING_SPEED = 150
TURN_DISTANCE = 20
SIDE_DISTANCE = 8
STOP_DISTANCE = 6

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
    iterations = (2)
    
    for i in range(iterations):
        motor_serial.send_command(TURNING_SPEED * direction, -TURNING_SPEED * direction)
        time.sleep(0.10)

def turn_robot_left():

    direction = -1
    iterations = (7)
    
    for i in range(iterations):
        motor_serial.send_command(TURNING_SPEED * direction, -TURNING_SPEED * direction)
        time.sleep(0.10)

def turn_robot_around():

    direction = 1
    iterations = (14)
    
    for i in range(iterations):
        motor_serial.send_command(TURNING_SPEED * direction, -TURNING_SPEED * direction)
        time.sleep(0.10)

def turn_robot_slight_left():

    direction = -1
    iterations = (1)
    
    for i in range(iterations):
        motor_serial.send_command(TURNING_SPEED * direction, -TURNING_SPEED * direction)
        time.sleep(0.05)

def turn_robot_slight_right():

    direction = 1
    iterations = (1)
    
    for i in range(iterations):
        motor_serial.send_command(TURNING_SPEED * direction, -TURNING_SPEED * direction)
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
# The motor_serial object will inform us when it's time to exit the program
# (say if the program is terminated by the user)
print("Entering loop. Ctrl+c to terminate")
while not motor_serial.shutdown_now :


    ###############################################################
    # This is the start of our loop. Your code goes below.        #
    #                                                             #
    # An example is provided to give you a starting point         #
    # In this example we get the distance readings from each of   #
    # the two distance sensors. Then we multiply each reading     #
    # with a constant gain and use the two resulting numbers      #
    # as commands for each of the two motors.                     #
    #  ________________________________________________________   #
    # |                                                        |  #
    # V                                                           #
    # V                                                           #
    ###############################################################






    # Get and print readings from distance sensors
    dist_1 = motor_serial.get_dist_1()
    dist_2 = motor_serial.get_dist_2()
    dist_3 = motor_serial.get_dist_3()
    dist_4 = motor_serial.get_dist_4()
    print("Dist 1:", dist_1, "   Dist 2:", dist_2, "  Dist 3:", dist_3, "   Dist 4:", dist_4)

    # Check if there is an obstacle in the way
    
    # Obstacle on the left side
    if dist_1 < SIDE_DISTANCE or dist_2 < TURN_DISTANCE:
        # Too close, back up and turn 180 degrees
        if dist_2 < STOP_DISTANCE:
            drive_robot(BACKWARDS, 0.3)
            turn_robot_around()
        else:
            turn_robot_slight_right()
            
    # Obstacle on the right side
    elif dist_3 < TURN_DISTANCE or dist_4 < SIDE_DISTANCE:
        # Too close, back up and turn left
        if dist_3 < STOP_DISTANCE:
            drive_robot(BACKWARDS, 0.3)
            turn_robot_left()
        else:
            turn_robot_slight_left()
            
    # Too much room to the right        
    elif dist_4 < 150:
        if dist_4 > 60:
            drive_robot(FORWARDS, 0.2)
            turn_robot_right()
        else:
            drive_robot(FORWARDS, 0.1)
            
    # If there is nothing in front of the robot it continues driving forwards        
    else:
        drive_robot(FORWARDS, 0.1)
'''
    if dist_1 < TURN_DISTANCE or dist_2 < TURN_DISTANCE or dist_3 < TURN_DISTANCE or dist_4 < TURN_DISTANCE:
        # There is an obstacle in front of the robot
        # Turn slightly to the side with more room
        print("Correcting!")
        if dist_1 < TURN_DISTANCE:
            turn_robot_slight_right()
        elif dist_4 < TURN_DISTANCE:
            turn_robot_slight_left()
        else:
            drive_robot(BACKWARDS, 0.3)
            if dist_1 > dist_4:
                turn_robot_slight_right()
            elif dist_4 > dist_1:
                turn_robot_slight_left()
            else:
                turn_robot_slight_right()
'''


    #elif  dist_2 < STOP_DISTANCE or dist_3 < STOP_DISTANCE:
    #    drive_robot(BACKWARDS, 0.1)
    #    if dist_1 > dist_4:
    #        turn_robot_slight_left()
    #   else:
    #        turn_robot_slight_right()

    #else:
        # If there is nothing in front of the robot it continus driving forwards
        #drive_robot(FORWARDS, 0.1)


        
                



    ###############################################################
    #                                                           A #
    #                                                           A #
    # |_________________________________________________________| #
    #                                                             #
    # This is the end of our loop,                                #
    # execution continus at the start of our loop                 #
    ###############################################################
    ###############################################################





# motor_serial has told us that its time to exit
# we have now exited the loop
# It's only polite to say goodbye
print("Goodbye")
