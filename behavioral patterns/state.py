from abc import ABC

class State(ABC):
    def walk(self) -> None:
        pass

    def run(self) -> None:
        pass

    def jump(self) -> None:
        pass

    def idle(self) -> None:
        pass

class IdleState(State):
    def __init__(self, character) -> None:
        self.character = character

    def idle(self) -> None:
        print('The character is already idle.')

    def walk(self) -> None:
        self.character.state = self.character.walking_state
        print('The character starts walking.')

    def run(self) -> None:
        print('The character cannot run.')

    def jump(self) -> None:
        print('The character cannot jump.')

class WalkingState(State):
    def __init__(self, character) -> None:
        self.character = character

    def idle(self) -> None:
        self.character.state = self.character.idle_state
        print('The character is idle now.')

    def walk(self) -> None:
        print('The character is already walking.')

    def run(self) -> None:
        self.character.state = self.character.running_state
        print('The character is running.')

    def jump(self) -> None:
        print('The character cannot jump.')

class RunningState(State):
    def __init__(self, character) -> None:
        self.character = character

    def idle(self) -> None:
        self.character.state = self.character.idle_state
        print('The character is idle now.')

    def walk(self) -> None:
        print('The character cannot walk.')

    def run(self) -> None:
        print('The character is already running.')

    def jump(self) -> None:
        self.character.state = self.character.jumping_state
        print('The character cannot jump.')

class JumpingState(State):
    def __init__(self, character) -> None:
        self.character = character

    def idle(self) -> None:
        self.character.state = self.character.idle_state
        print('The character is idle now.')

    def walk(self) -> None:
        print('The character cannot walk.')

    def run(self) -> None:
        print('The character cannot run.')

    def jump(self) -> None:
        print('The character is already jumping.')

class Character(ABC):
    def __init__(self) -> None:
        self.idle_state = IdleState(self)
        self.walking_state = WalkingState(self)
        self.running_state = RunningState(self)
        self.jumping_state = JumpingState(self)

        self.state = self.idle_state

    def idle(self) -> None:
        self.state.idle()

    def walk(self) -> None:
        self.state.walk()

    def run(self) -> None:
        self.state.run()

    def jump(self) -> None:
        self.state.jump()



if __name__ == '__main__':
    character = Character()

    character.walk()
    character.run()
    character.jump()
    character.idle()

    character.run()
    character.jump()