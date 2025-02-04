# Needed to define a Pose2d
import wpimath.geometry._geometry as geometry
from wpilib import Field2d

class MotionSimulation():
    """
    The MotionSimulation class is used to create a simulated path that can be sent
    to a Field2d. The Field2d is a graphical representation that is visible in the
    Simulator.
    """
    
    def __init__(self, field: Field2d):
        """
        Initialize the instance variables of the MotionSimulation class
        """
        self.periodicCount = 0
        self.goForward = True
        self.xPos = 0
        self.yPos = 0
        self.field = field
    
    def teleopPeriodic(self):
        """
        Call this method from the robot.py teleopPeriodic method.
        
        This method will periodically update a counter. On every 20th update (400 ms), it will
        increment or decrement the X and Y position (increments when going forward and
        decrements when going back).
        """
        # Every 400 ms increment the position counter by 1 (this method is called once every 20 ms
        # and we use a modulus of 20, which will cause the if statement to be true every twentieth time),
        if self.periodicCount % 20 == 0:            
            # Move the position forward or back once every 200 ms
            if (self.goForward):
                self.xPos += 1
                self.yPos += 1
            else:
                self.xPos -= 1
                self.yPos -= 1
            
        # After 5 position increments, change the direction
        if self.periodicCount >= 100:
            self.periodicCount = 0
            self.goForward = not self.goForward
        
        self.periodicCount += 1
        tempPose = geometry.Pose2d(self.xPos,self.yPos,3)
        self.field.setRobotPose(tempPose)  