import phoenix6 as phx

class Motors:
    def __init__(self,
                 left_motors: tuple[int, int],
                 right_motors: tuple[int, int],
                 left_inverted: bool = False,
                 right_inverted: bool = False,
                 oppose_direction_left: bool = False,   # Wether one of the left motors should be inverted
                 oppose_direction_right: bool = False,  # Wether one of the right motors should be inverted
                 ) -> None:

        # Initialize the motors
        self.master_left_motor = phx.hardware.TalonFX(left_motors[0])
        self.follower_left_motor = phx.hardware.TalonFX(left_motors[1])
        self.master_right_motor = phx.hardware.TalonFX(right_motors[0])
        self.follower_right_motor = phx.hardware.TalonFX(right_motors[1])

        # Configure front right motor
        right_motor_config = phx.configs.MotorOutputConfigs()
        if left_inverted:
            right_motor_config.inverted = phx.configs.talon_fx_configs.InvertedValue.COUNTER_CLOCKWISE_POSITIVE
        self.master_right_motor.configurator.apply(right_motor_config)

        # Configure front left motor
        right_motor_config = phx.configs.MotorOutputConfigs()
        if right_inverted:
            right_motor_config.inverted = phx.configs.talon_fx_configs.InvertedValue.COUNTER_CLOCKWISE_POSITIVE
        self.master_left_motor.configurator.apply(right_motor_config)

        # Configure the follwer motors to follow the master motors
        follow_left_request = phx.controls.Follower(0, oppose_direction_left)
        self.follower_left_motor.set_control(follow_left_request)

        follow_right_request = phx.controls.Follower(2, oppose_direction_right)
        self.follower_right_motor.set_control(follow_right_request)

        # Duty cycles
        self.left_out = phx.controls.DutyCycleOut(output=0)
        self.right_out = phx.controls.DutyCycleOut(output=0)
    
    def drive(self, fwd: float, rot: float) -> None:
        self.master_left_motor.set_control(self.left_out.with_output(rot + fwd))
        self.master_right_motor.set_control(self.right_out.with_output(rot - fwd))