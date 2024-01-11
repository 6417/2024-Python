from phoenix6 import hardware, controls, unmanaged
import wpilib

class Mike2(wpilib.TimedRobot):

    def robotInit(self):
        # self.front_left_motor = hardware.TalonFX(0)
        self.rear_left_motor = hardware.TalonFX(12)
        # self.front_right_motor = hardware.TalonFX(13)
        # self.rear_right_motor = hardware.TalonFX(12)

        self.left_out = controls.DutyCycleOut(output=0)
        self.joystick = wpilib.Joystick(0)

    def teleopPeriodic(self):
        self.rear_left_motor.set_control(self.left_out.with_output(self.joystick.getX()))

    def _simulationPeriodic(self):
        if wpilib.DriverStation.isEnabled():
            unmanaged.feed_enable(100)
