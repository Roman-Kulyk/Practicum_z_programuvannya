#Напишіть програму для перетворення висоти (вказується окремо у футах
#(1 фут = 30,48 см) і дюймах (1 дюйм = 2,54 см) у сантиметри.

Feet=int(input('Enter your height foot: '))
Inches=int(input('Enter your height inches: '))
height=int(Feet * 30.48 + Inches * 2.54)
print(f'Your height is:{height}')
