import gamefunctions
#FIXME: add in new functions and fix weird monster thing
print("Hello! To begin your adventure, enter your name: ")
gamefunctions.user_base['name'] = input()
gamefunctions.print_welcome(gamefunctions.user_base["name"])
gamefunctions.game_menu()
print('Thank you for playing!')
