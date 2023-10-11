# 388. На вхід програми подається два рядка A і B, що складаються з малих букв англійського 
# алфавіту. Виведіть кількість входжень рядка B в рядок A.
"""
Вхідні дані:
aaaa
a
ababada
abc
abababa
aba

Вихідні дані:
4
0
3
"""
text1 = input("Enter your string: ")
text2 = input("Enter your string: ")
counter = 0

for i in range(len(text1)):
    if text1[i:i+len(text2)] == text2[:]:
        counter += 1
    else:
        continue

print(counter)
    