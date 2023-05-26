# 372. Дано рядок нулів та одиниць. Напишіть програму для знаходження найдовшої 
# неперервної послідовності нулів у рядку.
'''
Вхідні дані:
1001
100001001010
1000001

Вихідні дані:
2
4
5
'''
s = input("Enter a string: ")
max_len = 0 #it initialize maximum length zero sequence
cur_len = 0 # current length zero sequence
for i in s:#it checks every item in string and in case
    if i == '0': #item equal to 0
        cur_len +=1 #it add it to current sequence
        if cur_len > max_len: #it check if current sequense is longer than maximum one
            max_len = cur_len # if so it assign current to maximum
    else: #if item equal to 1
        cur_len = 0 #it assign 0 to current sequence
print(max_len)#it prints maximum length