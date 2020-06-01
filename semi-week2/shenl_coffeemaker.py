class Coffee:
    def __init__(self, water, milk, beans, cost):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cost = cost

# espresso, latte, cappuccino
class coffeeOptions:
    espresso = Coffee(250, 0, 16, 4)
    latte = Coffee(350, 75, 20, 7)
    cappuccino = Coffee(200, 100, 12, 6)

class Resources:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.disp_cups = 9
        self.money = 550

    def buy(self, coffee):
    #subtract amount of ingredients needed for different type of coffee based off of parameter
        water = self.water - coffee.water
        milk = self.milk - coffee.milk
        beans = self.beans - coffee.beans
        disp_cups = self.disp_cups - 1
        if water < 0:
            print('Sorry, not enough water!')
        elif milk < 0:
            print('Sorry, not enough milk!')
        elif beans < 0:
            print('Sorry, not enough coffee beans!')
        elif disp_cups < 0:
            print('Sorry, not enough disposable cups!')
        else:
            print('I have enough resources, making you a coffee!')
            self.water = water
            self.milk = milk
            self.beans = beans
            self.disp_cups = disp_cups
            self.money += coffee.cost

    def make_coffee(self):
        choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
        if choice == '1':
            self.prepare_coffee(coffeeOptions.espresso)
        if choice == '2':
            self.prepare_coffee(coffeeOptions.latte)
        if choice == '3':
            self.prepare_coffee(coffeeOptions.cappuccino)

    def fill(self):
        self.water += int(input('Write how many ml of water the coffee machine has: '))
        self.milk += int(input('Write how many ml of milk the coffee machine has: '))
        self.beans += int(input('Write how many grams of coffee beans the coffee machine has: '))
        self.disp_cups += int(input('Write how many disposable cups of coffee do you want to add: '))

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0

    def remaining(self):
        print(f'The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.beans} of coffee beans')
        print(f'{self.disp_cups} of disposable cups')
        print(f'${self.money} of money')


class CoffeeMachine:
    def __init__(self):
        self.cup_of_coffee = coffeeOptions()
        self.resources = Resources()
        self.need_cups = 0
        self.affordable_cups = 0
        self.main()

#MAIN
    def main(self):
        while True:
            action = input('Write action (buy, fill, take, remaining, exit): ')
            print()
            if action == 'buy':
                self.resources.buy()
                print()
            elif action == 'fill':
                self.resources.fill()
                print()
            elif action == 'take':
                self.resources.take()
                print()
            elif action == 'remaining':
                self.resources.remaining()
                print()
            elif action == 'exit': #end the program here
                break

#INSTANCE OBJECT
test = CoffeeMachine()
