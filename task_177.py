#177. Дано натуральне число n (n ≤ 9999). З’ясувати, чи різні усі чотири цифри цього числа (з урахуванням чотирьох цифр). 
#Наприклад, в числі 5623 усі цифри різні, в числі 0012 - ні.


num = int(input("Enter a number: "))

f = num // 1000
s = num % 1000 // 100
t = num % 1000 % 100 // 10
fo = num % 1000 % 100 %10
print(f,s,t,fo)

if f != s and f != t and f != fo and s != t and s != fo and t != fo:
    print(True)
else:
    print(False)