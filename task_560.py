# 560. Дано текст англійською мовою. Крім англійських букв, в ньому можуть 
# зустрічатися пропуски і розділові знаки. Надрукуйте відомості про те, скільки яких 
# букв зустрічається в цьому тексті (вивести 26 чисел). При підрахунку великі та 
# малі літери не розрізняються.
'''
Вхідні дані:
Hello world!

Вихідні дані:
0 0 0 1 1 0 0 1 0 0 0 3 0 0 2 0 0 1 0 0 0 0 1 0 0 0
'''
letter_count = [0] * 26
text = input("Enter a sequence: ")

for char in text:#for every item in text
    char = char.lower()#it converts character into lower register
    if char.isalpha():#it checks if item is a letter
        letter_count[ord(char) - ord('a')] += 1#it counts letters
#print(' '.join(str(count) for count in letter_count))#it prints string of letter whic were counted
for count in letter_count:
    print(count, end = ' ')
print()