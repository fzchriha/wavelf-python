class CoffeeMachine:
    
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def __str__(self):
        return """ "The coffee machine has:
        {} of water
        {} of milk
        {} of beans
        {} of disposable cups
        ${} of money""".format(self.water, self.milk, self.beans, self.cups, self.money)
        

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        buy_options = input()
        if buy_options == "1":
            if self.water > 250 and self.beans > 16 and self.cups > 1:
                self.water -= 250
                self.beans -= 16
                self.money += 4
                self.cups -= 1
                print("I have enough resources, making you a coffee!")
            else:
                if self.water < 250:
                    print("Sorry not enough water.")
                if self.beans < 16:
                    print("Sorry not enough beans.")
                if self.cups < 1:
                    print("Sorry not enough cups.")
        elif buy_options == "2":
            if self.water > 350 and self.milk > 75 and self.beans > 20 and self.cups > 1:
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.money += 7
                self.cups -= 1
                print("I have enough resources, making you a coffee!")
            else:
                if self.water < 350:
                    print("Sorry, not enough water.")
                if self.milk < 75:
                    print("Sorry, not enough milk.")
                if self.beans < 20:
                    print("Sorry, not enough beans.")
                if self.cups < 1:
                    print("Sorry, not enough cups.")
        elif buy_options == "3":
            if self.water > 200 and self.milk > 100 and self.beans > 12 and self.cups > 1:
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.money += 6
                self.cups -= 1
                print("I have enough resources, making you a coffee!")
            else:
                if self.water < 200:
                    print("Sorry, not enough water.")
                if self.milk < 100:
                    print("Sorry, not enough milk.")
                if self.beans < 12:
                    print("Sorry, not enough beans.")
                if self.cups < 1:
                    print("Sorry, not enough cups.")
        elif buy_options == "back":
            pass


    def fill(self):
        print("Write how many ml of water do you want to add:")
        filled_water = int(input())
        print("Write how many ml of milk do you want to add:")
        filled_milk = int(input())
        print("Write how many grams of coffee beans do you want to add:")
        filled_beans = int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        filled_cups = int(input())
        self.water += filled_water
        self.milk += filled_milk
        self.beans += filled_beans
        self.cups += filled_cups

    def take(self):
        print("I gave you $", self.money)
        self.money = 0

    def remaining(self):
        print(self)
    

# how the program actually runs 


coffee_machine = CoffeeMachine()
print("Write action (buy, fill, take, remaining, exit):")
option = input()
print("")

while option != "exit":
    if option == "buy":
        coffee_machine.buy()
        print("")

    elif option == "fill":
        coffee_machine.fill()
        print("")

    elif option == "take":
        coffee_machine.take()
        print("")

    elif option == "remaining":
        coffee_machine.remaining()

    elif option == "exit":
        break
    
    print("Write action (buy, fill, take, remaining, exit):")
    option = input()
    print("")
    
