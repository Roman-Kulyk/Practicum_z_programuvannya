# 585.Дано рядок слів, розділених пропусками. Надрукуйте довжину найдовшого слова.
"""
Вхідні дані:
aaa aaaaa aa a aaaaa

Вихідні дані:
5
"""
text = input("Enter your list members: ").split()
print(len(max(text)))