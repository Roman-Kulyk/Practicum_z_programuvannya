#179.Робота світлофора для водіїв запрограмована таким чином: 
#на початку кожної години протягом трьох хвилин горить зелений сигнал, потім протягом однієї хвилини - жовтий, 
#потім протягом двох хвилин - червоний, а далі протягом трьох хвилин - знову зелений і т. д. 
#Дано ціле число t, що позначає час у хвилинах, що минув з початку чергової години. Визначити, 
#сигнал якого кольору горить для водіїв в цей момент.

t = int(input("Enter a number: "))
'''
0-3, 3-4, 4-6,
6-9, 9-10, 10-12,
12-15, 15-16, 16-18,
18-21, 21-22, 22-24,
24-27, 27-28, 28-30,
30-33, 33-34, 34-36,
37-39, 39-40, 40-42,
42-44, 44-45, 45-47,
48-50, 50-51, 51-53,
53-55, 55-56, 56-58,
58-60.

'''
if t % 6 == 1 or t % 6 == 2 or t % 6 == 3:
    print("Green")
elif t % 6 == 4:
    print("Yellow")
else:
    print("Red")