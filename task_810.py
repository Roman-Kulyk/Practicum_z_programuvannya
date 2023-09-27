# 810. Напишіть клас під назвою Rectangle для визначення площі прямокутника за введеними довжиною та 
# шириною сторін. Клас прямокутника має містити метод, який обчислює площу прямокутника.
"""
Вхідні дані:
2
3

Вихідні дані:
6
"""
class Rectangle():
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_square(self):
        result = self.height * self.width
        print(result)

r_1 = Rectangle(2,3)
r_1.calculate_square()

r_2 = Rectangle(4,5)
r_2.calculate_square()