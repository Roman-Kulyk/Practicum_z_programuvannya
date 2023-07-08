# 549. В рядку записаний текст. Словом вважається послідовність непробільних 
# символів, які йдуть підряд, слова розділені одним або більшим числом пропуском або 
# символами кінця рядка. Для кожного слова з цього тексту підрахуйте, скільки разів 
# воно зустрічалося в цьому тексті раніше.
'''
Вхідні дані:
var list set tuple list tuple tuple dict var

Вихідні дані:
0 0 0 0 1 1 2 0 1
'''
input_string = input('Enter your text: ')
words = input_string.split()

word_freq = {}

for word in words:
        if word in word_freq:
               word_freq[word] += 1
        else:
              word_freq[word] = 0


#print(word_freq)
freq_list = []
for freq in word_freq.values():
    freq_list.append(freq)
print(freq_list)
    