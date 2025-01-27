from base_robot import *

#sample delivery
# When we run this program from the master program, we will call this
br = BaseRobot()
print(br.rightAttachmentMotor.control.limits())
br.GyroDrive(150, 500, Stop.HOLD) #drive straight to leave home
br.GyroTurn(-95)
br.GyroDrive(245, 500, Stop.HOLD)
br.rightAttachmentMotor.run_angle(1100, -200)
br.GyroDrive(-100, 500, Stop.HOLD)
br.leftAttachmentMotor.run_angwwle(600, 600)
br.GyroDrive(300, 500, Stop.HOLD)
#br.leftAttachmentMotor.run_angle(500, -1200)
#br.GyroDrive(150, -100, Stop.HOLD)
#br.Curve(190,-110)
#br.rightAttachmentMotor.dc(100)  
#br.rightAttachmentMotor.run_angle(1100, -200)  # speed 200, 180 degrees

# print(br.rightAttachmentMotor.control.limits())






# br.GyroDrive(600, 400, Stop.HOLD) #drive straight to leave home
# br.GyroTurn(41)  #turn to leave home
# br.GyroDrive(220, 400, Stop.HOLD) #drive straight to leave home

# br.leftAttachmentMotor.run_angle(300, -400)  # speed 200, 180 degrees
# br.leftAttachmentMotor.run_angle(500, 500)  # speed 200, 180 degrees
# br.GyroDrive(-260, 400, Stop.HOLD) #drive straight to leave home
# br.GyroTurn(-100)  #turn to leave home
# br.leftAttachmentMotor.run_angle(500, -500)  # speed 200, 180 degrees
# br.GyroDrive(500, 400, Stop.HOLD) #drive straight to leave home
# #br.GyroDrive(-30, 400, Stop.HOLD) #drive straight to leave home
# br.leftAttachmentMotor.run_angle(500, 250)  # speed 200, 180 degrees
# wait(5)
# br.GyroDrive(-30, 400, Stop.HOLD) #drive straight to leave home
# br.GyroTurn(-100)  #turn to leave home
# br.GyroDrive(300, 400, Stop.HOLD) #drive straight to leave home
# # br.GyroTurn(110)  #turn to leave home
# # br.GyroDrive(-110, 400, Stop.HOLD) #drive straight to leave home