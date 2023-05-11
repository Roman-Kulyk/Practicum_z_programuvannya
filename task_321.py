# 321. Дано два рядки, що можуть містити пропуски. 
# Виведіть слово Yes, якщо перший рядок є підрядком другого рядка або 
# слово No в іншому випадку.
'''
Вхідні дані:

Lords of the World
But who shall dwell in these worlds if they be inhabited? Are we or they Lords of the World? 
And how are all things made for man?

Вихідні дані:

Yes

'''
s_1 = input("Enter a string: ")
s_2 = input("Enter another string: ")
if s_1 in s_2:
    print("Yes")
else:
    print("No")