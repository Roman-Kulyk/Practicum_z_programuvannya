#175. Дано чотирицифрове число. Визначити, чи дорівнює сума двох перших його цифр сумі двох його останніх цифр.

num = int(input("Enter a number: "))

f = num // 1000
s = num % 1000 // 100
t = num % 1000 % 100 // 10
fo = num % 1000 % 100 %10
print(f,s,t,fo)

if f + s == t + fo:
    print(True)
else:
    print(False)