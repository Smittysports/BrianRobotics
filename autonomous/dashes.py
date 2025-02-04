from magicbot import AutonomousStateMachine, timed_state, state
import wpilib

class PrintDashes(AutonomousStateMachine):

    MODE_NAME = "PrintDashes"
    DEFAULT = False

    @timed_state(duration=3, first=True)
    def print_dashes(self):
        print("-", end = " ")