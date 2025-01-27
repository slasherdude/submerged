from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase

# Set up all devices.
prime_hub = PrimeHub()
LeftMotor = Motor(Port.D, Direction.CLOCKWISE)
RightMotor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
RightWheel = Motor(Port.B, Direction.CLOCKWISE)
LeftWheel = Motor(Port.A, Direction.COUNTERCLOCKWISE)
drive_base = DriveBase(LeftWheel, RightWheel, 56, 114)


# The main program starts here.
drive_base.settings(turn_rate=50)
drive_base.straight(450)
drive_base.turn(105)
drive_base.straight(350)
LeftMotor.run_angle(500, -280)
RightMotor.run_angle(500, 240)
drive_base.straight(-150)
RightMotor.run_angle(500, -240)
drive_base.settings(turn_rate=150)
drive_base.turn(150)
drive_base.settings(straight_speed=500)
drive_base.straight(450)
