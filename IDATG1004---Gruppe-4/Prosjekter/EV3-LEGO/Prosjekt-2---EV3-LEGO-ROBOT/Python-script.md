[main.py](uploads/b083b740bda532145574bb7aeffece8c/main.py)
```python
#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

# Initialize ultrasonic sensor, touch sensor
ultrasonic_sensor = UltrasonicSensor(Port.S4)
touch_sensor = TouchSensor(Port.S1)

# Initialize motors
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

#initialize drive base
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=114)
    
while True:
    if touch_sensor.pressed():                          # Start the program when the touch sensor is pressed
        ev3.speaker.say("Exercise 2")                   # Announce the start of the exercise
        while True:                                     # Main loop
            robot.drive(150, 0)                         # Move forward at 150 mm/s
            if touch_sensor.pressed():                  # Stop the program when the touch sensor is pressed again
                robot.stop(Stop.BRAKE)                  # Stop the robot
                ev3.speaker.say("Exercise done")        # Announce the end of the exercise
                break                                   # Exit the inner loop to stop the program
            while ultrasonic_sensor.distance() < 300:   # If an obstacle is detected within 300 mm
                robot.stop(Stop.BRAKE)                  # Stop the robot
                robot.turn(30)                          # Turn 30 degrees
        break                                           # Exit the outer loop to end the program