# 266. Камера спостереження реєструє в автоматичному режимі швидкість проїжджаючих повз неї автомобілів, 
# округляючи значення швидкості до цілих чисел. Необхідно визначити: різницю максимальної і мінімальної 
# швидкостей автомобілів; кількість автомобілів, швидкість яких не перевищувала 30 км/год. Програма отримує 
# на вхід число зафіксованих автомобілів n (1 ≤ n ≤ 30), потім вказуються їх швидкості. Значення швидкості 
# не може бути менше 1 і більше 300. Програма повинна спочатку вивести різницю максимальної та мінімальної 
# швидкостей автомобілів, потім кількість автомобілів, швидкість яких не перевищувала 30 км/год.

'''
Вхідні дані:

3
15
25
140

Вихідні дані:

125
2

'''

n = int(input("Enter a number: "))
num_list_min = []
num_list_max = []
for i in range(0,n):
    speed = int(input("Enter a number: "))
    if speed < 30:
        num_list_min.append(speed)
    else:
        num_list_max.append(speed)

max_sp = max(num_list_max)
min_sp = min(num_list_min)
    
print(max_sp - min_sp)
print(len(num_list_min))
