import gamefunctions
#FIXME: add in new functions and fix weird monster thing
print("Hello! To begin your adventure, enter your name: ")
user_name = input()
print_welcome(user_name)
print("Let's find out what kind of monster you are")
user_monster = create_new_monster()
print(user_monster[name], user_monster[description])
print(f"Here's your stats:\nHealth: {user_monster[health]}\nPower: {user_monster[power]}\n Money: {user_monster[money]}")
print("What would you like to purchase?")
print_shop_menu("Sword", 15, "Healing Potion", 5)
purchase = strip.lower.input()
print("How many would you like to buy? ")
amount = int(input())
if purchase == 'sword':
  purchase_item(15,amount,user_monster[money])
elif purchase == 'healing potion':
  purchase_item(5,amount,user_monster[money])
else:
  print("That item isn't for sale")

  
