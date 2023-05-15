# 342. Дано рядок, що складається з слів, розділених пропусками. 
# Визначте кількість слів у рядку.
'''
Вхідні дані:
Events happened very rapidly with Francis Morgan that late spring morning
Вихідні дані:
11
'''
txt = input("Enter a string: ")

print(len(txt.split()))