#107. У чемпіонаті з футболу команді за виграш дається 3 очка, за програш - 0, за нічию - 1. 
#Відомо кількість очок, отриманих командою за гру. Вивести результат гри у вигляді відповідних слів: 
#«виграш», «програш» або «нічия».

score = int(input('Enter a score: '))
if score == 3:
    print('win')
elif score == 1:
    print('draw')
else:
    print('lose')