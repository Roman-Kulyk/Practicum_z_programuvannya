# 241. Напишіть програму для побудови шаблону як у вихідних даних за введеним значенням n.



'''
Вхідні дані:

7

Вихідні дані:

1 	2 	3 	4 	5 	6 	7
2 	3 	4 	5 	6 	7
3 	4 	5 	6 	7
4 	5 	6 	7
5 	6 	7
6 	7
7
'''


n = int(input("Enter a number: "))
for n in range(n,0,-1):
    print('$'*n)