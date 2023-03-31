#158. Дано двоцифрове число. Визначити, чи є сума його цифр двоцифровим числом.

num = int(input("Enter a number: "))
f = num // 10
s = num % 10
#print(f,s)

if f + s >= 10:
    print(True)
else:
    print(False)