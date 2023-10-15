# 399. Кодування довжин послідовностей - це базовий алгоритм стиснення даних. Реалізуйте 
# один з найпростіших його варіантів. На вхід алгоритму подається рядок, що містить символи 
# англійського алфавіту. Цей рядок розбивається на групи однакових символів, що йдуть підряд 
# («серії»). Кожна серія характеризується символом і кількістю повторень. Саме ця інформація 
# і записується в код: спочатку пишеться довжина серії повторюваних символів, потім сам 
# символ. У серій довжиною в один символ кількість повторень не записується.
"""
Вхідні дані:
aaabccccCCaB
aabcccddffffffffff

Вихідні дані:
3ab4c2CaB
2ab3c2d10f
"""
def str_coding(text):
    coded_str = ""
    counter = 1

    for i in range(len(text)-1):
        if text[i] == text[i + 1]:
            counter += 1
        else:
            coded_str += str(counter) + text[i]
            counter = 1  

    coded_str += str(counter) + text[-1]
    return coded_str

text = input("Enter your string: ")
coded_str = str_coding(text)
print(coded_str)