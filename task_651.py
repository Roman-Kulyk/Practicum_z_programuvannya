# 651. Напишіть функцію - простий лічильник відвідувань, яка отримує в циклі 
# (до тих пір, поки не буде введено 0) логін. Якщо логін новий, то лічильник 
# збільшується на одиницю, якщо логін вже був, то лічильник відвідувань також 
# збільшується на одиницю, а число унікальних відвідувачів залишається незмінним. 
# На екран має виводитися кількість відвідувань і кількість унікальних користувачів.
'''
Вхідні дані:
Barbara
Alex56
Alex56
Barbara
0

Вихідні дані:
1 1
2 2
3 2
4 2
5 2
0
'''
def vocab_func():
    vocab_dict = {}
    name =''
    separate_user = 0
    attendance = 0
    while name != '0':
        name = input("Enter you name: ")

        if name not in vocab_dict and name !='0':
            vocab_dict[name] = 1
            separate_user += 1
            attendance +=1
            print(attendance, separate_user)

        elif name in vocab_dict:
            vocab_dict[name] += 1
            attendance += 1
            print(attendance, separate_user)

        elif name == '0':
            attendance += 1
            print(attendance, separate_user)
            break

vocab_func()