class CalculatorError(Exception):
    pass

class ExpressionParser:
    def parse(self, expression):
        parts = expression.split()
        if len(parts) != 3:
            raise CalculatorError("Expression must be in the format: number operator number")
        num1,operator,num2 = parts
        try:
            num1=float(num1)
            num2 = float(num2)
        except ValueError:
            raise CalculatorError("Invalid Number")
        return num1,operator,num2

class calculatorEngine:
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiply(slef,a,b):
        return a*b
    def divide(self,a,b):
        if b==0:
            raise CalculatorError("Cannot divide by zero")
        return a/b
    def compute(self,a,operator,b):
        if operator == "+":
            return self.add(a,b)
        elif operator == "-":
            return self.subtract(a,b)
        elif operator == "*":
            return self.multiply(a,b)
        elif operator == "/":
            return self.divide(a,b)
        else:
            raise CalculatorError("Invalid Operator")
class Calculator:
    def __init__(self):
        self.parser = ExpressionParser()
        self.engine = calculatorEngine()
    def run(self):
        print("welcome to python calculator program shell")
        print("The expression should be like number operator number i.e : 25 + 25")
        print("Type 'exit' to quit the program")
        while True:
            expression =input("Enter xpression:")
            if expression.lower() == 'exit':
                print("Bye~~~~~~~~~~~")
                break
            try:
                num1, operator, num2 = self.parser.parse(expression)
                result = self.engine.compute(num1, operator, num2)
                print(f"Result: {result}")
            except CalculatorError as e:
                print(f'Error: {e}')
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    calc = Calculator()
    calc.run()