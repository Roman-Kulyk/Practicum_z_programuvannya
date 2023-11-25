# 596.Двоє друзів вирішили здійснити влітку сходження в гори Карпати. Кожен з них зібрав свій 
# рюкзак речей. Перевірте, які речі присутні в обох рюкзаках друзів, які є лише в першому рюкзаку, 
# але не має в другому і, навпаки, є в другому і відсутні в першому. Дано два словники, у яких 
# ключами є назви речей, а значеннями - кількості речей. Надрукуйте назви речей і їх кількості, 
# які пристутні в обох рюкзаках друзів, лише в першому рюкзаку і лише в другому рюкзаку.
"""
Вхідні дані:
Немає

Вихідні дані:
In both:
first aid kit 1
lighter 2
sunglasses 1
trousers 2
hygienic set 1
flashlight 1
footwear 2
socks 3
sleeping bag 1

Only in the first:
water jacket 1
cap 1
dishes 2
woolen gloves 1
tent 1

Only in the other:
batteries 4
poncho 1
t-shirts 3

"""
backpack_1 = {'first aid kit': 1,
              'lighter': 2,
              'sunglasses': 1,
              'trousers': 2,
              'hygienic set': 1,
              'flashlight': 1,
              'footwear': 2,
              'socks': 3,
              'sleeping bag': 1,
              'water jacket': 1,
              'cap': 1,
              'dishes': 2,
              'woolen gloves': 1,
              'tent': 1
              }
backpack_2 = {'first aid kit': 1,
              'lighter': 2,
              'sunglasses': 1,
              'trousers': 2,
              'hygienic set': 1,
              'flashlight': 1,
              'footwear': 2,
              'socks': 3,
              'sleeping bag': 1,
              'batteries': 4,
              'poncho': 1,
              't-shirts': 3
              }

print('In both:')
for key, value in backpack_1.items() and backpack_2.items():
    if key in backpack_1 and backpack_2:
        print(key, value)

print('Only in the first:')
for key, value in backpack_2.items() and backpack_1.items():
    if key in backpack_1:
        if key not in backpack_2:
            print(key, value)

print('Only in the other:')
for key, value in backpack_1.items() and backpack_2.items():
    if key in backpack_2:
        if key not in backpack_1:
            print(key, value)

