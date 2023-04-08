#202. Дано натуральне число n (0 ≤ n ≤ 1000), яке визначає період піврозпаду радіоактивних атомів, визначений у 
#роках. Необхідно вивести значення періоду піврозпаду, додавши до цього числа відповідно «рік» (rik), «роки» (roku),
#«років» (rokiv).

n = int(input("Enter a number: "))
if 5 <= n <=20 :                               # 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
    print(f"{n} років")

elif (n % 10) == (1 % 10):                      # 21 31 41 51 61 71 81 91 
    print(f"{n} рік")

elif 2 <= n % 10 <= 4:                          # 22 23 24 32 33 34 42 43 44 
    print(f"{n} роки")

elif 5 <= (n % 10) <= 9:                        # 25 26 27 28 29  35 36 37 38 38  45 46 47 48 49 
    print(f"{n} років")
    
elif n % 10 == 0:                               # 30 40 50 60 70 80 90 
    print(f"{n} років")