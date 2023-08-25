# 734. У вхідному файлі записано два цілих числа, які можуть бути розділені пропусками і кінцями рядків. 
# Виведіть у вихідний файл їх суму.
'''
Вхідні дані:
Файл input.txt з вмістом
  2

 2

Вихідні дані:
Файл output.txt з вмістом
4
'''
freading = open('task_734_input.txt', 'rt' )
lines = freading.readlines()
freading.close()

summ = int(lines[0]) * int(lines[1])
print(summ)

freading_2 = open('task_734_output.txt','wt')
lines = freading_2.write(str(summ))
freading_2.close()