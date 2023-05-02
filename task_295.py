# 295. Вводяться два чотирицифрових числа a і b. 
# Виведіть у порядку зростання всі чотирицифрові числа в інтервалі від a до b, 
# запис яких містить тільки три однакові цифри.
'''
Вхідні дані:

1400
1600

Вихідні дані:

1411
1444
1511
1555

'''
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
for i in range(a,b):
    fir_num = i // 1000
    sec_num = i % 1000 // 100
    thir_num = i % 100 // 10
    fou_num = i % 10
    if fir_num == sec_num == thir_num\
        or fir_num == sec_num == fou_num\
        or fir_num == thir_num == fou_num\
        or sec_num == fir_num == fou_num\
        or sec_num == thir_num == fou_num\
        or thir_num == sec_num == fou_num:
        print(i) 
