#116. Напишіть програму, яка друкує Yes, якщо вводяться рядки yes або YES або Yes, у інших випадках друкує No.

phrase = input('Enter your phrase: ')
if phrase == 'YES':
    print('Yes')
elif phrase == 'Yes':
    print('Yes')
elif phrase == 'yes':
    print('Yes')
else:
    print('No')
