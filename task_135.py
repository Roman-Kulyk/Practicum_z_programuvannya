#135. Розробіть програму для виведення інформації про операційну систему, яка встановлена на комп’ютері користувачa, 
#при введенні відповідного номера: 1 - Window, 2 - Linux, 3 - MacOS. Передбачте у роботі програми ситуації, 
#коли користувач вводить інший номер, відмінний від наведених, або програма на вхід отримує порожній рядок.


number = int(input('Enter a number: '))
if number == 1:
    print('Windows')
elif number == 2:
    print('Linux')
elif number == 3:
    print('MacOS')
else:
    print('Incorrect data')