# 370. Користувач вводить рядок і певний символ, який устрічається у рядку 
# щонайменше двічі. Напишіть програму, яка видалить із введеного рядка перше і 
# останнє входження символа, а також всі символи між ними.
'''
Вхідні дані:
We left in pretty good time, and came after nightfall to Klausenburgh. Here I stopped for the night at the Hotel Royale.
u

Вихідні дані:
We left in pretty good time, and came after nightfall to Klargh. Here I stopped for the night at the Hotel Royale.
'''
txt = input("Enter a string: ")
char = input("Enter a character to find: ")

x_1 = txt.find(char)

x_2 = txt.rfind(char)
print(txt[:x_1]+txt[x_2+1:])