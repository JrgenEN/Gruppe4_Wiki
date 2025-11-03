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
SPEED = 100
WHEEL_DIAMETER = 54
AXLE_TRACK = 200


# Create your objects here.
ev3 = EV3Brick()
# Define the Robot class.
class Robot:
    # Initialize the robot.
    def __init__(self):
        left_motor = Motor(Port.B)
        right_motor = Motor(Port.D)
        self.spade = Motor(Port.A)
        self.robot = DriveBase(left_motor, right_motor, WHEEL_DIAMETER, AXLE_TRACK)
        self.running = False
        self.ultrasonic = UltrasonicSensor(Port.S3)
        self.pickup = False
    # Drive forward.
    def drive(self):
        self.robot.drive(SPEED, 0)
        self.running = True
    # Get distance from ultrasonic sensor.
    def distance(self):
        return self.ultrasonic.distance()
        
    # Handle obstacle Pick it up.
    def obstacle(self):
        self.pickup = True
        self.robot.stop()
        self.spade.run_angle(-50, 210)
        wait(210)
        self.robot.straight(150)
        wait(250)
        self.spade.run_angle(-50, -210)
        wait(1000)
        self.running = False
        self.pickup = False
    # Main program loop.
    def run(self):
        while True:
            if self.distance() < 200 and self.pickup == False:
                self.obstacle()
            if self.running == False:
                self.drive()
        
# Create and run the robot.
robot = Robot()
robot.run()
    