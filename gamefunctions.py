#gamefunctions.py
#Fynch Andrus
#10/20/2024

#Create modual summary DocString using the comments in file
#turn individual function comments into doc strings

'''gamefunctions.py is a module containing definitions to aid in game play.

The definitions in this module are print_welcome - which takes in users name
from input and outputs a greeting; print_shop_menu - takes items and their corresponding
price from input and formats it into a menu; purchase_item - takes item price, the
amount of money user has, and how many items are purchased and outputs the remaining
money available and the number of items purchased; and new_random_monster - which
outputs a monster and its corresponding description, health, power, and money.'''

#Call functions print_welcome and print_shop_menu 3 times with
#3 different inputs to demonstrate them working within your program.

def print_welcome(name):
    '''This function will return the statement 'Hello, [user]!' centered in a 20
    character frame with the name taken from user input.

    Parameters:
     name(str): The name of user.

    Returns:
     Print statement of greeting.

    Example:
     >>>print_welcome(Joe)
          Hello Joe!     '''
    
    width = 20
    welcome = 'Hello '+name+'!'
    return print(f'{welcome:^20}')

def print_shop_menu(item1Name,item1Price,item2Name,item2Price):
    '''This function will return a menu that is a list of 2 items and their corresponding prices.
    These will be formatted in a menu style listing items with its corresponding price
    The price needed extra steps to be formmated correctly including forcing the float and
    connecting the '$' so they would shift together.
    
    Parameters:
     item1Name(str): name of the first item
     item1Price(float): price of first item
     item2Name(str): name of second item
     item2Price(float): price of second item
     
    Returns:
     None
     
    Example:
    >>>print_shop_menu('Apple',1.25,'Orange',1.50)
    /--------------------\
    |Apple          $1.25|
    |Orange         $1.50|
    \--------------------/'''
    
    price1 = "{:.2f}".format(item1Price)
    item1Format = '$'+price1
    price2 = "{:.2f}".format(item2Price)
    item2Format = '$'+price2
    header = print('/'+'-'*20+'\\')
    item1 = print(f'|{item1Name:12}{item1Format:>8}|')
    item2 = print(f'|{item2Name:12}{item2Format:>8}|')
    footer = print('\\'+'-'*20+'/')
    
def purchase_item(itemPrice, startingMoney, quantityToPurchase=1):
    '''This function will return the number of items purchased and the
    quantity of money that is remaining. If unable to afford all the items,
    it will only buy as many as can be afforded. Nothing is printed by the
    function call. The quantityToPurchase parameter has a default value of 1.
    
    Parameters:
     itemPrice(float): Price of the item being purchased
     startingMoney(float): How much money user has prior to the transaction
     quantityToPurchase(int): The number of items being purchased. Has a default
     value of 1.
     
    Returns:
     quantityPurchased(int): The actual number of items purchased
     leftoverMoney(float): How much money user has after the transaction.
     
    Example:
    >>> amountPurchased, remainingMoney = purchase_item(1.25, 4, 2)
    >>>print(amountPurchased)
    2
    >>>print(remainingMoney)
    1.50'''
    
    quantityPurchased = startingMoney // itemPrice
    if quantityPurchased > quantityToPurchase:
        quantityPurchased = quantityToPurchase
    else:
        quantityPurchased = quantityPurchased
    leftoverMoney = startingMoney - (itemPrice * quantityPurchased)
    return quantityPurchased, leftoverMoney

import random
def new_random_monster():
    '''This function will return 1 of 3 available monsters - Sprite, Imp, Skeleton -  as well
    as its description, health, power, and money. The amount of money, health, and power will 
    be random but confined to a range around 15.
    
    Parameters:
     None
     
    Returns:
     name(str): Name of the monster created
     description(str): Description of the monster
     health(randint): How much health the monster begins with. Has range of 5.
     power(randint): How much damage each monster deals. Has a range of 5.
     money(randint): How much money each monster has. Has range of 15.
     
    Example:
     >>> name, decription = new_random_monster()
     >>>print(name)
     Sprite
     >>>print(description)
     Tiny fey creature, often asscociated with the natural elements.
     >>> name, power = new_random_monster()
     >>> print(name, power)
     Skeleton 14'''
    
    monster = random.randint(1,3)
    if monster == 1:
        name = 'Sprite'
        description = 'Tiny fey creature, often associated with the natural elements.'
        health = random.randint(12,16)
        power = random.randint(8,12)
        money = random.randint(27,42)
        return name, description, health, power, money
    elif monster == 2:
        name = 'Imp'
        description = 'Tiny fiend (devil, shapechanger)'
        health = random.randint(11,15)
        power = random.randint(8,12)
        money = random.randint(42,56)
        return name, description, health, power, money
    elif monster == 3:
       name = 'Skeleton'
       description = 'Remanants of the undead, resurrected.'
       health = random.randint(6,10)
       power = random.randint(12,16)
       money = random.randint(20,34)
       return name, description, health, power, money

def user_base(name):
    name = name
    money = 10
    health = 30
    power = random.randint(5,15)
    return name, money, health, power
    
def displayFightStatistics():
    print(f'{new_random_monster[name]}: {new_random_monster[health]:20}{user_base[health]} :{user_base[name]}')

def userFightOptions():
    print('Would you like to...\n1) Fight\n2) Run away')
    action = input()
    while action != ('1' or '2'):
        print("Please enter the digit that corresponds with the action you would like to make") 
    while user_health > 0:
        if action == '1':
            monster_health -= user_base[power]
            user_health -= new_random_monster[power]
            displayFightStatistics(monster_name,monster_health,user_name,user_health)
            action = input()
        else:
            game_menu()
    pass
def game_menu():
    print("Current HP: 30, Current Gold: 10")
    print("What would you like to do? (Enter number)\n")
    print("1) Fight Monster\n2) Sleep(Restore HP for 5 Gold)\n3) Quit\n")
    action = str(input())
    while action != ('1' or '2' or '3'):
        print("Please enter the digit that corresponds with the action you would like to make")
    if action == '1':
        displayFightSatistics()
        userFightOptions()
    elif action == '2':
        user_base[money] -= 5
        user_base[health] = 30
        return user_base[money], user_base[health]
    else:
        print('goodbye')

def user_base(name):
    name = name
    money = 10
    health = 30
    power = random.randint(5,15)
    return name, money, health, power

def test_functions():
    print_welcome('User')
    print_shop_menu('Apple',1.25,'Orange',1.50)
    purchase_item(1.25, 4, 2)
    new_random_monster()
    user_base('User')
    displayFightStatistics()
    userFightOptions()
    game_menu()

if __name__ == "__main__":
    test_functions()
