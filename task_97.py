#97. Відомо, що батько старший за сина на n років, а син молодший батька в m разів. Визначте, скільки років 
#батькові і скільки років синові. Вхідні дані такі, що вік батька і вік сина є цілими числами. Програма має вивести 
#два числа, розділені пропуском: вік батька і вік сина.
n = int(input('Enter a number:'))
m = int(input('Enter a number: '))

dad_age = son_age + n      #n = 20, dad_age = 25
son_age = dad_age // m     #m = 5 , son_age = 5



