# 809. Напишіть клас з назвою Circle для обчислення площі круга за введеним радіусом. 
# Клас Circle має містити метод, який обчислює площу круга.
"""
Вхідні дані:
3

Вихідні дані:
28.26
"""
class Circle():
    def __init__(self, radius):
        self.radius = radius

    def calculate_square(self):
        radius = self.radius
        result = 3.14 * radius * radius
        print(result)

c_1 = Circle(3)
c_1.calculate_square()

c_2 = Circle(5)
c_2.calculate_square()