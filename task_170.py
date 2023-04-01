#170. Дано трицифрове ціле число. Визначити кількість однакових цифр у записі числа і вивести значення цієї кількості.
num = int(input("Enter a number:"))


f = num // 100
s = num % 100 // 10
t = num % 100 % 10

if f == s == t:
    print("3")
elif f == s != t or f == t != s or s == t != f:
    print("2")
elif f != s != t:
    print("0")