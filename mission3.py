from base_robot import *

br = BaseRobot()
br.rightAttachmentMotor.run_angle(2000, 200) #close front
br.GyroDrive(250, 400, Stop.HOLD) #drive straight and leave home
br.GyroTurn(90)
br.leftAttachmentMotor.run_angle(200, -150)  # speed 200, 180 degrees
br.GyroDrive(1200, 250) #drive across the mat
br.GyroDrive(-200, 600) #drive backwards
br.leftAttachmentMotor.run_angle(1000, 100)  # raise arm back
br.GyroDrive(1000)