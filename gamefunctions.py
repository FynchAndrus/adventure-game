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
    

'''This function will return the number of items purchased and the
quantity of money that is remaining. If unable to afford all the
items, it will only buy as many as can be afforded. Nothing is printed
by the function call. The quantityToPurchase parameter has a default value of 1.'''

def purchase_item(itemPrice, startingMoney, quantityToPurchase=1):
    quantityPurchased = startingMoney // itemPrice
    if quantityPurchased > quantityToPurchase:
        quantityPurchased = quantityToPurchase
    else:
        quantityPurchased = quantityPurchased
    leftoverMoney = startingMoney - (itemPrice * quantityPurchased)
    return quantityPurchased, leftoverMoney

'''This function will return 1 of 3 available monsters as well as its description, health,
power, and money. The amount of money will be random but confined to a range around 15.'''
import random
def new_random_monster():
    monster = random.randint(1,3)
    if monster == 1:
        name = 'Sprite'
        description = 'Tiny fey creature, often associated with the natural elements.'
        health = random.randint(12,17)
        power = random.randint(8,12)
        money = random.randint(27,45)
        return name, description, health, power, money
    elif monster == 2:
        name = 'Imp'
        description = 'Tiny fiend (devil, shapechanger)'
        health = random.randint(11,15)
        power = random.randint(8,12)
        money = random.randint(42,57)
        return name, description, health, power, money
    elif monster == 3:
       name = 'Skeleton'
       description = 'Remanants of the undead, resurrected.'
       health = random.randint(6,10)
       power = random.randint(12,17)
       money = random.randint(20,36)
       return name, description, health, power, money





