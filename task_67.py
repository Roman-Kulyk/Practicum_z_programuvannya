#67.Книга коштує a гривень і b копійок. Визначте, скільки гривень і копійок
#потрібно заплатити за n книг. Значення вводяться користувачем упорядку
#a,b,n на окремих рядках, а сума до сплати в одному рядку через пропуск:
#кількість гривень і копійок відповідно.

a=int(input('Enter a гривень number: '))
b=int(input('Enter a копійок number: '))
n=int(input('Enter a книг number: '))

price=a*100+b
total=price*n
total_hr=total//100
total_cop=total%100
print(str(total_hr)+' '+str(total_cop))



