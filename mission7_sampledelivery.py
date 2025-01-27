from base_robot import *

#sample delivery
# When we run this program from the master program, we will call this
br = BaseRobot()
br.GyroDrive(120, 400, Stop.HOLD) #drive straight to leave home
br.GyroTurn(-110)  #turn to leave home
br.GyroDrive(250, 400, Stop.HOLD) #drive straight to leave home

br.leftAttachmentMotor.run_angle(300, -500)  # speed 200, 180 degrees
br.leftAttachmentMotor.run_angle(500, 500)  # speed 200, 180 degrees
br.GyroTurn(110)  #turn to leave home
br.GyroDrive(-110, 400, Stop.HOLD) #drive straight to leave home