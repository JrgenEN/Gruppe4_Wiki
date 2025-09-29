from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port, Stop
from pybricks.robotics import DriveBase

ev3 = EV3Brick()

# Initialize ultrasonic sensor
ultrasonic_sensor = UltrasonicSensor(Port.S4)

# Initialize motors
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

#initialize drive base
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=114)

while True:
    robot.drive(100, 0)  # Move forward at 100 mm/s
    
    while ultrasonic_sensor.distance() < 200:
        robot.stop(Stop.BRAKE)
        robot.turn(90)  # Turn 90 degrees
        
    