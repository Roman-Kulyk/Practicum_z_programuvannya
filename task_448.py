# 448. Для введеної послідовності цілих чисел обміняйте сусідні елементи у парах 
# (A[0] з A[1], A[2] з A[3] і т. д.). Надрукуйте отриманий список. Якщо в списку є 
# непарне число елементів, залиште останній елемент на місці.
'''
Вхідні дані:
1 4 5 3 7
4 2 10 5
2

Вихідні дані:
4 1 3 5 7
2 4 5 10
2
'''
input_list = input("Enter the list members: ").split()
if len(input_list)%2 == 0:
    for i in range(0, len(input_list),2):
        input_list[i],input_list[i+1]=input_list[+1],input_list[i]
print(input_list)
