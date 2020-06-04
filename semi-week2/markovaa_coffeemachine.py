class State:
    START = 'START'
    EXPECTING_ORDER = 'ORDER'
    EXPECTING_BUY_CHOICE = 'BUY'
    EXPECTING_WATER_FILL = " FILL WATER"
    EXPECTING_MILK_FILL = "FILL MILK"
    EXPECTING_BEANS_FILL = "FILL COFFEE BEANS"
    EXPECTING_CUPS_FILL = "FILL CUPS"

class CoffeeMachine:
    ORDER_MESSAGE = '\nWrite action (buy, fill, take, remaining, exit): '
    BUY_MESSAGE = '\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: '
    UNRECOGNIZED_ACTION = "\nCan't recognize your writing. Could you type better?"
    
    def __init__(self, water, milk, coffee, cups, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money
        self.state = State.START

    def process(self, user_input) :
        if self.state == State.EXPECTING_ORDER :
            if user_input == 'buy':
                print(self.BUY_MESSAGE)            
                self.state = State.EXPECTING_BUY_CHOICE
            elif user_input == 'fill':
                print('\nWrite how many ml of water do you want to add: ')
                self.state = State.EXPECTING_WATER_FILL
                        
            elif user_input == 'take':
                print(f"I gave you ${self.money}")
                self.money = 0
                print("\nWrite action (buy, fill, take, remaining, exit): ")
                self.state = State.EXPECTING_ORDER
            elif user_input == 'remaining':
                self.remaining()
                print(self.ORDER_MESSAGE)
            elif user_input == 'exit':
                exit()
            else:
                print(self.UNRECOGNIZED_ACTION)
                print(self.ORDER_MESSAGE)
        elif self.state == State.START :
            self.state = State.EXPECTING_ORDER
            print(self.ORDER_MESSAGE)
        elif self.state == State.EXPECTING_BUY_CHOICE :
            self.check(user_input)
            self.state = State.EXPECTING_ORDER
            print(self.ORDER_MESSAGE)
            # Add water
        elif self.state == State.EXPECTING_WATER_FILL:
            self.water += int(user_input)
            print('Write how many ml of milk you want to add: ')
            self.state = State.EXPECTING_MILK_FILL
        elif self.state == State.EXPECTING_MILK_FILL:
            self.milk += int(user_input)
            print('Write how many grams of beans you want to add: ')
            self.state = State.EXPECTING_BEANS_FILL
        elif self.state == State.EXPECTING_BEANS_FILL:
            self.coffee += int(user_input)
            print('Write how many disposable cups of coffee do you want to add: ') 
            self.state = State.EXPECTING_CUPS_FILL
        elif self.state == State.EXPECTING_CUPS_FILL:
            self.cups += int(user_input)
            print("\nWrite action (buy, fill, take, remaining, exit): ")
            self.state = State.EXPECTING_ORDER   


        else:
            print("State: " + self.state)


    def check(self, flavor):

        if flavor == '1':
            if self.water < 250:
                print('Sorry, not enough water!')
            elif self.coffee < 16:
                print('Sorry, not enough coffee!')
            elif self.cups < 1:
                self.print('Sorry, not enough cups!')
            else:
                print('I have enough resources, making you a coffee!')
                self.buy(flavor)

        elif flavor == '2':
            if self.water < 350:
                print('Sorry, not enough water!')
            elif self.milk < 75:
                print('Sorry, not enough milk!')
            elif self.coffee < 20:
                print('Sorry, not enough coffee!')
            elif self.cups < 1:
                print('Sorry, not enough disposable cups')
            else:
                print('I have enough resources, making you a coffee!')
                self.buy(flavor)

        elif flavor == '3':
            if self.water < 200:
                print('Sorry, not enough water!')
            elif self.milk < 100:
                print('Sorry, not enough milk!')
            elif self.coffee < 12:
                print('Sorry, not enough coffee!')
            elif self.cups < 1:
                print('Sorry, not enough disposable cups')
            else:
                print('I have enough resources, making you a coffee!')
                self.buy(flavor)

    def buy(self, flavor):
        global water, milk, coffee, money, disposable_cups
        if flavor == '1':
            self.water -= 250
            self.coffee -= 16
            self.cups -= 1
            self.money += 4
        elif flavor == '2':
            self.water -= 350
            self.milk -= 75
            self.coffee -= 20
            self.cups -= 1
            self.money += 7
        elif flavor == '3':
            self.water -= 200
            self.milk -= 100
            self.coffee -= 12
            self.cups -= 1
            self.money += 6

    def remaining(self):
        print('\nThe coffee machine has:')
        print(f'''{self.water} of water
{self.milk} of milk
{self.coffee} of coffee beans
{self.cups} of disposable cups
${self.money} of money''')

def main() :
    cm = CoffeeMachine(400, 540, 120, 9, 550)

    user_input = ""
    while True:
        cm.process(user_input)
        user_input = input()


if __name__ == "__main__":
    main()
