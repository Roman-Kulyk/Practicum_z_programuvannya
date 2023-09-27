#811. Напишіть клас з назвою Circle, який містить два методи: для обчислення площі круга та довжину 
# кола за введеним радіусом.
"""
Вхідні дані:
8

Вихідні дані:

200.96
50.24
"""

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def calculate_square(self):
        result = 3.14 * self.radius * self.radius
        print(result)

    def calculate_length(self):
        result = 2 * 3.14 * self.radius
        print(result)

c_1 = Circle(8)
c_1.calculate_square()
c_1.calculate_length()

c_2 = Circle(5)
c_2.calculate_square()
c_2.calculate_length()