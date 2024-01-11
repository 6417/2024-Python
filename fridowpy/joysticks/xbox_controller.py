import wpilib

from .frido_joystick import FridoJoystick

class XboxController(FridoJoystick):
    """Can be used as a joystick, but has more additional functionality"""

    def __init__(self, port: int) -> None:
        self.xbox_controller = wpilib.XboxController(port)

    def getRight(self) -> float:
        return self.xbox_controller.getLeftX()

    def getForward(self) -> float:
        return self.xbox_controller.getLeftY()