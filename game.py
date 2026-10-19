import gamefunctions

num_purchased, leftover_money = gamefunctions.purchase_item(123, 1000, 3)
print(num_purchased)
print(leftover_money)

my_monster = gamefunctions.new_random_monster()
print(my_monster["name"])
print(my_monster["description"])
print(my_monster["health"])
print(my_monster["power"])
print(my_monster["money"])

username = str(input("enter name: "))
gamefunctions.print_welcome(username, 20)

gamefunctions.print_shop_menu("Apple", 31, "Pear", 1.234)

gamefunctions.test_functions()