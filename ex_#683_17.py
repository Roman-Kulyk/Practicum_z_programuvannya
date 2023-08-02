# У програмі визначте функцію, яка генерує випадковий пароль. Пароль має бути 
# довільної довжини від 7 до 10 символів. Кожен символ паролю повинен бути випадково 
# обраним з позицій 33 до 126 з таблиці кодів ASCII . Функція повертає випадково 
# сформований пароль як єдиний її результат і він виводиться в основній програмі. 
# Скористайтеся вказівками з попередньої задачі.

def pass_gen():


    import random
    for symbol in range(random.randint(7,10)):#it generates different amount of numbers in password
        symbol = random.randrange(33,126)#it generates different value for every number
        print(chr(symbol), end ='')#it turns numbers into symbols and prints them
    print()

pass_gen()