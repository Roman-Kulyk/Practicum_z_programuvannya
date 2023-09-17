# Запишіть програмно поточні дату й час як рядок у текстовий файл today.txt. 
# Зчитайте текстовий файл today.txt і розмістіть дані у рядку today_string. 
# Розберіть дату з рядка today_string на складові, використовуючи функції для роботи з датом й часом, 
# і виведіть їх на екран у вигляді повідомлень з пояснюючим текстом.

from datetime import datetime

now = datetime.now()
#print(now)

freading = open('ex_#943_1_today.txt', 'w' )#it opens a file in writing mode.
freading.write(str(now))#it writes current date and time to the file
freading.close()#it closes the file

freading_1 = open('ex_#943_1_today.txt','r')#it opens a file in reading mode.
today_string = freading_1.read()#it reading data from file and assign it to string
freading_1.close()#it closes the file

parsed_datetime = datetime.strptime(today_string, "%Y-%m-%d %H:%M:%S.%f")#it parses date by its constituent parts format

print(f"Year: {parsed_datetime.year}")
print(f"Month: {parsed_datetime.month}")
print(f"Day: {parsed_datetime.day}")
print(f"Hour: {parsed_datetime.hour}") 
print(f"Minute: {parsed_datetime.minute}")
print(f"Second: {parsed_datetime.second}")
print(f"Microsecond: {parsed_datetime.microsecond}")