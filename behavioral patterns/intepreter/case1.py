from abc import ABC


class Expression(ABC):
    def interpret(self) -> None:
        pass

class PrintExpression(Expression):
    def __init__(self, message: str) -> None:
        self.message = message

    def interpret(self) -> None:
        print(self.message)

class RepeatExpression(Expression):
    def __init__(self, count: int, expression: Expression):
        self.count = count
        self.expression = expression

    def interpret(self) -> None:
        for _ in range(self.count):
            self.expression.interpret()

class ReverseExpression(Expression):
    def __init__(self, message: str) -> None:
        self.message = message

    def interpret(self) -> None:
        print(self.message[::-1])



if __name__ == '__main__':
    command = 'REPEAT 2 TIMES: REVERSE Hello'
    words_list = command.split(' ')

    if words_list[0] == 'REPEAT':
        repeat_cnt = int(words_list[1])

        if words_list[3].upper() == 'PRINT':
            expression = PrintExpression(words_list[4])
        elif words_list[3].upper() == 'REVERSE':
            expression = ReverseExpression(words_list[4])
        else:
            expression = ValueError(f'Unsupported command: {words_list[3]}')
        
        repeat_expression = RepeatExpression(repeat_cnt, expression)

        # Interpret the command
        repeat_expression.interpret()