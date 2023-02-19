#45.Обчисліть, скільки коштуватиме певний товар в магазині, якщо діє знижка на
#нього. Значення ціни товару і відсоток знижки вводяться вокремих рядках
#користувачем з клавіатури.

price = int(input('Enter a price of unit: '))
discount = float(input('Enter a discount: '))
for_sale = price - price*(1 * discount)
print(for_sale)
