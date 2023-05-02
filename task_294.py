# 294. Дано два чотирицифрових числа a і b. 
# Виведіть усі чотирицифрові числа на відрізку від a до b, 
# які є паліндромами (читаються однаково як зліва направо, так і справа наліво).
'''
Вхідні дані:

1400
2200

Вихідні дані:

1441
1551
1661
1771
1881
1991
2002
2112
'''
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
#pal_list = []#it initialize empty list
for i in range(a,b):
    b_i = str(i)#it changes variale type to str
    rb_i = b_i[::-1]#it returns a string in backward order
    if str(i) == rb_i:#it checks values of variables
        #pal_list.append(i)#it adds member to the list
    #else:
        #continue
        print(i)