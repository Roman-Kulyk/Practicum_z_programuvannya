#172. Напишіть програму, яка отримує на вхід ціле число, і виводить True, якщо передане значення потрапляє в 
#інтервал (-15,12] ∪ (14,17) ∪ [19, + ∞) і False в іншому випадку. Зверніть увагу на різні дужки, 
#які використовуються для позначення інтервалів.


num = int(input("Enter a number: "))

if -15 < num <= 12 or 14 <= num <17 or 19 <= num:
    print(True)
else:
    print(False)
