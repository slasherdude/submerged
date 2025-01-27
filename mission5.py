from base_robot import *

#Whale and Shipping Lanes
# When we run this program from the master program, we will call this
br = BaseRobot()
br.GyroDrive(300, 400, Stop.HOLD) #drive straight to leave home
br.GyroTurn(-30)  #turn to leave home
br.GyroDrive(560, 400, Stop.HOLD) #drive straight to leave home
br.GyroDrive(-38, 400, Stop.HOLD) #drive straight to leave home
br.rightAttachmentMotor.run_angle(400, 2000) #close front

br.leftAttachmentMotor.run_angle(3000, 400)  # speed 200, 180 degrees
br.GyroDrive(-150, 400, Stop.HOLD) #drive straight to leave home
br.GyroTurn(-13)  #turn to leave home
br.GyroDrive(-250, 400, Stop.HOLD) #drive straight to leave home
br.GyroDrive(90, 400, Stop.HOLD) #drive straight to leave home
br.leftAttachmentMotor.run_angle(3000, -800)  # speed 200, 180 degrees
br.GyroTurn(25)  #turn to leave home
br.GyroDrive(-500, 400, Stop.HOLD) #drive straight to leave home


# # br.GyroDrive(180, 400, Stop.HOLD) #drive straight to leave home
# br.rightAttachmentMotor.run_angle(400, 2000) #close front
#br.leftAttachmentMotor.run_angle(3000, -800)  # speed 200, 180 degrees