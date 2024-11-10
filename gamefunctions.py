#gamefunctions.py
#Fynch Andrus
#11/09/2024

#Create modual summary DocString using the comments in file
#turn individual function comments into doc strings
#Create functions to allow for game play

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
        health = random.randint(12,26)
        power = random.randint(8,12)
        money = random.randint(27,42)
        return [name, description, health, power, money]
    elif monster == 2:
        name = 'Imp'
        description = 'Tiny fiend (devil, shapechanger)'
        health = random.randint(11,25)
        power = random.randint(8,12)
        money = random.randint(42,56)
        return [name, description, health, power, money]
    elif monster == 3:
       name = 'Skeleton'
       description = 'Remanants of the undead, resurrected.'
       health = random.randint(6,20)
       power = random.randint(12,16)
       money = random.randint(20,34)
       return [name, description, health, power, money]
    
monster_list = new_random_monster()

def user_base():
    '''This function provides base values to allow functions to work. These also work as
    starting values for a new player to use.
    
    Parameters: None
    
    Returns:
     name(str): name of the player, default "User"
     money(int): starting money for player, default 10
     health(int): starting and reset health for player, default 30
     power(randint): starting damage player can deal, range of 5 to 15.

    Example:
     >>> money, health = user_base()
     >>>print(health)
     30
     >>>print(money)
     10'''
    
    name = 'User'
    money = 10
    health = 30
    power = random.randint(5,15)
    return [name, money, health, power]
      
userBase_list = user_base()

def display_health_bar(monster,monster_health,user,user_health):
    '''This function is to display the health bar of both the player and the monster during
    a fight. The bar will decrease as they lose health.
    
    Parameters:
     monster(str): name of the monster in the fight.
     monster_health(int): how much health the monster has.
     user(str): name of the player in the fight.
     user_health(int): how much health the user has.
     
    Returns:
     None
     
    Example:
    >>>displayFightStatistics('Skeleton',20,'User', 30)
    |Skeleton: 20          30 :User|
    |----------     ---------------|'''
    
    monster_setup = monster + ': ' + str(monster_health)
    user_setup = str(user_health) + ': ' + user
    monster_health_bar = '-' * (monster_health // 2)
    user_health_bar = '-' * (user_health // 2)
    print(f'|{monster_setup:15}{user_setup:>15}|')
    print(f'|{monster_health_bar:15}{user_health_bar:>15}|')

def user_action(source):
    '''This function is to retrieve and process the actions that a player will make.
    
    Parameters:
     source(str): this is what function the choice comes from
     '''
    if source == 'game_menu':
        print("What would you like to do? (Enter number)\n")
        choice = int(input())
        while choice not in [1, 2, 3, 4]:
            print("Please enter the digit that corresponds with the action you would like to make.")
            print("1) Fight Monster\n2) Sleep(Restore HP for 5 Gold)\n3) Quit\n")
            choice = int(input())          
        if choice == 1:
            '''FIXME: I want to call these functions but they have their own parameters and I don't know what those are.
            I also think I'm over-beefing this function because the work is supposed to be done by the functions, this is just to
            process input variables so name == main will work without requiring inputs
            new_random_monster()
            display_health_bar()
            user_fight_options()'''
            pass
        elif choice == 2:
            user_sleep()
        elif choice == 3:
            print('Goodbye')
    elif source == 'fight_options':
        pass

def game_menu():
    print('Hello! Welcome to the game menu!')
    print('Here you can access any of the things you may want to do!')
    print("1) Fight Monster\n2) Sleep(Restore HP for 5 Gold)\n3) Quit\n")
    
def user_sleep():
    pass

def user_fight_options():
    pass
    
def test_functions():
    print_welcome('User')
    print_shop_menu('Apple',1.25,'Orange',1.50)
    purchase_item(1.25, 4, 2)
    new_random_monster()
    #new functions: 
    user_base()
    display_health_bar('Sprite', 20, 'User', 10)
    user_action('game_menu')
    #FIXME: game_menu()
    #FIXME: user_fight_options()
    #FIXME: user_sleep()

if __name__ == "__main__":
    test_functions()
