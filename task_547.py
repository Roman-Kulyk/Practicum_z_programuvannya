# 547.Створіть словник, який відображає ідентифікатори акцій на біржі. 
# Ключами словника є ідентифікатори акцій, а значеннями - дійсні числа - ціни акцій. 
# На основі цього словника створіть програмно словник, 
# який містить значення цін акцій, які більше якогось введеного цілого значення n, 
# і виведіть елементи другого словника.
'''
Вхідні дані:
200

Вихідні дані:
AAPL 612.78
IBM 205.55
'''
dictionary ={
    'FB':10.75,
    'ACME':45.23,
    'HPQ':37.2,
    'AAPL':612.78, 
    'IBM':205.55 
    }
rate = int(input("Enter your highest rate: "))
'''
sorted_dictionary = sorted(dictionary.items(), key = lambda x:x[1])
converted_dict = dict(sorted_dictionary)

for key,value in converted_dict.items():
    if value > rate:
        print(key,',',value,sep = " ")
'''
for key,value in dictionary.items():
    if value > rate:
        print(key,',',value,sep = " ")