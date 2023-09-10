# 743. Напишіть програму для перевірки правильності пароля, введеного користувачем. 
# Пароль має задовільняти таким вимогам:

# Не менше 1 букви з проміжку [a-z] та 1 букви з порміжку [A-Z].
# Принаймні 1 число з проміжку [0-9].
# Не менше 1 символу з [$#@].
# Мінімальна довжина 8 символів.
# Максимальна довжина 12 символів.
# Використайте модуль re.
'''
Вхідні дані:
12$FGasEr9
qwerty
45Da#0

Вихідні дані:
Valid
Invalid
Invalid
'''
import re
def validate_password(password):
    #define our regex for validation
    pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"
    #we use the re.match function to test the password against the pattern
    match = re.match(pattern, password)
    #return True if the password matches the pattern, False otherwise
    return bool(match)

password1 = "12$FGasEr9"
print(validate_password(password1))
password2 = "qwerty"
print(validate_password(password2))
password3 = "45Da#0"
print(validate_password(password3))