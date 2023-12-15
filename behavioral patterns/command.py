from abc import ABC


class TextEditor(ABC):
    def __init__(self) -> None:
        self.text_list = list()
        self.last_behavior = list()

    def insert(self, text: str, position: int) -> None:
        if text != ' ':
            length = len(self.text_list)
            self.text_list[length - 1] += text
            self.last_behavior[0] = length
            self.last_behavior[1] = text

    def delete(self, start: int, end: int) -> None:
        self.text_list = self.text_list[:start] + self.text_list[end + 1:]

    def get_text(self) -> str:
        return self.text_list.join(' ') + '.'


class Command(ABC):
    def execute(self) -> None:
        pass

    def undo(self) -> None:
        pass

    def redo(self) -> None:
        pass


class InsertCommand(Command):
    def __init__(self, text: str, editor: TextEditor, position: int) -> None:
        self.text = text
        self.editor = editor
        self.index = position

    def execute(self) -> None:
        self.editor.insert(self.text, self.index)

    def undo(self, start: int, end: int) -> None:
        self.editor.delete(start, end)

    def redo(self) -> None:
        self.execute()

class DeleteCommand(Command):
    def __init__(self, editor: TextEditor, position: int, length: int) -> None:
        self.editor = editor
        self.index = position
        self.length = length
        self.deleted_text = None

    def execute(self) -> None:
        text = self.editor.get_text()
        self.deleted_text = text[self.index, self.index + self.length]
        self.editor.delete(self.index, self.index + self.length)

    def undo(self, start: int, end: int) -> None:
        self.editor.delete(start, end)

    def redo(self) -> None:
        self.execute()



class Command_Manipulator(ABC):
    def __init__(self) -> None:
        self.history = list()
        self.redo_history = list()

    def execute(self, command: Command) -> None:
        command.execute()
        self.history.append(command)
        self.redo_history.clear()

    def undo(self) -> None:
        if self.history:
            command = self.history.pop()
            self.history.append(command)
            command.undo()

    def redo(self) -> None:
        if self.redo_history:
            command = self.redo_history.pop()
            self.history.append(command)
            command.redo()



if __name__ == '__main__':
    editor = TextEditor()
    manipulator = Command_Manipulator()

    manipulator.execute(InsertCommand('Hello, ', editor, 0))
    manipulator.execute(InsertCommand('world!', editor, 7))
    manipulator.execute(DeleteCommand(editor, 5, 2))

    editor.get_text()