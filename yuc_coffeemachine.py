water = 400
milk = 540
beans = 120
cups = 9
money = 550

class CoffeeMachine:

    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
    
    def buy(self, coffee_type):
        if coffee_type == "1":
            con_water = 250
            con_milk = 0
            con_beans = 16
            con_cup = 1
            add_money = 4
        elif coffee_type == "2":
            con_water = 350
            con_milk = 75
            con_beans = 20
            con_cup = 1
            add_money = 7
        elif coffee_type == "3":
            con_water = 200
            con_milk = 100
            con_beans = 12
            con_cup = 1
            add_money = 6
        if con_water > self.water:
            print("Sorry, not enough water!")
        elif con_milk > self.milk:
            print("Sorry, not enough milk!")
        elif con_beans > self.beans:
            print("Sorry, not enough beans!")
        if con_water <= self.water and con_milk <= self.milk and con_beans <= self.beans and con_cup <= self.cups:
            self.water -= con_water
            self.milk -= con_milk
            self.beans -= con_beans
            self.cups -= con_cup
            self.money += add_money
            print('I have enough resources, making you a coffee!')           

    def remaining(self):
        print(f'''
The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.beans} of coffee beans
{self.cups} of disposable cups
${self.money} of money''')

    def fill(self):
        print()
        print("Write how many ml of water do you want to add:")
        fill_water = int(input())
        print("Write how many ml of milk do you want to add:")
        fill_milk = int(input())
        print("Write how many grams of coffee beans do you want to add:")
        fill_beans = int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        fill_cups = int(input())
        self.water += fill_water
        self.milk += fill_milk
        self.beans += fill_beans
        self.cups += fill_cups

    def take(self):
        print()
        self.money = 0
        print(f"I gave you ${self.money}")

    def main(self):
        print("Write action (buy, fill, take, remaining, exit):")
        action = input()
        while action != "exit":
            if action == "buy":
                print()
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
                coffee_type = input()
                if coffee_type != "back":
                    self.buy(coffee_type)
            elif action == "fill":
                self.fill()
            elif action == "remaining":
                self.remaining()
            elif action == "take":
                self.take()
            print()
            print("Write action (buy, fill, take, remaining, exit):")
            action = input()
                
coffee = CoffeeMachine(water, milk, beans, cups, money)
coffee.main()           
