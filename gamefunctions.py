'''This module contains 4 functions that serve different purposes.

using the different functions, you can calculate values related to 
purchasing items, randomly create a monster with variance between each
monster, print a welcome message, and print a formatted shop menu'''

#gamefunctions.py
#kaden beckham
#10/2/2026


#imports random module
import random

#function purchase_item takes three perameters
#calculates values for number of purchasable items and leftover money
def purchase_item(itemPrice, startingMoney, quantityToPurchase = 1):
    '''
    Calculates leftover money and number of purchaseable items.

    Parameters: 
        itemPrice: The amount of money the item costs
        startingMoney: The amount of money the user starts with
        quantityToPurchase: The amount of items available to buy

    Returns:
        num_purchased: The amount of items the user can purchase
        leftover_money: The amount of money left over after purchasing
    '''
    num_purchased = startingMoney // itemPrice
    if num_purchased <= quantityToPurchase:
        spent_money = num_purchased * itemPrice
        leftover_money = startingMoney - spent_money
        return num_purchased, leftover_money
    else:
        num_purchased = quantityToPurchase
        spent_money = num_purchased * itemPrice
        leftover_money = startingMoney - spent_money
        return num_purchased, leftover_money
        
#function new_random_monster takes zero perameters
#randomly selects monster and assigns variables based on monster
#variability added between each monster
#returns values in a dictionary so they can be called later
def new_random_monster():
    '''
    Generates a random monster with corresponding values.

    Parameters: 
        None

    Returns:
        name (name): The type of monster generated
        description (description): A description of the monster
        health (health): The health of the monster
        power (power): The power of the monster
        money (money): The money of the monster
    '''
    names = ("zombie", "skeleton", "werewolf")
    name = random.choice(names)
    if name == "zombie":
        description = ("an undead person that attacks and eats the "
        "flesh of living people")
        health = random.randint(60, 80)
        power = random.randint(40, 60)
        money = random.randint(500, 1000)
    elif name == "skeleton":
        description = ("form of physically manifested undead made up "
        "of only animated bones, almost always carrying a weapon")
        health = random.randint(20, 40)
        power = random.randint(80, 100)
        money = random.randint(1000, 2000)
    else:
        description = ("a human being that has the ability to alter "
        "its form into a wolf-like animal")
        health = random.randint(40, 60)
        power = random.randint(60, 80)
        money = random.randint(1, 500)
    return {"name": name, "description": description, "health": health,
    "power": power, "money": money}

#function print_welcome takes two perameters
#prints called name centered across called width
def print_welcome(name, width):
    '''
    Prints name given in function call centered across given widths

    Parameters: 
        name: The name that should be displayed
        width: The width you want the name centered in 

    Returns:
        None
    '''
    print(f"{name:^{width}}")
    
#function print_shop_menu takes 4 parameters
# names and prices are formated in a menu
def print_shop_menu(item1Name, item1Price, item2Name, item2Price):
    '''
    Formats called values for name and price into a menu

    Parameters: 
        item1Name: The name of the first item
        item1Price: The price of the first item
        item2Name: The name of the second item
        item2Price: The price of the second item

    Returns:
        None
    '''
    price1 = f"${item1Price:.2f}"
    price2 = f"${item2Price:.2f}"
    print(f"/{"-"*22}\\")
    print(f"| {item1Name:<12}{price1:>8} |")
    print(f"| {item2Name:<12}{price2:>8} |")
    print(f"\\{"-"*22}/")


def test_functions():
    num_purchased, leftover_money = purchase_item(123, 1000, 3)
    print(num_purchased)
    print(leftover_money)

    num_purchased, leftover_money = purchase_item(123, 201, 3)
    print(num_purchased)
    print(leftover_money)

    num_purchased, leftover_money = purchase_item(341, 2112)
    print(num_purchased)
    print(leftover_money)

    my_monster = new_random_monster()
    print(my_monster["name"])
    print(my_monster["description"])
    print(my_monster["health"])
    print(my_monster["power"])
    print(my_monster["money"])

    print_welcome("kaden", 20)
    print_welcome("jeff", 10)
    print_welcome("big dawg", 15)

    print_shop_menu("Apple", 31, "Pear", 1.234)
    print_shop_menu("Egg", .23, "Bag of Oats", 12.34)
    print_shop_menu("banana", .83, "milk", 3.89)

if __name__ == "__main__":
    test_functions()