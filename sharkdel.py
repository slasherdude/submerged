from base_robot import *

#sample delivery
# When we run this program from the master program, we will call this
br = BaseRobot()
br.GyroDrive(700, 1000, Stop.BRAKE) #drive straight to leave home
br.GyroDrive(-700, 1000,Stop.BRAKE) #drive straight to leave home
# br.GyroTurn(41)  #turn to leave home
# br.GyroDrive(220, 400, Stop.HOLD) #drive straight to leave home

# br.leftAttachmentMotor.run_angle(300, -400)  # speed 200, 180 degrees
# br.leftAttachmentMotor.run_angle(500, 500)  # speed 200, 180 degrees
# br.GyroDrive(-260, 400, Stop.HOLD) #drive straight to leave home
# br.GyroTurn(-100)  #turn to leave home
# br.leftAttachmentMotor.run_angle(500, -500)  # speed 200, 180 degrees
# br.GyroDrive(650, 400, Stop.HOLD) #drive straight to leave home
# br.GyroDrive(-30, 400, Stop.HOLD) #drive straight to leave home
# br.leftAttachmentMotor.run_angle(500, 250)  # speed 200, 180 degrees
# wait(5)
# br.GyroDrive(-30, 400, Stop.HOLD) #drive straight to leave home
# br.GyroTurn(-100)  #turn to leave home
# br.GyroDrive(300, 400, Stop.HOLD) #drive straight to leave home
# br.GyroTurn(110)  #turn to leave home
# br.GyroDrive(-110, 400, Stop.HOLD) #drive straight to leave home