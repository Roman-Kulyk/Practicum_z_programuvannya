# 240. Напишіть програму для побудови шаблону як у вихідних даних за введеними значеннями n і m.


n = int(input("Enter a number: "))
m = int(input("Enter a number: "))

for n in range(0,n):
    n += 1
    print(f'{n} {n} {n}'.format(n))
    