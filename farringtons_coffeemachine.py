#At the moment, the coffee machine has $550, 400 ml of water, 540 ml of milk, 120 g of coffee beans, and 9 disposable cups.
money = 550
water = 400
milk = 540
beans = 120
cups = 9
action = 0
class Coffeemachine:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
    def communicate(self, prompt):
        return input(prompt)
    def change_materials(self, changeWater, changeMilk, changeBeans, changeCups, changeMoney):
        self.water -= changeWater
        self.milk -= changeMilk
        self.beans -= changeBeans
        self.cups -= changeCups
        self.money -= changeMoney
    def tell_remaining(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"${self.money} of money")
coffee_machine = Coffeemachine(400,540,120,9,550)        
        
while action != "exit":
    action = coffee_machine.communicate("Write action (buy, fill, take, remaining, exit):")
    if action == "buy":
        action = coffee_machine.communicate("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if action == "1":
            if coffee_machine.water >= 250 and coffee_machine.beans >= 16 and coffee_machine.cups >= 1:
                print("I have enough resources, making you a coffee!")
                coffee_machine.change_materials(250, 0, 16, 1, -4)
            else:
                if coffee_machine.water < 250:
                    print("Sorry, not enough water!")
                if coffee_machine.beans < 16:
                    print("Sorry, not enough coffee beans!")
                if coffee_machine.cups < 1:
                    print("Sorry not enough disposable cups!")
        if action == "2":
            if coffee_machine.water >= 350 and coffee_machine.milk >= 75 and coffee_machine.beans >= 20 and coffee_machine.cups >= 1:
                print("I have enough resources, making you a coffee!")
                coffee_machine.change_materials(350, 75, 20, 1, -7)
            else:
                if coffee_machine.water < 350:
                    print("Sorry, not enough water!")
                if coffee_machine.milk < 75:
                    print("Sorry, not enough milk!")
                if coffee_machine.beans < 20:
                    print("Sorry, not enough coffee beans!")
                if coffee_machine.cups < 1:
                    print("Sorry not enough disposable cups!")
        if action == "3":
            if coffee_machine.water >= 200 and coffee_machine.milk >= 100 and coffee_machine.beans >= 12 and coffee_machine.cups >= 1:
                print("I have enough resources, making you a coffee!")
                coffee_machine.change_materials(200, 100, 12, 1, -6)
            else:
                if coffee_machine.water < 200:
                    print("Sorry, not enough water!")
                if coffee_machine.milk < 100:
                    print("Sorry, not enough milk!")
                if coffee_machine.beans < 12:
                    print("Sorry, not enough coffee beans!")
                if coffee_machine.cups < 1:
                    print("Sorry not enough disposable cups!")
        if action == "back":
            continue       
    if action == "fill":
        coffee_machine.water += int(input("Write how many ml of water do you want to add:"))
        coffee_machine.milk += int(input("Write how many ml of milk do you want to add:"))
        coffee_machine.beans += int(input("Write how many grams of coffee beans do you want to add:"))
        coffee_machine.cups += int(input("Write how many disposible cups of coffee do you want to add:"))
    if action == "take":
        print(f"I gave you ${coffee_machine.money}")
        coffee_machine.money = 0
    if action == "remaining":
        coffee_machine.tell_remaining()
        
    
