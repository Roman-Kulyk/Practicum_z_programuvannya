# 546. Створіть словник, який відображає ідентифікатори акцій на біржі. 
# Ключами словника є ідентифікатори акцій, а значеннями - дійсні числа - ціни акцій. 
# Надрукуйте ціни акцій та ідентифікатори у порядку зростання ціни.
'''
Вхідні дані:
Немає

Вихідні дані:
10.75 FB
37.2 HPQ
45.23 ACME
205.55 IBM
612.78 AAPL
'''
dictionary ={
    'FB':10.75,
    'ACME':45.23,
    'HPQ':37.2,
    'AAPL':612.78, 
    'IBM':205.55 
    }

sorted_dictionary = sorted(dictionary.items(), key = lambda x:x[1])
converted_dict = dict(sorted_dictionary)
for key,value in converted_dict.items():
    print(key,',',value,sep = " ")