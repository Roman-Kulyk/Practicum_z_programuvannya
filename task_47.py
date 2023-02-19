#47.Визначити, яку платню одержить на фірмі сумісник за виконану роботу, якщо
#йому нараховано s гривень, а податок становить p. Значення платні і податку
#(у %) вводяться користувачем.

salary = int(input('Enter a salary value: '))
tax = int(input('Enter a tax value in %: '))

weigh = salary - salary/ 100 * tax
print(weigh)
