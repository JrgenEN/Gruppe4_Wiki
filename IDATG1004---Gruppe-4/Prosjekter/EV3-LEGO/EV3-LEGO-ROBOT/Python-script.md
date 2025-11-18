[main.py](uploads/c7f00342689fcbde7c6c059cfbbc1a26/main.py)
```python 
#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Import necessary modules from the pybricks library
# These libraries came with the project creation

# Initialize EV3 and motors
ev3 = EV3Brick() # Create an instance of the EV3 brick
left_motor = Motor(Port.B) # Create an instance of the left motor
right_motor = Motor(Port.C) #  Create an instance of the right motor


# Prints text on screen
ev3.screen.clear() # Clear the screen
ev3.screen.print("Hello World") # Print "Hello World" on the LCD screen
wait(2000) # Wait for 2 seconds
ev3.screen.clear() # Clears screen

# Function to drive straight
def drive_forward(speed, time_ms): # Parameters: speed and time in milliseconds
    left_motor.run_time(speed, time_ms, Stop.BRAKE, False) # Left motor with parameters (speed, time, stop, wait)
    right_motor.run_time(speed, time_ms, Stop.BRAKE, True) # Right motor with parameters (speed, time, stop, wait)

# Function to turn 90 degrees to the right
def turn_right(speed, time_ms): # Parameters: speed and time in milliseconds
    left_motor.run_time(speed, time_ms, Stop.BRAKE, False) # Left motor with parameters (speed, time, stop, wait)
    right_motor.run_time(-speed, time_ms, Stop.BRAKE, True) # Right motor with parameters (-speed, time, stop, wait)

# Drive a rectangle
for i in range(4): # For-loop that repats 4 times, with variable "i"
    drive_forward(300, 2000)   # Drive forward with speed 300, for 2 seconds
    turn_right(300, 800)      # Turn right with speed 300, for 0.8 seconds

# When finished, say "Have a nice day"
ev3.speaker.say("Have a nice day")