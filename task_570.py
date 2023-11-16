# 570. Дано послідовність цілих чисел. Для кожного числа надрукуйте слово YES 
# (в окремому рядку), якщо це число вже зустрічалось в послідовності, і надрукуйте NO, 
# якщо воно ще не було виявлено. Для зберігання значень використайте множину.
"""
Вхідні дані:
1 4 5 2 10 15 4 10 3

Вихідні дані:
NO
NO
NO
NO
NO
NO
YES
YES
NO
"""
lst_1 = [int(item) for item in input("Enter the list members: ").split()]
lst_2 = set()
for i in lst_1:
    
    if i not in lst_2:
        lst_2.add(i)
        print("NO")
    else:
        print("YES")

print(lst_2)