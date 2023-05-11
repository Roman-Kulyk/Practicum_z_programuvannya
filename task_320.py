# 320. Користувач вводить рядок, в якому можуть бути пристуні пропуски. 
# Визначити, чи є рядок паліндромом, тобто таким, який однаково читається як 
# справа наліво, так і зліва направо. Для літер регістр не враховувати. 
# Приклади рядків-паліндромів: racecar, 10201, Ada, Never odd or even.
'''
Вхідні дані:

Ada
Able was I ere I saw Elba
10501
Origin

Вихідні дані:

True
True
True
False

'''
message = input("Enter a word or message: ")
message = message.lower()
if message[0:]==message[::-1]:
    print(True)
else:
    print(False)