#75.За правилами числа округлюються до найближчого цілого числа, а якщо
#дробова частина числа дорівнює 0.5, то число округляється вгору.Дано
#невід’ємне число a, яке необхідно округлити за цими правилами. Зверніть увагу,
#що функція round()не годиться для цього завдання!Використовувати розгалуження,
#цикли, математичний модуль math не можна.
import decimal as decimal
num = float(input('Enter a number: '))
print(decimal.Decimal(num).quantize(decimal.Decimal('1'), rounding=decimal.ROUND_HALF_UP))
