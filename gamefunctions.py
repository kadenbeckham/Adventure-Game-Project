'''This module contains 4 functions that serve different purposes.

using the different functions, you can calculate values related to 
purchasing items, randomly create a monster with variance between each
monster, print a welcome message, and print a formatted shop menu'''

#gamefunctions.py
#kaden beckham
#10/2/2026


#imports random module
import random

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

#function town_menu takes two perameters
#prints users current location
#prints users health points and gold values
#prints three options for the player to choose and returns the choice
def town_menu(hp, gold):
    '''
    Prints menu while play is in the town location

    Parameters: 
        hp: the current health points of the player
        gold: the current ammount of gold the player has

    Returns:
        user input: the players choice of action
    '''
    print("\nYou are in town.")
    print(f"HP: {hp}, Gold: {gold}")
    print("What would you like to do?\n")
    print("1) Leave town (Fight Monster)")
    print("2) Sleep (Restore HP for 100 Gold)")
    print("3) Quit\n")
    return input("enter number for choice: ")

#function town_choice takes four perameters
#if choice is 1, fight_monster definition is called
#if choice is 2 and cost requirement is confirmed, gold is taken away,
#and the users hp is reset to the maximum
def town_choice(choice, hp, gold, max_hp):
    '''
    Continues choice 1 and choice 2 from the town menu

    Parameters: 
        choice: the decision made by the player
        hp: the current health points of the player
        gold: the current ammount of gold the player has
        max_hp: the total hp the player could have

    Returns:
        hp: the current hp of the player(after sleep or fight)
        gold: the current ammount of gold the player has(after sleep or fight)
    '''
    if choice == "1":
        hp, gold = fight_monster(hp, gold)
    elif choice == "2":
        if gold >= 100:
            gold -= 100
            hp = max_hp
            print("You sleep and restore your health.")
        else:
            print("Not enough gold to sleep.")
            
    return hp, gold

#function get_user_fight_action takes two perameters
#prints the HP of the monster and the player
#prints users two fight action options
#asks the user to pick a choice and returns the choice
def get_user_fight_action(hp, monster_hp):
    '''
    Prints options menu for monster interaction

    Parameters: 
        hp: the current health points of the player
        monster_hp: the current healh points of the monster

    Returns:
        user input: the players choice of action
    '''
    print(f"\nYour HP: {hp} | Monster HP: {monster_hp}")
    print(f"1) Attack")
    print(f"2) Run away")
    return input("Choose fight action: ")

#function fight_monster takes two perameters
#calls new_random_monster, stores values related to the monster
#stores random value for characters damage
#while loop calls get_user_fight_action as long as user and monster health is greater than zero
#characters and monsters health points are updated if they hit eachother
#if monster health goes below zero, monster gold is added to player gold
#if player health goes below zero and the monster is still alive, the player is defeated
def fight_monster(character_health, character_gold):
    '''
    establishes monster fight sequence

    Parameters: 
        character_health: the current health points of the player
        character_gold: the ammount of gold the player currently has

    Returns:
        character_health: updated character health points post altercation
        character_gold: updated character gold ammount post altercation
    '''
    monster = new_random_monster()
    
    monster_name = monster["name"]
    monster_desc = monster["description"]
    monster_health = monster["health"]
    monster_power = monster["power"]
    monster_money = monster["money"]
    
    character_damage = random.randint(45, 60)
    
    print(f"\nA {monster_name} appears")
    print(f"Description: {monster_desc}")
    print(f"Monster Stats - HP: {monster_health} | Power: {monster_power} | Bounty: {monster_money} Gold")
    
    while character_health > 0 and monster_health > 0:
        user_action = get_user_fight_action(character_health, monster_health)
        
        if user_action == "1":
            monster_health -= character_damage
            character_health -= monster_power
            print(f"You hit the {monster_name}. It hits you back for {monster_power} damage.")
        elif user_action == "2":
            print("You ran away safely")
            break 
        else:
            print("Invalid, please choose 1 or 2.")
            
    if monster_health <= 0:
        print(f"You defeated the {monster_name} and earned {monster_money} gold.")
        character_gold += monster_money
    elif character_health <= 0:
        print("You have been defeated.")
        
    return character_health, character_gold
