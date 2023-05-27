# 374. Дано два слова. Складіть програму, що визначає чи можна чи ні з букв 
# слова A скласти слово B. Програма має враховувати регістр літер введених слів.
'''
Вхідні дані:
Python
not
Ruby
Buy

Вихідні дані:
Yes
No
'''
a = input("Enter a string: ")
b = input("Enter another string: ")

if all(c in a for c in b):
    print("Yes")
else:
    print("No")