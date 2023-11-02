# 386. Послідовності із символів 0 і 1 називаються бінарними. Вони широко застосовуються в 
# інформатиці. Одне з незручностей бінарних послідовностей – їх важко запам’ятовувати. Для 
# вирішення цієї проблеми був запропонований такий спосіб їх стиснення: переглядаючи 
# послідовність зліва направо, виконується заміна 1 на a, 01 на b, 001 на c, ..., 
# 00000000000000000000000001 на z. Напишіть програму, яка допоможе автоматизувати такий 
# процес заміни.
"""
Вхідні дані:
1111
1001101
10000101

Вихідні дані:
aaaa
acab
aeb
"""
import re
def seq_decoder(text):
    replacement = {'1':'a','01':'b','001':'c','0001':'d'}

    #formatted_text = text
    for key, value in replacement.items():
    #        formatted_text = formatted_text.replace(key, value)
    #return formatted_text
        text = re.sub(f"(?<!0){key}(?!1)",value, text)
    return text
    
text = input("Enter your text: ")
result = seq_decoder(text)
print(result)