from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    br.GyroDrive(100, 400, Stop.HOLD) #drive straight to leave home
    br.GyroTurn(-60)  #turn to leave home
    br.GyroDrive(230, 400, Stop.HOLD) #drive straight to collect them all
    br.GyroTurn(70) #turning to face the krill before collecting
    br.GyroDrive(400, 400, Stop.HOLD) #drive straight and leave home
    br.GyroTurn(35) #the turn before lowering to get the sample
    br.GyroDrive(65, 400, Stop.HOLD) #drive straight to capture the the sample
    br.rightAttachmentMotor.run_angle(2000, 250) #close front
    

    # br.leftAttachmentMotor.run_angle(200, -150)  # speed 200, 180 degrees
    # br.GyroDrive(1200, 250) #drive across the mat
    # br.GyroDrive(-200, 600) #drive backwards
    # br.leftAttachmentMotor.run_angle(1000, 100)  # raise arm back
    # br.GyroDrive(1000)
    
    #br.GyroTurn(90)
    #br.GyroDrive(275)
    # br.leftAttachmentMotor.run_angle(200, 180)  # speed 200, 180 degrees
    # br.GyroDrive(-25)
    # br.GyroTurn(-90)


# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)