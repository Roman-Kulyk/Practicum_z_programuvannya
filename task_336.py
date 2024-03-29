# 336. Для доступу до власного акаунту на сайті соціальної мережі користувач 
# ввів логін і пароль. 
#Так як була увімкнена двофакторна авторизація, на його 
# телефон прийшло повідомлення з рядком цифр та інформацією як отримати код доступу.
# У повідомленні йшлося: 
#«Кожну цифру, яка більша 5, необхідно націло розділити на 2, 
# а потім з утвореної послідовності цифр видалити усі парні числа». 
# Який код повинен ввести користувач для успішної авторизації? Напишіть програму, 
# на вхід якої вводиться рядок цифр із повідомлення, а програма повинна надрукувати 
# правильний код доступу.
'''
Вхідні дані:
5763
1977
Вихідні дані:
33
33
'''
input_str = input("Enter a row: ")
result = []

for char in input_str:
    char = int(char)
    if char > 5:
        char = char//2
        if char % 2 != 0:
            char = str(char)
            result.append(char)
print("".join(result))