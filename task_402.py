# 402. Дано рядок, який може міститити пропуски. Визначте, яка буква англійського 
# алфавіту (або які букви) в цьому рядку зустрічається найчастіше. Великі і малі літери 
# вважаються однаковими, а інші символи, які не є буквами, не враховуються. Програма повинна 
# вивести в першому рядку всі букви, які зустрічаються найчастіше в заданому рядку. Виводити 
# букви необхідно у верхньому регістрі, в алфавітному порядку (додатково), без пропусків. 
# У другому рядку виведіть єдине число - скільки разів у цьому рядку зустрічаються ці літери. 
# При виконанні цього завдання не можна користуватися вкладеними циклами. Вхідний рядок 
# повинен оброблятися за один прохід.
"""
Вхідні дані:
Project Gutenberg EBook of The jungle book, by Rudyard Kipling

Вихідні дані:
EO
6
"""
def find_most_frequent_letter(string):
    string = string.replace(' ','')#it removed empty space
    string = string.lower()#it turns all letter in lower case
    frequency = {}#it initializes an empty dictionary

    for letter in string:#it checks every character in string
        if letter.isalpha():#if it is a letter
            if letter in frequency:#and if it is in frequency dictionary
                frequency[letter]  += 1#if so it enlarge frequency counter
            else:#in another case 
                frequency[letter] = 1#it assigns to the frequency counter 1
    max_frequency = max(frequency.values())#it assign maximum frequency value
    #to the max_frequency variable
    most_frequent_letter = [letter for letter, frequency in frequency.items() 
                            if frequency == max_frequency]
    #it adds most frequence letter to the most_frequent_letter list
    return most_frequent_letter, max_frequency

string = input("Enter your string: ")
most_frequent_letter, frequency = find_most_frequent_letter(string)
print(type(most_frequent_letter))

print('Most frequent letters: ')
print(" ".join(most_frequent_letter))
print(f'Frequency: {frequency}')
