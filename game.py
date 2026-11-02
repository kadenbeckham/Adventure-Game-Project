import gamefunctions

character_health = 65
max_health = 75
character_gold = 100
playing = True

while playing == True:
    choice = gamefunctions.town_menu(character_health, character_gold)
        
    if choice == "3":
        print("Thanks for playing")
        playing = False
    elif choice == "1" or choice == "2":
        character_health, character_gold = gamefunctions.town_choice(choice, character_health, character_gold, max_health)
    else:
        print("Invalid, please enter a valid option.")
