# 389. Користувач вводить рядок цифр без пропусків. Необхідно написати програму, 
# яка «розіб’є» це число на трійки цифр справа наліво комами. Якщо число містить менше 
# трьох цифр, то воно виводиться без змін.
"""
Вхідні дані:
4567
123
2348906

Вихідні дані:
4,567
123
2,348,906
"""

def split_to_three(num):
    length = len(num)

    if length <= 3:#if length of num less than 3 
        return num#it returnss num without any action
    else:
        splitted_threes = []#it initialize an empty list where the threes will be stored
        for i in range(length//3):
            beginning = length - (i + 1) * 3#it calculates index of slice's beginning
            ending = length - i * 3#it calculates index of slice's ending
            threes = num[beginning:ending]#it assigns slice's value
            #to the threes variable
            splitted_threes.insert(0, threes)#it issign threes into the list of threes

        rest = num[:length % 3]#it calculates rest of the number for further calculation
        if rest:
            splitted_threes.insert(0, rest)#it adds an element at the specified position
        return ','.join(splitted_threes)#it returns a string joined by coma
num = input('Enter your number: ')#it asks user to input his number
result = split_to_three(num)#it assings function invocation to result variable
print(result)#it prints result