from abc import ABC


class TextEditor(ABC):
    def __init__(self) -> None:
        self.text_list = list()

    def insert(self, text: str, position: int) -> None:
        if text != ' ':
            self.text_list.insert(position, text)

    def delete(self, start: int, end: int) -> None:
        del self.text_list[start:end]

    def get_text(self) -> str:
        result = ''
        for string in self.text_list:
            result += string
        
        return result


class EditorCommand(ABC):
    def execute(self) -> None:
        pass

    def undo(self) -> None:
        pass

    def redo(self) -> None:
        pass

class InsertCommand(EditorCommand):
    def __init__(self, text: str, editor: TextEditor, position: int) -> None:
        self.text = text
        self.editor = editor
        self.index = position

    def execute(self) -> None:
        self.editor.insert(self.text, self.index)

    def undo(self) -> None:
        self.editor.delete(self.index, self.index + len(self.text))

    def redo(self) -> None:
        self.execute()

class DeleteCommand(EditorCommand):
    def __init__(self, editor: TextEditor, position: int, length: int) -> None:
        self.editor = editor
        self.index = position
        self.length = length
        self.deleted_text = None

    def execute(self) -> None:
        text = self.editor.get_text()
        self.deleted_text = text[self.index : self.index + self.length]
        self.editor.delete(self.index, self.index + self.length)

    def undo(self) -> None:
        if self.deleted_text is not None:
            self.editor.insert(self.deleted_text, self.index)

    def redo(self) -> None:
        self.execute()

class OutputCommand(EditorCommand):
    def __init__(self,  editor: TextEditor) -> None:
        self.editor = editor
    
    def execute(self) -> str:
        return self.editor.get_text()


class Command_Manipulator(ABC):
    def __init__(self) -> None:
        self.history = list()
        self.redo_history = list()

    def execute(self, command: EditorCommand) -> None:
        command.execute()
        self.redo_history.clear()
        self.history.append(command)

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
    # manipulator.execute(DeleteCommand(editor, 5, 2))
    # manipulator.execute(OutputCommand(editor))
    print(editor.get_text())