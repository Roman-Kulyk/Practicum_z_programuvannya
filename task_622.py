# 622.Напишіть функцію, яка повертає назву пори року для введеного значення 
# номера місяця.
'''
Вхідні дані:
6
2
9
3
15

Вихідні дані:
summer
winter
autumn
spring
unknown
'''
def what_season(num):
    summer = [6,7,8]
    winter = [12,1,2]
    autumn = [9,10,11]
    spring = [3,4,5]

    if num in summer:
        print('summer')
    elif num in winter:
        print('winter')
    elif num in autumn:
        print('autumn')
    elif num in spring:
        print('spring')
    else:
        print('unknown')


what_season(6)
what_season(2)
what_season(9)
what_season(3)
what_season(15)