# 394. Дано текст і відомо, що він шифрується наступним чином. Спочатку визначається 
# кількість букв k в найдовшому слові (словом називається безперервна послідовність 
# англійських букв, слова один від одного відокремлюються будь-якими іншими символами, 
# довжина слова не перевищує 20 символів). Потім кожна англійська літера замінюється на 
# букву, що стоїть в алфавіті на k букв раніше (алфавіт вважається циклічним, тобто перед 
# буквою A стоїть буква Z). Інші символи залишаються незмінними. Малі літери при цьому 
# залишаються малими, а великі - великими. Розшифруйте введений текст.
"""
Вхідні дані:
Njzxwxgd Bpihjbdid, rgtpidg du iwt Gjqn egdvgpbbxcv apcvjpvt.

Вихідні дані:
Yukihiro Matsumoto, creator of the Ruby programming language.
"""
def decrypt_text(text,k):
    decrypt_text = ""

    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - ascii_offset + k) % 26 + ascii_offset)
            decrypt_text += decrypted_char
        else:
            decrypt_text += char
    return decrypt_text

encrypted_text = input('Enter your text: ')
words = encrypted_text.split()
max_word_len = max(words,key = lambda x: len([ char for char in x if char.isalpha()]))
k = len(max_word_len)

decrypted_text = decrypt_text(encrypted_text,k)
print(decrypted_text)
