# 748. Напишіть програму для друку випадкової вибірки слів із текстового файла. 
# Кількість слів має бути також випадковою в межах кількості рядків у файлі. 
# Слова зберігаються у файлі на окремих рядках.
'''
Вхідні дані:
Файл input.txt з вмістом
Python
Ruby
C++
C
Java

Вихідні дані:
Java
Python
C++
'''
import random
freading = open('task_748_input.txt', 'r' )#it opens a file
c = len(freading.readlines())#it assign a q-ty of rows in file to c variable
freading.close()#it closes the file

for i in range(random.randint(1,c)):# for some q-ty of times in range from 0 to w-ty of rows in file
    freading = open('task_748_input.txt', 'r' )#it opens a file in read mode
    lines = random.choice(freading.readlines())#it return a random element from the non-empty sequence
    print(lines,sep=' ',end=' ')#print line which was returned
freading.close()#it closes the file
print()