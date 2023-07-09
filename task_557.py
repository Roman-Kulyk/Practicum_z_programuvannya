# 557. У вхідному рядку записана послідовність чисел через пропуск. 
# Для кожного числа виведіть слово YES (в окремому рядку), якщо це число раніше 
# зустрічалося в послідовності або NO, якщо не зустрічалося. Вводиться список чисел. 
# Всі числа списку знаходяться на одному рядку. Для зберігання значень використайте 
# словник.
'''
Вхідні дані:
4 6 1 8 4 9 0 1

Вихідні дані:
NO
NO
NO
NO
YES
NO
NO
YES
'''
sequence = input("Enter a sequence of letter: ").split()
print(sequence)
sequence_list = []
for i in sequence:
    if i not in sequence_list:
        sequence_list.append(i)
        print("NO")
    else:
        sequence_list.append(i)
        print("YES")