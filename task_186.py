#186. Скласти програму знаходження добутку двох найменших з трьох різних цілих чисел.

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

if a < b < c:
    print(a * b)
elif a < c < b:
    print(a * c)
elif b < a < c:
    print(b * a)
elif b < c < a:
    print(b * c)
elif c < a < b:
    print(c * a)
elif c < b < a:
    print(c * b)
