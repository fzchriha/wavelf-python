water = 400
milk = 540
coffee_beans = 120
cups = 9
money = 550
        
class CoffeeMachine:

    def __init__(self, water, milk, coffee_beans, cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money
        
    def __str__(self):
        return f"The coffee machine has:\n{self.water} of water\n{self.milk} of milk\n{self.coffee_beans} of coffee beans\n{self.cups} of disposable cups\n${self.money} of money"

    def take(self):
        print("I gave you $", self.money)
        self.money = 0
        
    def fill(self):
        print("How many ml of water do you want to add:")
        amount_water = int(input())
        self.water = amount_water + self.water
        print("How many ml of milk do you want to add:")
        amount_milk = int(input())
        self.milk = amount_milk + self.milk
        print("How many grams of coffee beans do you want to add:")
        amount_coffee_beans = int(input())
        self.coffee_beans = amount_coffee_beans + self.coffee_beans
        print("How many disposable cups do you want to add:")
        amount_cups = int(input())
        self.cups = amount_cups + self.cups
        
    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        options_for_buy = input()
        if options_for_buy == "1":
            if self.water > 250 and self.coffee_beans > 16 and self.cups > 1:
                print("I have enough resources, making you a coffee!")
                self.water = self.water - 250
                self.coffee_beans = self.coffee_beans - 16
                self.cups = self.cups - 1
                self.money = self.money + 4
            else:
                if self.water < 250:
                    print("Sorry not enough water.")
                elif self.coffee_beans < 16:
                    print("Sorry not enough coffee beans.")
                elif self.cups < 1:
                    print("Sorry not enough cups.")
        elif options_for_buy == "2":
            if self.water > 350 and self.milk > 75 and self.coffee_beans > 20 and self.cups > 1:
                print("I have enough resources, making you a coffee!")
                self.water = self.water - 350
                self.milk = self.milk - 75
                self.coffee_beans = self.coffee_beans - 20
                self.cups = self.cups - 1
                self.money = self.money + 7
            else:
                if self.water < 350:
                    print("Sorry not enough water.")
                elif self.milk < 75:
                    print("Sorry not enough milk.")
                elif self.coffee_beans < 12:
                    print("Sorry not enough coffee beans.")
                elif self.cups < 1:
                    print("Sorry not enough cups.")
        elif options_for_buy == "3":
            if self.water > 200 and self.milk > 100 and self.coffee_beans > 12 and self.cups > 1:
                print("I have enough resources, making you a coffee!")
                self.water = self.water - 200
                self.milk = self.milk - 100
                self.coffee_beans = self.coffee_beans - 12
                self.cups = self.cups - 1
                self.money = self.money + 6

    def remaining(self):
        print(self)
        
coffee_machine = CoffeeMachine(water, milk, coffee_beans, cups, money)
option = input("Write action (buy, fill, take, remaining, exit):\n")

while option != 'exit':
    print("")
    if option == "take":
        coffee_machine.take()
        print("")

    elif option == "fill":
        coffee_machine.fill()
        
    elif option == "buy":
        coffee_machine.buy()
        
    elif option == "remaining":
        coffee_machine.remaining()
    
    option = input("\nWrite action (buy, fill, take, remaining, exit):\n")
