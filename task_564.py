# 564.  Вводяться n рядків зі скороченими назвами країн і повними назвами міст 
# кожної країни, після цього вводяться m рядків з назвами міст. Напишіть програму, 
# яка для кожного міста друкує скорочену назву країну, в якій місто знаходиться.
'''
Вхідні дані:
5
UA Kyiv Zhytomyr Ternopil Dnipro
JP Tokyo Osaka Kyoto
CA Montreal Toronto Ottawa
USA Boston Pittsburgh Washington Seattle
UK London Edinburgh Cardiff Belfast
3
Seattle
London
Kyiv

Вихідні дані:
USA
UK
UA
countries = {'UA':['Kyiv','Zhytomyr','Ternopil','Dnipro'],
             'JP':['Tokyo','Osaka','Kyoto'],
             'CA':['Montreal','Toronto','Ottawa'],
             'USA':['Boston','Pittsburgh','Washington','Seattle'],
             'UK': ['London','Edinburgh','Cardiff','Belfast'}
'''
n = int(input("Enter the q-ty or rows: "))

countries = {}

for i in range(n):
    line = input().split()

    country = line[0]
    cities = line[1:]

for city in cities:
    countries[city] = country

m = int(input("Enter the q-ty of towns to search for: "))

for  i in range(m):
    city = input()
    print(countries[city])

