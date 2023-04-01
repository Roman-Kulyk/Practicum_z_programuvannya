#164. Напишіть програму для розрахунку індексу маси тіла, який обчислюється за формулою: 
#індекс = маса / ( зріст * зріст). Користувач вводить значення зросту (у метрах) і маси (у кілограмах), 
#а програма обчислює індекс маси тіла і виводить відповідне повідомлення: underweight (мала маса, індекс менше 18.5),
# normal weight (нормальна маса, індекс 18.5-24.9), overweight (надмірна маса, індекс більше 24.9).

h = float(input("Enter your height: "))
w = float(input("Enter your weight: "))

index = w /( h * h)

if index < 18.5:
    print("underweight")
elif 18.5 < index < 24.9:
    print("normal weight")
elif 24.9 < index:
    print("overweight")

    