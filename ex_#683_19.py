# Створіть програму за мотивами відомої гри «Камінь, Ножиці, Папір». Застосуйте 
# функціональний підхід при написанні коду програми.
import random




def game_item(text_1 = input("Enter your item: ")):

    text_2 = random.choice(['Камінь', 'Ножиці', 'Папір'])
    if text_1 == 'Ножиці' and text_2 == 'Папір':
        print('"ножиці" б\'ють (розрізають) "папір"')
    elif text_1 == 'Папір' and text_2 == 'Камінь':
        print('"папір" б\'є (накриває) "камінь"')
    elif text_1 == 'Камінь' and text_2 == 'Ножиці':
        print('"камінь" б\'є (ламає) "ножиці"')
    elif text_1 == text_2:
        print("It's a draw play again!")
    else:
        print(f"You're lost, looser!!!I've got a {text_2}")
              
#"ножиці" б'ють (розрізають) "папір";
#"папір" б'є (накриває) "камінь";
#"камінь" б'є (ламає) "ножиці".
 
game_item()