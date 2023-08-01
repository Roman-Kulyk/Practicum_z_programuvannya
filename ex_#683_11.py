# Створіть програму, яка зчитує позицію шахової фігури від користувача і повідомляє 
# про колір квадрату, де знаходиться фігура. Наприклад, якщо користувач вводить a і 1, 
# то програма повинна повідомити, що квадрат має колір black, якщо d і 5 - програма 
# повідомляє, що квадрат має колір white.

def find_square_color(position):
    letter = position[0]#it assign first char to letter
    number = int(position[1])#it assign second char to number
    if letter in['a','c','e','g']:
        if number % 2 != 0:
            color = 'black'
        else:
            color = 'white'
            

    elif letter in['b','d','f','h']:
        if number % 2 != 0:
            color = 'white'
        else:
            color = 'black'


    return color
    
position = input("Enter position: ")
color = find_square_color(position)
print(color)
    
    
        


