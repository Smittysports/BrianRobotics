#!/usr/bin/env python3

import logging
from magicbot import MagicRobot
# The Field2d is required to send simulated Pose position to the Network Tables
from wpilib import Field2d
from wpilib import SmartDashboard
from MotionSimulation import MotionSimulation
class Robot(MagicRobot):
    """ The main class used by robotpy. This class is mandatory.
    
    The robot will run periodic tasks based on what state the robot is currently in.
    
    Robot States:
        Disabled:     The robot is currently disabled.
            - See disabledInit() and disabledPeriodic()
        Autonomous:   The robot is coded to act on its own
            - See disabledInit() and disabledPeriodic()
        Teleop:       Remote controlled, usually by a human with a joystick.
            - See teleopInit() and teleopPeriodic()
        Test:         Testing mode
            - See teleopInit() and teleopPeriodic()

    Args:
        MagicRobot (Class): The base class, which itself inherits from wpilib.RobotBase.
    """      
        
    def robotInit(self):
        """
        This method is called as soon as the robot is turned on.
        """
        super().robotInit()
    
        self.logger = logging.getLogger("Brian")
        self.logger.info("Brian's robot is initializing")
        
        # This is just a general purpose counter. I am using it in this example code to allow me
        # to slowly print periodic status updates
        self.indexCount = 0
        self.shouldShowDots = True
        # The Field2d is needed to send Robot pose to the NetworkTables
        self.field = Field2d()
        # The MotionSimulation is used to simulate a moving robot and displays the position in the Simulator using the Field2d
        self.motionSimulation = MotionSimulation(self.field)
        
        # Tell the SmartDashboard about the Field2D
        SmartDashboard.putData("Field", self.field)

    def showDots(self):
        if (self.shouldShowDots):
            if self.indexCount % 250 == 0:
                print(".", end = " ")
                
    def createObjects(self):
        """
        TBD: This method will be utilized in future commits
        """
        ...

    def disabledInit(self):
        """
        Called when disabled state starts
        """
        print("\ndisabledInit")
        self.indexCount = 0

    def disabledPeriodic(self):
        """
        The periodic code that is run in the disable state.
        
        The Amount of time each loop takes is set in the MagicRobot base class.
        It defaults to 20ms and is set with 'control_loop_wait_time = 0.020'
        """
        self.showDots()
        self.indexCount += 1
        
    def autonomousInit(self):
        """
        Called when autonomous state starts for any of the autonomous modes.
        
        The autonomous state does not use an autonomousPeriodic. Instead, a folder must
        exist in the same location as robot.py and it must contain an empty file called
        __init__.py. Additional autonomous files can be created. For this example, we have
        a file named dots.py and a file named dashes.py. The dots.py is the default and the
        dashes.py can be slected using the simulator, in the SmartDashboard section of the
        NetworkTables.
        """
        print("\nautonomousInit")
        self.indexCount = 0
        
    def teleopInit(self):
        """
        Called when teleop state starts
        """
        print("\nteleopInit")
        self.indexCount = 0
        
    def teleopPeriodic(self):
        """
        The periodic code that is run in the teleop state.
        
        This method will call into motionSimulation.teleopPeriodic() in order to simulate a
        moving robot.
        
        The Amount of time each loop takes is set in the MagicRobot base class.
        It defaults to 20ms and is set with 'control_loop_wait_time = 0.020'
        """
        self.motionSimulation.teleopPeriodic()

    def testInit(self):
        """
        Called when test state starts
        """
        print("\ntestInit")
        self.indexCount = 0
        
    def testPeriodic(self):
        """
        The periodic code that is run in the test state.
        
        The Amount of time each loop takes is set in the MagicRobot base class.
        It defaults to 20ms and is set with 'control_loop_wait_time = 0.020'
        """
        self.showDots()
        self.indexCount += 1
    
    def robotPeriodic(self):
        """
        Called last after every state.
        
        This test code simply simulates Robot position by incrementing and decrementing the X and Y
        positions used in a Pose.
        """        
        
        super().robotPeriodic()  

            