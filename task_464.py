# 464. На вхід програми подається деякий текст в одному рядку з пропусками. Необхідно знайти у тексті слово під певним номером (наприклад, п’яте слово за рахунком)
# і вивести на екран його першу букву.
'''
Вхідні дані:
Now is better than never
3

Вихідні дані:
b
'''
txt = input("Enter your text: ").split()
char = int(input("Enter your number: "))

print(txt[char -1][0])