# 645. Дано два дійсних числа x і y. Напишіть функцію для перевірки, чи належить 
# точка з координатами (x, y) ромбу (включаючи його межу), що має розміри 1 х 1 
# клітинки і розташований в початку системи координат. Якщо точка належить ромбу, 
# виведіть слово YES, інакше виведіть слово NO. Функція не повинна містити 
# інструкцію «якщо».
'''
Вхідні дані:
1
1
-0.6
0.3

Вихідні дані:
NO
YES
'''
def romb_func(x, y):
    result = "YES" if -1 <=x <= 0 and -1 <= y <= 1 else "NO"
    return result

print(romb_func(1,1))
print(romb_func(-0.6,0.3))