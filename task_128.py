#128.Червоний, зелений та синій кольори відомі як основні кольори колірної моделі RGB. 
#При змішуванні червоного та зеленого кольорів, отримується жовтий, при змішуванні синього і зеленого - блакитний, 
#а при змішуванні синього і червоного – пурпуровий колір. 
#Напишіть програму, яка запропонує користувачеві ввести назви двох основних кольорів для змішування. 
#Якщо користувач вводить щось інше, ніж «червоний», «синій» або «зелений», 
#програма повинна виводити повідомлення про відсутність такої палітри. 
#В іншому випадку програма повинна відображати назву кольору, що утворився.

colour_1 = input('Enter first colour: ')
colour_2 = input('Enter second colour: ')

if colour_1 == 'red' and colour_2 == 'green' or colour_2 == 'red' and colour_1 == 'green':
    print('Yellow')
elif colour_1 == 'blue' and colour_2 == 'green' or colour_2 == 'blue' and colour_1 == 'green':
    print('Light blue')
elif colour_1 == 'blue' and colour_2 == 'red' or colour_2 == 'blue' and colour_1 == 'red':
    print('Purple')
else:
    print('There is not such colour!')