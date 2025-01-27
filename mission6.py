from base_robot import *

#plants
# When we run this program from the master program, we will call this
br = BaseRobot()
br.GyroDrive(50, 100, Stop.HOLD) #drive straight to leave home
br.GyroDrive(-50, 100, Stop.HOLD) #drive straight to leave home
