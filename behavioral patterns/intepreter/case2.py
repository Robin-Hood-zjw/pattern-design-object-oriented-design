from abc import ABC


class Expression(ABC):
    def interpret(self) -> None:
        pass
    
class MathematicalExpression(Expression):
    def __init__(self, tokens) -> None:
        self.result = 0
        self.tokens = tokens
        
    def calculate(self) -> None:
        stack = list()
        i, length = 0, len(self.tokens)
        
        while i < length:
            if self.tokens[i] == '*' or self.tokens[i] == '/':
                operand1 = int(stack.pop())
                operand2 = int(self.tokens[i + 1])
                
                if self.tokens[i] == '*':
                    stack.append(operand1 * operand2)
                elif self.tokens[i] == '/':
                    stack.append(operand1 // operand2)
                
                i += 2
            else:
                stack.append(self.tokens[i])
                i += 1
                
        while stack:
            token = stack.pop(0)
            if token == '+':
                self.result += int(stack.pop(0))
            elif token == '-':
                self.result -= int(stack.pop(0))
            elif token:
                self.result += int(token)
            
        
    def interpret(self) -> None:
        print(self.result)


if __name__ == '__main__':
    expression1 = MathematicalExpression('3 + 4 * 2'.split(' '))
    expression2 = MathematicalExpression('5 * 6 / 3'.split(' '))

    expression1.calculate()
    expression2.calculate()

    expression1.interpret()
    expression2.interpret()
