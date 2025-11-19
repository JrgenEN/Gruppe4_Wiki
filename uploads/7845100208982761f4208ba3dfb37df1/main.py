#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from time import sleep

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.
# This program requires the pybricks-micropython environment.
SPEED = 245 # mm/s                                                                       # Speed of the robot
# data = DataLog("TurnRate", "LeftSensor", "RightSensor", "LeftDeviation", "RightDeviation")  # DataLog to store data

EV3 = EV3Brick()                                                                            # Create your objects here. 

class RallyCar():                           # Define the RallyCar class
    def __init__(self):
        leftMotor = Motor(Port.A)
        rightMotor = Motor(Port.D)
        self.robot = DriveBase(leftMotor, rightMotor, wheel_diameter = 56, axle_track = 114)
        self.right_color_sensor = ColorSensor(Port.S1)
        self.left_color_sensor = ColorSensor(Port.S4)
        self.touch_sensor = TouchSensor(Port.S2)
        self.running = False
        self.whiteLeft = 0
        self.blackLeft = 0
        self.whiteRight = 0
        self.blackRight = 0
        self.tresholdLeft = 0
        self.tresholdRight = 0
        self.calibrated = False
        self.swing_skale = 0.82 # Adjust this value to change the responsiveness of the robot

    def run(self):
        while not self.running:
            if not self.calibrated:
                self.calibrate_sensors()
            if self.touch_sensor.pressed():
                    self.running = True
        while self.running:
            self.follow_line()
                
        

    def follow_line(self):
        deviation_right = self.right_color_sensor.reflection() - self.tresholdRight
        deviation_left = self.left_color_sensor.reflection() - self.tresholdLeft
        
        turn_rate = self.swing_skale * (deviation_right - deviation_left)
        #data.log(turn_rate, self.left_color_sensor.reflection(), self.right_color_sensor.reflection(), deviation_left, deviation_right)   
        if self.left_color_sensor.reflection() > (self.whiteLeft-20) and self.right_color_sensor.reflection() > (self.whiteRight-20):
            self.robot.drive(SPEED, -10)
        else:
            self.robot.drive(SPEED, turn_rate)
        
        wait(10)
        
    def calibrate_sensors(self):
        EV3.screen.print(self.right_color_sensor.reflection())
        EV3.screen.print("White Calibration: Press to set")
        sleep(1)  # Give user time to read
        while True:
            if self.touch_sensor.pressed():
                self.whiteRight = self.right_color_sensor.reflection()
                self.whiteLeft = self.left_color_sensor.reflection()
                sleep(1)  # Debounce delay
                break
        EV3.screen.print(self.right_color_sensor.reflection())
        EV3.screen.print("Black Calibration Left: Press to set")
        while True:
            if self.touch_sensor.pressed():
                self.blackLeft = self.left_color_sensor.reflection()
                sleep(1)  # Debounce delay
                break
        EV3.screen.print(self.right_color_sensor.reflection())
        EV3.screen.print("Black Calibration Right: Press to set")
        while True:
            if self.touch_sensor.pressed():
                self.blackRight = self.right_color_sensor.reflection()
                sleep(1)  # Debounce delay
                break


        self.tresholdLeft = (self.whiteLeft + self.blackLeft) / 2
        self.tresholdRight = (self.whiteRight + self.blackRight) / 2
        EV3.screen.clear()
        EV3.screen.print("Calibration Done")
        self.calibrated = True

    

rally_robot = RallyCar()
rally_robot.run()