# 587. Користувачем вводяться наступні дані: у першому рядку міститься кількість рядків n, 
# а потім - вводяться n рядків слів. Надрукуйте слово, яке в тексті зустрічається найчастіше. 
# Якщо таких слів є декілька, надрукуйте слово, яке в алфавітному порядку розташоване раніше.
"""
Вхідні дані:
3
editor detective baker scientist
singer teacher
teacher scientist

Вихідні дані:
scientist
"""
number = int(input("Enter your number: "))
text = ''
for i in range(number):
    string = input("Enter your row of text: ")
    text += (string + ' ')

word_list  = (sorted(text.split()))
print(word_list)
# print(len(word_list))

word_list_dict = {}
for i in word_list:
    word_list_dict[i] = word_list.count(i)

# print(word_list_dict)

# taking list of car values in v
v = list(word_list_dict.values())
 
# taking list of car keys in v
k = list(word_list_dict.keys())
 
print(k[v.index(max(v))])
