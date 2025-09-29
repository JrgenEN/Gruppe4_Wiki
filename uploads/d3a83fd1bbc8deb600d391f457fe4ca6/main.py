#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
import random


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Initialize the Ultrasonic Sensor, touch sensor and color sensor.
obstacle_sensor = UltrasonicSensor(Port.S4)
touch_sensor = TouchSensor(Port.S3)
line_sensor = ColorSensor(Port.S1)

# Create your objects here.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Calculate the light threshold. Choose values based on your measurements.
BLACK = 5
WHITE = 85
threshold = (BLACK + WHITE) / 2 # Set the threshold to the average of black and white.


# Set the drive speed at 100 millimeters per second.
DRIVE_SPEED = 80

# Set the gain of the proportional line controller. This means that for every
# percentage point of light deviating from the threshold, we set the turn
# rate of the drivebase to 1.2 degrees per second.

# For example, if the light value deviates from the threshold by 10, the robot
# steers at 10*1.2 = 12 degrees per second.
PROPORTIONAL_GAIN = 1.2

start = time.time()

def entertain(): # Function to entertain the user
    rand_nr = random.randint(1, 4) # Generates ranodm number between 1 and 4
    robot.stop() # Stop the robot
    if rand_nr == 1: # If the random number is 1, play fanfare sound
        ev3.speaker.play_file(SoundFile.FANFARE)
    elif rand_nr == 2: # If the random number is 2, play hello sound
        ev3.speaker.play_file(SoundFile.HELLO)
    elif rand_nr == 3: # If the random number is 3, do a little dance
        robot.turn(45)
        robot.turn(-90)
        robot.turn(45)
        
    else: # Else, say "I am a robot"
        ev3.speaker.say("I am a robot")

# Start following the line endlessly.
while True:
    end = time.time() # Get the current time
     # If 10 seconds have passed, play entertainment

    if end - start >= 10: # Check if 10 seconds have passed
        entertain() # Call function entertain
        start = time.time() # Reset the start time to the current time
        
    # Calculate the deviation from the threshold.
    deviation = line_sensor.reflection() - threshold

    # Calculate the turn rate.
    turn_rate = PROPORTIONAL_GAIN * deviation

    # Set the drive base speed and turn rate.
    robot.drive(DRIVE_SPEED, turn_rate)
    
    while obstacle_sensor.distance() < 200: # If an obstacle is detected within 200 mm
        robot.stop() # Stop the robot
        ev3.speaker.play_file(SoundFile.FANFARE) # Play fanfare sound

    # You can wait for a short time or do other things in this loop.
    wait(10)
