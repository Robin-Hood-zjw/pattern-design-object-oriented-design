from abc import ABC, abstractmethod


class TVImplementor(ABC):
    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass

    @abstractmethod
    def tune_channel(self):
        pass

class SonyImplementor(TVImplementor):
    def on(self) -> str:
        return 'Sony TV is ON'

    def off(self) -> str:
        return 'Sony TV is OFF'

    def tune_channel(self) -> str:
        return 'Switching Sony TV channel'

class TCLImplementor(TVImplementor):
    def on(self) -> str:
        return 'TCL TV is ON'

    def off(self) -> str:
        return 'TCL TV is OFF'

    def tune_channel(self) -> str:
        return 'Switching TCL TV channel'


class RemoteControl(ABC):
    def __init__(self, implementor)-> None:
        self.implementor = implementor

    def turn_on(self) -> str:
        return self.implementor.on()

    def turn_off(self) -> str:
        return self.implementor.off()

    def switch_channel(self) -> str:
        return self.implementor.tune_channel()

class AdvancedRemoteControl(RemoteControl):
    pass



if __name__ == '__main__':
    Sony_remote = AdvancedRemoteControl(SonyImplementor())
    TCL_remote = AdvancedRemoteControl(TCLImplementor())

    Sony_remote.turn_on()
    Sony_remote.switch_channel()
    Sony_remote.turn_off()

    TCL_remote.turn_on()
    TCL_remote.switch_channel()
    TCL_remote.turn_off()