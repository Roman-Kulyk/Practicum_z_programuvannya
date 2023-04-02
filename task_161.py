#161. Відомі рік і номер місяця народження людини, а також рік і номер місяця сьогоднішнього дня 
#(січень - 1 і т. д.). Визначити вік людини (число повних років). У разі збігу вказаних номерів місяців вважати, 
#що пройшов повний рік.

year_of_birth = int(input("Enter a birth year: "))
month_of_birth = int(input("Enter a birth month: "))
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))

if month_of_birth < month:
    age = year - year_of_birth

elif month_of_birth > month:
    age = (year - year_of_birth) - 1
else:
    age = year - year_of_birth

print(age)

