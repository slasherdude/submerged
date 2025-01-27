from base_robot import *

#Collect Krills, Plants, release shark, hit corral and get sample
# When we run this program from the master program, we will call this
br = BaseRobot()
br.GyroDrive(150, 400, Stop.COAST_SMART) #drive straight to leave home
br.GyroTurn(15)  #turn to leave home
br.GyroDrive(400, 400, Stop.HOLD) #drive straight to leave home
br.rightAttachmentMotor.run_angle(400, 300) #close front
br.GyroDrive(125, 400, Stop.HOLD) #drive straight to leave home
br.GyroDrive(-100, 400, Stop.HOLD) #drive straight to leave home
br.GyroTurn(-45)  #turn to leave home
br.GyroDrive(97, 400, Stop.HOLD) #drive straight to leave home
br.rightAttachmentMotor.run_angle(400, -250) #close front
br.GyroDrive(90, 400, Stop.HOLD) #drive straight to leave home
br.rightAttachmentMotor.run_angle(1100, 250) #close front
br.GyroDrive(-220, 400, Stop.HOLD) #drive straight to leave home
br.GyroTurn(75)  #turn to leave home
br.GyroDrive(440, 275, Stop.HOLD) #drive straight to leave home
br.rightAttachmentMotor.run_angle(1100, -250) #close front
br.GyroDrive(-50, 400, Stop.HOLD) #drive straight to leave home
br.rightAttachmentMotor.run_angle(1100, 250) #close front
br.GyroDrive(-1200, 400, Stop.HOLD) #drive straight to leave home
#br.Curve(-50,-50)
#br.GyroDrive(-670, 978, Stop.HOLD) #drive straight to leave home





# drive_base.straight(-120)
# RightWheel.run_angle(500, -240)
# drive_base.settings(straight_speed=500)
# drive_base.straight(-600)



# br.GyroDrive(560, 400, Stop.HOLD) #drive straight to leave home
# br.GyroDrive(-38, 400, Stop.HOLD) #drive straight to leave home
# br.rightAttachmentMotor.run_angle(400, 2000) #close front

# br.leftAttachmentMotor.run_angle(3000, 400)  # speed 200, 180 degrees
# br.GyroDrive(-150, 400, Stop.HOLD) #drive straight to leave home
# br.GyroTurn(-13)  #turn to leave home
# br.GyroDrive(-250, 400, Stop.HOLD) #drive straight to leave home
# br.GyroDrive(90, 400, Stop.HOLD) #drive straight to leave home
# br.leftAttachmentMotor.run_angle(3000, -800)  # speed 200, 180 degrees
# br.GyroTurn(25)  #turn to leave home
# br.GyroDrive(-500, 400, Stop.HOLD) #drive straight to leave home


# # br.GyroDrive(180, 400, Stop.HOLD) #drive straight to leave home
# br.rightAttachmentMotor.run_angle(400, 2000) #close front
#br.leftAttachmentMotor.run_angle(3000, -800)  # speed 200, 180 degrees




# The main program starts here.


# RightMotor.run_angle(500, 250)
# drive_base.straight(125)
# drive_base.straight(-100)
# drive_base.turn(-55)
# drive_base.straight(60)
# RightMotor.run_angle(500, -250)
# drive_base.straight(90)
# RightMotor.run_angle(3500, 250)
# drive_base.straight(-120)
# RightWheel.run_angle(500, -240)
# drive_base.settings(straight_speed=500)
# drive_base.straight(-600)
