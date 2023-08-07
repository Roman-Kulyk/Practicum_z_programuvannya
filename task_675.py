# 675. Напишіть функцію для перевірки чи є послідовність цілих чисел арифметичною 
# прогресією чи ні. Примітка. У математиці арифметична прогресія або арифметична 
# послідовність - це послідовність чисел, в якій різниця між послідовними членами є 
# постійною. Наприклад, послідовність 5, 7, 9, 11, 13, 15,... є арифметичною 
# прогресією із загальною різницею 2.
'''
Вхідні дані:
5 7 9 11
5 7 10 12

Вихідні дані:
True
False
'''
def if_arithmetic():
    seq = [int(item) for item in input("Enter the list members: ").split(' ')]
    seq = sorted(seq)
    if len(seq) >  1:
        const = seq[1] - seq[0]
    else:
        return True
    for i in range(len(seq) - 1):
        if seq[i + 1] - seq[i] != const:
            return False
    return True


print(if_arithmetic())
