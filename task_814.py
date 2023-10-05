# 814. Напишіть клас Bank для опису простих операції з вашим банківським 
# рахунком: покласти на рахунок, зняти з рахунку, переглянути рахунок. 
# При створенні екземпляру класу, екземпляр отримує атрибут __balance з 
# певним значенням. Клас повинен містити методи для додавання коштів на 
# рахунок і знімання з рахунку, за умови, що на рахунку достатньо коштів.

class Bank:
    def __init__(self, __balance):
        self.balance = __balance

    def deposit(self, add):
        self.balance = self.balance + add
        print(f"You have {self.balance} $ on your account.")

        

    def withdrowal(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print(f"You have {self.balance} $ on your account.")
        else:
            print("You do not have enough $ on your account.")
            print("Contact your manager.")

    def check_ackount(self):
        print(f"You have {self.balance} $ on your account.")

raif = Bank(200)
raif.deposit(200)
raif.check_ackount()
raif.withdrowal(350)
raif.withdrowal(100)