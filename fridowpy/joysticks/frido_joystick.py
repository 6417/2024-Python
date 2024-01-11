import abc

class FridoJoystick(abc.ABC):

    @abc.abstractmethod
    def __init__(self) -> None: pass

    @abc.abstractmethod
    def getRight(self) -> float:
        raise NotImplementedError()

    @abc.abstractmethod
    def getForward(self) -> float:
        raise NotImplementedError()
