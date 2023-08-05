# 657. Дано дійсне додатне число a і ціле число n, яке може набувати додатних і 
# від’ємних значень. Напишіть функцію для обчислення an. Стандартною функцією 
# піднесення до степеня і оператором ** користуватися не можна.
'''
Вхідні дані:
2
1
2
-1

Вихідні дані:
2.0
0.5
'''
def power_to_func(a,n):
    result = 1
    if n > 0:
        for i in range(n):
            result *= a
    elif n < 0:
        for i in range(abs(n)):
            result /= a
    return result

print(power_to_func(2,1))
print(power_to_func(2,-1))
