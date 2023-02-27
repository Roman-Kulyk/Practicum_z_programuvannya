#81.Дано ціле число n. Виведіть наступне за ним парне число.

n = int(input('Enter a number: '))
if n%2 == 0:
    print(n + 2)
else:
    print(n + 1)
