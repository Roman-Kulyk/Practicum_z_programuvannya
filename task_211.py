#211. Напишіть програму для побудови шаблону як у вихідних даних за введеним значенням n.

n = int(input("Enter a number: "))

for i in range(1,n + 1):
    #n = 0
    n = (i-1) + 1
    print(str(i)*n)
