from .frido_joystick import FridoJoystick

class LogitechExtreme(FridoJoystick):
    def __init__(self, port: int) -> None: pass

    def getRight(self) -> float:
        raise NotImplementedError()

    def getForward(self) -> float:
        raise NotImplementedError()
