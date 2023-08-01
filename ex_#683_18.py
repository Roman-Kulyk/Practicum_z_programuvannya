# Напишіть програму, у якій комп’ютер генерує випадкове число, а користувач повинен 
# вгадати число, вводячи його з клавіатури за вказану кількість спроб.
def quess_a_number(n):

    import random
    number = random.randint(0, 100)
    print(number)
    
    while n != 0:        
        n = n - 1
        your_number = int(input("Enter your number between 0 and 100: "))
        if your_number == number:
            print("You did it!")
            break
            
        else:
            if your_number > number:
                print("Your number is greater!")
            
            elif your_number < number:
                print("Your number is smaller!")

    print('The number was: ',number)
            
    
    

quess_a_number(6)