class CoffeeMachine:
    money, water, milk, coffee_beans, disposable_cups = 550, 400, 540, 120, 9

    def get_status(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.coffee_beans, "of coffee beans")
        print(self.disposable_cups, "of disposable cups")
        print(self.money, "of money")

    def make_espresso(self):
        self.money += 4
        self.water -= 250
        self.coffee_beans -= 16
        self.disposable_cups -= 1
        if self.water > 0 and self.coffee_beans > 0 and self.disposable_cups > 0:
            print("I have enough resources, making you a coffee!")
        else:
            if self.water < 0:
                print("Sorry, not enough water!")
            if self.coffee_beans < 0:
                print("Sorry, not enough coffee beans!")
            if self.disposable_cups < 0:
                print("Sorry, not enough disposable cups!")
            self.water += 250
            self.coffee_beans += 16
            self.disposable_cups += 1

    def make_latte(self):
        self.money += 7
        self.water -= 350
        self.milk -= 75
        self.coffee_beans -= 20
        self.disposable_cups -= 1
        if self.water > 0 and self.coffee_beans > 0 and self.disposable_cups > 0 and self.milk > 0:
            print("I have enough resources, making you a coffee!")
        else:
            if self.water < 0:
                print("Sorry, not enough water!")
            if self.coffee_beans < 0:
                print("Sorry, not enough coffe beans!")
            if self.disposable_cups < 0:
                print("Sorry, not enough disposable cups!")
            if self.milk < 0:
                print("Sorry, not enough milk!")
            self.water += 350
            self.coffee_beans += 20
            self.milk += 75
            self.disposable_cups += 1

    def make_cappuccino(self):
        self.money += 6
        self.water -= 200
        self.milk -= 100
        self.coffee_beans -= 12
        self.disposable_cups -= 1
        if self.water > 0 and self.coffee_beans > 0 and self.disposable_cups > 0 and self.milk > 0:
            print("I have enough resources, making you a coffee!")
        else:
            if self.water < 0:
                print("Sorry, not enough water!")
            if self.coffee_beans < 0:
                print("Sorry, not enough coffe beans!")
            if self.disposable_cups < 0:
                print("Sorry, not enough disposable cups!")
            if self.milk < 0:
                print("Sorry, not enough milk!")
            self.water += 200
            self.coffee_beans += 12
            self.milk += 100
            self.disposable_cups += 1

    def take(self):
        print("I gave you $", self.money)
        self.money = 0

    def fill(self, water, milk, coffee_beans, disposable_cups):
        self.water += water
        self.milk += milk
        self.coffee_beans += coffee_beans
        self.disposable_cups += disposable_cups


coffee_machine = CoffeeMachine()

coffee_machine.get_status()


def show_actions():
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    if action == "buy":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")

        coffee_type = input()
        if coffee_type == "1":
            coffee_machine.make_espresso()
        elif coffee_type == "2":
            coffee_machine.make_latte()
        elif coffee_type == "3":
            coffee_machine.make_cappuccino()
        else:
            show_actions()
    elif action == "fill":
        coffee_machine.fill(int(input("Write how many ml of water do you want to add:")),
                            int(input("Write how many ml of milk do you want to add:")),
                            int(input("Write how many grams of coffee beans do you want to add:")),
                            int(input("Write how many disposable cups of coffee do you want to add:")))
    elif action == "take":
        coffee_machine.take()
    elif action == "remaining":
        coffee_machine.get_status()
    elif action == "exit":
        return True


while True:
    if show_actions():
        break
