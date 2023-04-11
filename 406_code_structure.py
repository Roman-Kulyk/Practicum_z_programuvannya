#406. Виконайте візуалізацію структури коду програми. 
# Використайте у візуалізації структури елементи кортежу keywords = ('for', 'if', 'else', 'in', ':'). 
# У процесі виведення структури коду на екран, враховуйте відступи рядків від лівого краю, 
# у розрахунку один відступ - 4 пропуски. Вигляд структури коду має бути таким:

#for each token in the postfix expression :
#    if the token is a number :
#        print('Convert it to an integer and add it to the end of values')
#    else
#        print('Append the result to the end of values')


numbers = input("Enter five numbers through the spacebar: ").split(" ")

for number in numbers:
    if int(number) % 2 == 0:
        print(number)
    else:
        print("It's not an event number!")