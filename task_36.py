#36.Напишіть програму, яка виводить результат ділення цілих змінних a / b
#і b / a з роздільником ∗∗∗ у форматі 9 знакових позицій і 5 знаків після
#десяткової крапки відповідно.

a = 10
b = 3
n=a/b
f=b/a
print('{0:*^9.5f} {1:*^9.5f}'.format(n, f), sep='***')
