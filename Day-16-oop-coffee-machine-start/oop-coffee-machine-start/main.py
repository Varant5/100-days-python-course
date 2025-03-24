from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

start_menu = Menu()
coffee_machine = CoffeeMaker()
money_coffee_machine = MoneyMachine()

while True:
    choice = input(f"What would you like?: {start_menu.get_items()} ")

    if choice == "off":
        break

    elif choice == "report":
        coffee_machine.report()
        money_coffee_machine.report()

    else:
        chosen_drink = start_menu.find_drink(choice)
        enough_resources = coffee_machine.is_resource_sufficient(chosen_drink)
        if enough_resources:
            drink_cost = money_coffee_machine.make_payment(chosen_drink.cost)
            if drink_cost:
                coffee_machine.make_coffee(chosen_drink)









