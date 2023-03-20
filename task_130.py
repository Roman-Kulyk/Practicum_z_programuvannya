#130. Компанія-виробник програмного забезпечення у сфері інформаційної безпеки реалізує один комплект програм 
#за 2700 гривень. Якщо відбувається купівля декількох одиниць товару, працює система знижок: 
#10-19 одиниць товару - 10%, 
#20-49 - 20%, 
#50-99 - 30%, 
#100 або більше - 40%. 
#Напишіть програму, яка отримує від користувача ціле число - кількість придбаних комплектів програмного забезпечення 
#і виводить повідомлення про суму знижки (якщо така є) та загальну суму при купівлі зі знижкою

number = int(input('Enter a q-ty of licenses: '))
if 10 <= number < 19:
    discount = 0.9
elif 20 <= number < 49:
    discount = 0.8
elif 50 <= number < 99:
    discount = 0.7
elif 100 <= number:
    discount = 0.6
else:
    discount = 1
price = str(number * 2700 * discount)

#print(discount)
#print(price)
print(f'The amount of discount is {discount}, total amount of the purchase after the discount is UAH {price}')