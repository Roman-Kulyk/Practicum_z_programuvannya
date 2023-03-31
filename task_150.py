#150. Розробіть програму-резюме, яка за введеними початковими даними і порядковим номером виводить таку інформацію: 
#1 - прізвище, 2 - ім’я, 3 - вік, 4 - хобі, 5 - номер телефону.

surname = "Brendan"
name = "Eich"
age = 57
hobby = "programmer"
phone = 4567231

num = int(input("Enter a number: "))
if num == 1:
    print(surname)
elif num == 2:
    print(name)
elif num == 3:
    print(age)
elif num == 4:
    print(hobby)
elif num == 5:
    print(phone)
else:
    pass