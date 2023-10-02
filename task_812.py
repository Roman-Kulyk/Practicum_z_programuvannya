# 812. Напишіть клас, який має як мінімум два методи: перший - отримати рядок з вводу консолі, 
# другий - друкувати рядок у верхньому регістрі.
"""
Вхідні дані:
python

Вихідні дані:
PYTHON
"""
class InputOutput:

    def input_method(self):
        self.message = input('Enter your message: ')
        

    def output_method(self):
        print(self.message.upper())

manipulator = InputOutput()
manipulator.input_method()
manipulator.output_method()