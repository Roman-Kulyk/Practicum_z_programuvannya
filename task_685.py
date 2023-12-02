# 685. Напишіть програму, яка обчислює площі трикутника, круга і прямокутника, реалізувавши 
# для кожної фігури окрему функцію. Напишіть окрему функцію, яка визначає, площу якої фігури 
# необхідно обчислити, тобто отримує назву фігури і вхідні дані (дійсні числа) для обчислення 
# площі. З деякими вхідними даними триктуник може не існувати, тому реалізуйте ще одну функцію 
# для перевірки існування трикутника.
"""
Вхідні дані:
triangle
1 0 1
circle
5
rectangle
2 7
triangle
2 2 1

Вихідні дані:
triangle does not exist
78.50
14.00
0.97
"""
import math 
import inspect  
def area_triangle(a, b, c):
    p = (a + b + c)/2
    return ((p*(p - a)*(p - b)*(p - c)) ** 0.5)
    

def area_rectangle(a, b):
    return a * b
    

def area_circle(D):
    return 3.14 * D ** 2
    
    
def check_if_triangle_exist(a, b, c):
    return a + b > c and b + c > a and c + a> b

def calculate_area(shape, *args):
    if shape == "triangle":
        if check_if_triangle_exist(*args):
            return area_triangle(*args)
        else:
            return "Triangle doesn't exist!"
    elif shape == "circle":
        return area_circle(*args)
    elif shape == "rectangle":
        return area_rectangle(*args)
    else:
        return("Unknown shape!")

shape_name = input("Enter a shape name: ")
input_data = [float(input(f"Enter parameter {i + 1}: "))for i in
range(len(inspect.signature(globals()
[f'area_{shape_name}']).parameters))]
result = calculate_area(shape_name, *input_data)
print(f"Area {shape_name} is equal: {result:.2f}")


