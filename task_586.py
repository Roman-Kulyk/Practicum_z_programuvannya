# 586. Дано список країн і міст кожної країни. Потім подані назви міст. Для кожного міста 
# вкажіть, в якій країні воно знаходиться. Програма отримує на вхід кількість країн n. 
# Далі йде n рядків, кожен рядок починається з назви країни, потім йдуть назви міст цієї країни. 
# У наступному рядку записано число m, далі йдуть m запитів - назви якихось m міст, 
# перерахованих вище. Для кожного із запиту виведіть назву країни, в якій знаходиться дане місто.
"""
Вхідні дані:
2
Ukraine Kyiv Kharkiv Lviv
England London Liverpool Manchester Bristol
3
Kyiv
London
Lviv

Вихідні дані:
Ukraine
England
Ukraine
"""
def find_country(city, countries):
    for country, cities_in_country in countries.items():
        if city in cities_in_country:
            return country
    return "City was not found!"

n = int(input("Enter countries number: "))
countries = {}
for _ in range(n):
    country_and_cities = input("Enter countries and cities: ").split()
    country = country_and_cities[0]
    cities = country_and_cities[1:]
    countries[country] = cities

m = int(input("Enter q-ty of requests: "))
for _ in range(m):
    query_city = input("Enter city's name: ")
    country_of_city = find_country(query_city, countries)
    print(f'{query_city} {country_of_city}')
    print(country_of_city)