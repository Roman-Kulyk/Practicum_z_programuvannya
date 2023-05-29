# 380. Дано рядок, що складається з n цифр (тобто одноцифрових чисел), між якими 
# стоїть n-1 знаків операцій, кожна з яких може бути або +, або -. Обчисліть значення 
# цього виразу. Програма має надрукувати результат обчислення цього виразу.
'''
Вхідні дані:
5-3+1
6+3-2

Вихідні дані:
3
7
'''
s = input("Enter your string: ")
numbers = []
operations = []
current_number = ""
for char in s:
    if char.isdigit():
        current_number+=char
    else:
        numbers.append(int(current_number))
        current_number=""
        operations.append(char)
numbers.append(int(current_number))

result =  numbers[0]
for i in range(1,len(numbers)):
    if operations[i-1]=="+":
        result+=numbers[i]
    else:
        result-=numbers[i]
print(result)


