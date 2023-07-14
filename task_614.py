# 614. Напишіть функцію, яка перевіряє, чи існує трикутник із введеними 
# сторонами a, b, c.
'''
Вхідні дані:
2 2 1
1 2 4

Вихідні дані:
True
False
'''
def triangle(var_1,var_2,var_3):
    cars = [var_1, var_2, var_3]
    cars.sort(reverse=True)
    
    if cars[0] < (cars[1] + cars[2]):
        print("True")
    else:
        print("False")


triangle(2,2,1)
triangle(1,2,4)
