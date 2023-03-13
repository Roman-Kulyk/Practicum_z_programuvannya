# 108. Відомі дві швидкості: одна в кілометрах за годину, інша - в метрах за секунду. Яка з швидкостей більше?

speed_1 = int(input('Enter a first speed in km per hour: '))
speed_2 = int(input('Enter a second speed in m per second: '))

if (speed_1 * 1000 // 3600) > speed_2:
    print(speed_1)
else: 
    print(speed_2)