import numpy as np

import phoenix6 as phx
import wpilib

from fridowpy.joysticks.xbox_controller import XboxController
from src.drive.motors import Motors

SPEED_FACTOR: float = 1.0 / 5.0
MAX_SPEED: float = 1.0

def scale_speed(s: float) -> float:
    sigmoid = lambda s: 2 / (1 + np.float_power(np.e, -s)) - 1
    return max(-MAX_SPEED, min(MAX_SPEED, sigmoid(s)))

class MainRobot(wpilib.TimedRobot):

    def robotInit(self):
        self.motors = Motors(
            left_motors=(12, 0),
            right_motors=(13, 11),
            left_inverted=True,
            right_inverted=False,
            oppose_direction_left=True,
            oppose_direction_right=False)
        self.joystick = XboxController(0)

    def teleopPeriodic(self):
        fwd = -scale_speed(self.joystick.getForward())
        # rot = self.joystick.getRight()
        rot = 0

        self.motors.drive(fwd, rot)

    def _simulationPeriodic(self):
        if wpilib.DriverStation.isEnabled():
            phx.unmanaged.feed_enable(100)

