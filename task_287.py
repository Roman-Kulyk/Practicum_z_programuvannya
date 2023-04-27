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
        sequence.append(curr)
        prev = sequence[0]
         
        if prev > 0:
            prev_sign = 1
        else:
            prev_sign = -1
        sign_changes = 0

    for  cur in sequence[1:]:
        if cur > 0:
            cur_sign = 1
        else:
            cur_sign = -1

        if cur_sign != prev_sign:
            sign_changes+=1
        prev = cur
        prev_sign=cur_sign

print(sign_changes)