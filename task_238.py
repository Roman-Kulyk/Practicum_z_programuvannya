# 238. Надрукувати таблицю значень 1, 2, …​ n доларів США у переведенні на гривні за поточним 
# курсом k (значення курсу вводиться з клавіатури).


n = int(input("Enter a number: "))
k = float(input("Enter a course: "))

for n in range(1,n+1):
    sum = (n * k)
    print(f'{sum:.2f}'.format(sum))
