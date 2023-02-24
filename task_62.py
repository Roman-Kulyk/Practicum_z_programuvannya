#62.Напишіть програму для перетворення введених секунд у кількість днів, годин,
#хвилин та секунд.

seconds = int(input('Enter a 1-ty of seconds: '))
days = seconds//60//60//24
hours = seconds//60//60%24
minutes = seconds//60%60
sec = seconds%60
print(f'{days} days(s), {hours} hours, {minutes} minutes, {sec} seconds'.format(days,hours,minutes,sec))
