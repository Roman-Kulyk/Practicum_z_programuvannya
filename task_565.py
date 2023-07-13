# 565. У першому рядку вводиться кількість рядків, потім задаються самі рядки слів, 
# розділених пропусками. Виведіть слово, яке у рядках зустрічається найчастіше. 
# Якщо таких слів декілька, надрукуйте те, що розміщується вище в алфавітному порядку.
'''
Вхідні дані:
2
apple orange banana
banana orange

Вихідні дані:
banana
'''
n = int(input("Enter q-ty of the rows: "))#it enters the q-ty of row
words_dict = {}#it initialize an empty dictionary

for _ in range(n):#for rows in range n
    words = input("Enter your text: ").split()#it enters the row itself

    for word in words:#for every word in row
        if word in words_dict:#it check if word in dictionary
            words_dict[word] += 1#if is it ad 1 to q-ty
        else:#in other case
            words_dict[word] = 1#it assign 1 to q-ty

max_frequency = max(words_dict.values())#it founds max value in dict values list

most_frequent_words = sorted(word for word, frequency in words_dict.items() 
if frequency == max_frequency)#it sorts in alphabetical order items with the max frequency

print(most_frequent_words[0])#it prints word with max frequency