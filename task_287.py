# 287. Дано послідовність ненульових цілих чисел, яка завершується нулем 
# (саме число 0 в послідовність не входить, а використовується як ознака її закінчення). 
# Необхідно обчислити скільки разів в цій послідовності змінюється знак 
# (наприклад, в послідовності 10, -4, 12, 56, -4 знак змінюється 3 рази).

'''
Вхідні дані:

-5
-3
10
6
-4
7
-1
0

Вихідні дані:

4

'''
sequence = []
while True:
    curr = int(input("Enter a number: "))#it reads elements of sequence
    if curr == 0:#it checks if element not equal to zero
        break
    else:
        sequence.append(curr) #it appends element to the sequence list
        prev = sequence[0] #it assign first sequence's element to prev variable

        if prev > 0: #it checks if prev variable more than 0
            prev_sign = 1 #in this case it initialize prev_sign variable with 1
        else:
            prev_sign = -1 #in other case it initialize prev_sign variable with -1
        sign_changes = 0 #it initialiaze sign_changes variable with 0

    for  cur in sequence[1:]:
        if cur > 0: #it checks if cur variable more than 0
            cur_sign = 1 #in this case it initialize cur_sign variable with 1
        else:
            cur_sign = -1 #in other case it initialize cur_sign variable with -1

        if cur_sign != prev_sign: #it checks if cur_sign variable is not equal to prev_sign variable
            sign_changes+=1 #in this case it add 1 to the sign_changes counter
        prev = cur #it assign cur variable to prev variable
        prev_sign=cur_sign #it assign cur_sign variable to prev_sign variable

print(sign_changes) #it prints sign_changes variable