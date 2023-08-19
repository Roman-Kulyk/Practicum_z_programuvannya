# Створіть новий файл numbers.txt у текстовому редакторі і запишіть у нього 10 чисел, кожне з 
# нового рядка. Напишіть програму, яка зчитує ці числа з файла і обчислює їх суму, виводить цю 
# суму на екран і, водночас, записує цю суму у інший файл з назвою sum_numbers.txt.

numbers = []

freading1 = open('ex_#883_1_numbers.txt','rt')
lines = freading1.readlines()
freading1.close()

for line in lines:
    numbers.append(int(line.rstrip()))
print(numbers)
summ_of_num = (sum(numbers))
print(summ_of_num)


freading2 = open('sum_numbers.txt','wt')
freading2.write(str(summ_of_num))
freading2.close()
