# 548. Створіть словник, який відображає ідентифікатори акцій на біржі. 
# Ключами словника є ідентифікатори акцій, а значеннями - дійсні числа - ціни акцій. 
# На основі цього словника створіть програмно словник із значеннями акцій 
# технологічних компаній.
'''
Вхідні дані:
Немає

Вихідні дані:
AAPL 612.78
IBM 205.55
HPQ 37.2
'''
dictionary ={
    'HPQ':37.2,
    'AAPL':612.78, 
    'IBM':205.55 
    }
for key,value in dictionary.items():
    print(key,value,sep = " ")