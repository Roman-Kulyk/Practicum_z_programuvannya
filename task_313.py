# 313. Дано слово. З’ясуйте, чи слово починається і закінчується на одну і ту ж букву? 
# Регістр літер не враховувати.
'''
Вхідні дані:

Africa
Oceania

Вихідні дані:

True
False

'''
message = input('Enter a word: ')
message_low = message.lower()
if message_low[0] == message_low[-1]:
    print(True)
else:
    print(False)