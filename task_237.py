# 237. Припускаючи, що рівень океану зараз зростає приблизно на n міліметрів на рік. 
# Напишіть програму, яка відображатиме значення щорічного росту рівня океану протягом наступних m років.


n = float(input("Enter a number of milimiters: "))
m = int(input("Enter a number of years: "))
for m in range (1, m+1):
    sum = (int(m) * n)
    print(f'{sum:.2f}'.format(sum))