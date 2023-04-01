#162. Виведіть імена видатних особистостей України, зображених на грошових знаках. Користувач вводить номінал 
#банкноти, а програма виводить значення номіналу і ім’я особи, яка зображена на цій банкноті. Якщо користувач 
#вводить неіснуюче значення номіналу, виводиться відповідне повідомлення.
num = int(input("Enter a number: "))
if num == 10:
    bill = "Mazepa"
    print(f'{num}, {bill}')
elif num == 20:
    bill = "Franko"
    print(f'{num}, {bill}')
elif num == 50:
    bill = "Hrushevskyy"
    print(f'{num}, {bill}')
elif num == 100:
    bill = "Shevchenko"
    print(f'{num}, {bill}')
elif num == 200:
    bill = "Ukrainka"
    print(f'{num}, {bill}')
elif num == 500:
    bill = "Skovoroda"
    print(f'{num}, {bill}')
elif num == 1000:
    bill = "Vernadskyy"
    print(f'{num}, {bill}')
else:
    print("No bill.")


