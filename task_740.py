# 740. Напишіть програму для друку дати й часу на поточний момент у різних форматах як у вихідних даних. 
# Використайте модулі time і datetime.
'''
Вхідні дані:

Немає

Вихідні дані:
Current date and time: 2019-07-26 21:00:41.004061
Current year: 2019
Month of year: July
Week number of the year: 29
Weekday of the week: 5
Day of year: 207
Day of the month: 26
Day of week: Friday
'''
import time
import datetime

print(time.ctime())

print(f"Current date and time: {datetime.datetime.now()}")
print(f"Current year:{time.strftime('%Y')}")
print(f"Month of year:{time.strftime('%B')}")
print(f"Week number of the year:{time.strftime('%U')}")
print(f"Weekday of the week:{time.strftime('%w')}")
print(f"Day of year:{time.strftime('%j')}")
print(f"Day of the month:{time.strftime('%d')}")
print(f"Day of week:{time.strftime('%A')}")