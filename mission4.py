from base_robot import *

# When we run this program from the master program, we will call this
br = BaseRobot()
br.GyroDrive(100, 400, Stop.HOLD) #drive straight to leave home
br.GyroTurn(-60)  #turn to leave home
br.GyroDrive(230, 400, Stop.HOLD) #drive straight to collect them all
br.GyroTurn(70) #turning to face the krill before collecting
br.GyroDrive(400, 400, Stop.HOLD) #drive straight and leave home
br.GyroTurn(35) #the turn before lowering to get the sample
br.GyroDrive(65, 400, Stop.HOLD) #drive straight to capture the the sample
br.rightAttachmentMotor.run_angle(2000, 250) #close front
br.GyroDrive(-150, 400, Stop.HOLD) #drive straight to capture the the sample

br.GyroTurn(-60) #the turn before lowering to get the sample
br.GyroDrive(-340, 400, Stop.HOLD) #drive straight to capture the the sample
br.GyroTurn(-50) #the turn before lowering to get the sample
br.GyroDrive(200, 400, Stop.HOLD) #drive straight to capture the the sample
br.GyroDrive(-500, 400, Stop.HOLD) #drive straight to capture the the sample

# br.GyroTurn(-47) #turning to face the krill before collecting
# br.GyroDrive(-500, 400, Stop.HOLD) #drive straight to leave home