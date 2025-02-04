from magicbot import AutonomousStateMachine, timed_state, state
import wpilib

class PrintDots(AutonomousStateMachine):

    MODE_NAME = "PrintDots"
    DEFAULT = True

    @timed_state(duration=3, first=True)
    def print_dots(self):
        print(".", end = " ")