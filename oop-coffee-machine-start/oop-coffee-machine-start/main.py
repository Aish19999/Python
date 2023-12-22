from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
#menu_items = MenuItem()
money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
is_on = True

while is_on:
    options = menu.get_items()
    choose = input(f"What would you like to drink?({options}): ")
    if choose == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choose)
        print(drink)
        if coffe_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)





