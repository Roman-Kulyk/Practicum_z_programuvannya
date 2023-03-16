#119. В університеті використовується наступна шкала для інтерпретації результатів тестування студентів: 
#90 балів і вище (A), 80-89 (B), 70-79 (C), 60-69 (D), нижче 60 (F). 
#Напишіть програму, яка дозволить студенту ввести тестовий бал, а потім відобразити оцінку для цього балу.

grade = int(input('Enter you value: '))
if grade >= 90:
    print('Your grade is A')
elif 89 >= grade >= 80:
    print('Your grade is B')
elif 79 >= grade >= 70:
    print('Your grade is C')
elif 69 >= grade >= 60:
    print('Your grade is D')
else:
    print('Your grade is F')
