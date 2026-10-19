#gamefunctions.py
#kaden beckham
#10/2/2026

#imports random module
import random

#creates function purchase_item that takes three perameters
#calculates and returns values for number of purchasable items and leftover money
def purchase_item(itemPrice, startingMoney, quantityToPurchase = 1):
    '''purchase_item takes the parameters itemPrice, startingMoney, and
quantityToPurchase. Using these parameters, number of purchaseable items
and leftover money after purchase are calculated and returned'''
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
        
#creates function new_random_monster with zero perameters
#randomly selects monster and assigns variables based on monster with some variability
#returns values in a dictionary so they can be called later
def new_random_monster():
    '''new_random_monster takes no parameters. Using the imported random module,
 a random monster is chosen, and a corresponding description, and values for health,
 power, and money are chosen with variance. the name, description, and remainding
 values are returned in a dictionary'''
    names = ("zombie", "skeleton", "werewolf")
    name = random.choice(names)
    if name == "zombie":
        description = "an undead person that attacks and eats the flesh of living people"
        health = random.randint(60, 80)
        power = random.randint(40, 60)
        money = random.randint(500, 1000)
    elif name == "skeleton":
        description = ("form of physically manifested undead made up of only animated bones, almost always carrying a weapon")
        health = random.randint(20, 40)
        power = random.randint(80, 100)
        money = random.randint(1000, 2000)
    else:
        description = ("a human being that has the ability to alter its form into a wolf-like animal")
        health = random.randint(40, 60)
        power = random.randint(60, 80)
        money = random.randint(1, 500)
    return {"name": name, "description": description, "health": health, "power": power, "money": money, }

#creates function print_welcome with perameters name and with that can be called
#prints called name centered across called width
def print_welcome(name, width):
    '''print_welcome takes 2 parameters name, and width. The name is printed
 in the center of the field defined by the width parameter'''
    print(f"{name:^{width}}")
    
#creates function print_shop_menu with 4 parameters that are formated in a menu
def print_shop_menu(item1Name, item1Price, item2Name, item2Price):
    '''print_shop_menu takes the parameters item1Name, item1Price, item2Name,
 and item2Price. the prices are then stored in variables with a dollar sign
 before and the price formated to 2 decimal places. Now 4 print statements
 build our menu with proper centering and a border'''
    price1 = f"${item1Price:.2f}"
    price2 = f"${item2Price:.2f}"
    print(f"/{"-"*22}\\")
    print(f"| {item1Name:<12}{price1:>8} |")
    print(f"| {item2Name:<12}{price2:>8} |")
    print(f"\\{"-"*22}/")

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

