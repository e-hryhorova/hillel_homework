class ProcessInput:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add_numbers(self):
        return self.a + self.b

    def subtract_numbers(self):
        return self.a - self.b

    def multiple_numbers(self):
        return self.a * self.b

    def divide_numbers(self):
        try:
            return self.a // self.b
        except ZeroDivisionError:
            print('Division by zero!')


process_input = ProcessInput(a=20, b=0)
print(process_input.add_numbers())
print(process_input.subtract_numbers())
print(process_input.multiple_numbers())
print(process_input.divide_numbers())
