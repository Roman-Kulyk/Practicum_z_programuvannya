#Напишіть програму для перетворення відстані (вказана у футах) у дюйми
#(1 фут = 12 дюймів), ярди (1 фут = 0,333333333 ярда) і милі
#(1 фут = 0,000189393939 милі).

distance=int(input('Enter distance in feet: '))

inches_distance=distance*12
yards_distance=distance*0.333333333
miles_distance=distance*0.000189393939

print(f'The distance in inches is {inches_distance} inches.')
print(f'The distance in yards is {yards_distance:.3f} yards.')
print(f'The distance in miles is {miles_distance:.3f} miles.')

             
