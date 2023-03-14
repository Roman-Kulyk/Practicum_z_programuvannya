'''It would be great if this program:
-runs every month when money  come to my bank account and generate an email with this information.
-another features should be added further.'''

num = float(input('Enter a currency rate: '))
values = 300

lessons_price = 313 * 30
print('You have to pay ' + str(lessons_price)+ ' for lessons.')

sum = num * values
tax = sum * 0.05
print('You have to left ' + str(tax)+ ' for tax.')

rest = sum - tax - lessons_price
print('You must pay additional ' + str(rest) + ' for credit in this case, immediately.')

exam_price = num * 250
print('You have to pay ' + str(exam_price)+ ' for the exam.')

rest_1 = sum - tax - exam_price
print('You must pay additional ' + str(rest_1) + ' for credit in this case, immediately.')
