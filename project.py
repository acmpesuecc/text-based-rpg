# Defining a function named typing.
import time, sys
from tkinter import *

def typing(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


import random

typing("Welcome to The Quest!!\n")
typing("Story...\n")
typing("Intro\n")

room = ("monster", "shop", "treasure box", "monster", "shop")

gold = 500  # used in store to buy items
hp = 100  # user's hp
opp_hp = 100  # monster's hp
extra_hp = 0  # extra opponent hp for boss round
Iron_Sword = False  # increases attack by 20
Mythril_Sword = False  # increases attack by 30
Orichalium_Sword = False  # increases attack by 40
Iron_Armour = False  # decreases opp_att by 10
Mythril_Armour = False  # decreases opp_att by 20
Orichalium_Armour = False  # decereases opp_att by 30
platinum_armour = False #decreases opp_att by 40
diamond_armour = False  #decraese opp_att by 45
potion = 1  # increases hp by 30. Cost=300 gold
ultra_potion = 1  # increases hp by 50. Cost=600 gold
which_potion = 0  # variable that lets you select the potion that you want to take.


def fight():
    global opp_hp
    global potion
    global ultra_potion
    global extra_hp
    opp_hp = int(100 + extra_hp)
    typing("The match starts. You get the first chance\n")
    global hp
    while not hp <= 0 or not opp_hp <= 0:
        if hp <= 0 or opp_hp <= 0:
            break
        else:
            typing("Would you like to attack or use potion??\n")
            d = int(float(input("1=Attack, 2=Use potions\n")))
            # for invalid inputs of d
            while d != 2 and d != 1:
                typing("Invalid input. Try again.\n")
                d = int(input("1=Attack, 2=Use potion\n"))
                if d == 2 or d == 1:
                    break
                else:
                    pass

            # If user decides to attack
            if d == 1:
                userattack = random.randint(40, 70)
                typing("You will do the attack now\n")
                opp_hp = opp_hp - userattack
                if Iron_Sword == True:
                    opp_hp = opp_hp - 20
                    # if opp hp goes below 0 after this..
                    if opp_hp < 0:
                        opp_hp = 0
                elif Mythril_Sword == True:
                    opp_hp = opp_hp - 30
                    # if opp hp goes below 0 after this..
                    if opp_hp < 0:
                        opp_hp = 0
                elif Orichalium_Sword == True:
                    opp_hp = opp_hp - 40
                    # if oppp hp goes below 0 after this..
                    if opp_hp < 0:
                        opp_hp = 0
                if opp_hp > 0:
                    typing(f"Monster's HP={opp_hp}\n")
                elif opp_hp <= 0:
                    opp_hp = 0
                    typing(f"Monster's HP={opp_hp}\n")

            # If user decided to use potion
            elif d == 2:
                typing("Which potion would you like to drink?\n")
                which_potion = input("1=Potion, 2=Ultra Potion\n")

                # for invalid inputs of which_potion
                while which_potion != "1" and which_potion != "2":
                    typing("Invalid input. Try again..")
                    which_potion = input("1=Potion, 2=Ultra Potion")
                    if which_potion == "1" or which_potion == "2":
                        break
                    else:
                        pass

                if hp == 100:
                    hp = hp + 0
                elif int(which_potion) == 1:
                    if potion > 0:
                        hp = hp + 30
                        potion = potion - 1
                    elif potion == 0:
                        typing("You don't have a potion with you.\n")
                elif int(which_potion) == 2:
                    if ultra_potion > 0:
                        hp = hp + 50
                    elif ultra_potion == 0:
                        typing("You don't have a ultra potion.\n")
                else:
                    typing("Invalid input. You lose your chance.\n")
                typing(f"Your HP={hp}\n")

            # Monster's turn to attack
            if opp_hp <= 0:
                hp = hp + 0
            elif opp_hp != 0:
                typing("Now monster will take it's turn.\n")
                opp_attack = random.randint(((m - 1) * 10), (m * 10))
                hp = hp - opp_attack
                if hp < 0:
                    hp = 0
                if Iron_Armour == True:
                    hp = hp + 10
                elif Mythril_Armour == True:
                    hp = hp + 20
                elif Orichalium_Armour == True:
                    hp = hp + 30
                print(f"Your HP={hp}\n")


def potion_time():
    global hp
    global potion
    global ultra_potion
    typing("You have some time to rest.\n")
    typing("Would you like to use a potion?\n")
    a = input("1=Yes, 2=No\n")

    # If invalid input for whether user wants a potion or not
    while int(a) != 2 and int(a) != 1:
        typing("Invalid input. Try again.\n")
        a = input("1=Yes, 2=No\n")
        if int(a) == 2 or int(a) == 1:
            break
        else:
            pass

            # If user wants to utilize potion break
    if int(a) == 1:
        typing("Which potion would you like to take?\n")
        potion_chosen = input("1=Potion, 2=Ultra Potion\n")

        # If invalid input for potion chosen
        while int(potion_chosen) != 2 and int(potion_chosen) != 1:
            typing("Invalid input. Try again.\n")
            potion_chosen = input("1=Potion, 2=Ultra Potion\n")
            if int(potion_chosen) == 2 or int(potion_chosen) == 1:
                break
            else:
                pass

        # If user decides to take potion
        if int(potion_chosen) == 1:
            # If user's HP is already 100
            if hp == 100:
                typing("Your HP is already 100\n")
            elif potion > 0:
                hp = hp + 30
                # If user HP goes above 100
                if hp > 100:
                    hp = 100
                potion = potion - 1
                typing(f"Your HP={hp}\n")
                typing(f"You now have {potion} Potions left\n")
            elif potion == 0:
                typing("You dont have any potions with you.")
        # If user decides to take ultra potion
        elif int(potion_chosen) == 2:
            # If user's HP is already 100
            if hp == 100:
                typing("Your HP is already 100\n")
            elif ultra_potion > 0:
                hp = hp + 50
                # If user HP goes above 100
                if hp > 100:
                    hp = 100
                ultra_potion = ultra_potion - 1
                typing(f"Your HP={hp}\n")
                typing(f"You now have {ultra_potion} Ultra Potions left\n")
            elif ultra_potion == 0:
                typing("You don't have any ultra potions left with you.")
        potion_time()
    # If user decides not to take any potion..
    elif int(a) == 2:
        pass


def shopping():
    global gold
    global Iron_Sword
    global Mythril_Sword
    global Orichalium_Sword
    global Iron_Armour
    global Mythril_Armour
    global Orichalium_Armour
    global diamond_armour
    global platinum_armour
    global potion
    global ultra_potion
    print("")
    typing("Welcome to the store..\n")
    typing("What would you like to buy?\n")
    # store1 variable to ask user what necessity do they need to buy
    store1 = input("1=Potion, 2=Sword, 3=Armor, 4=Exit Store\n")

    # if invalid input..
    while int(store1) != 1 and int(store1) != 2 and int(store1) != 3 and int(store1) != 4:
        typing("Invalid Input. Try again\n")
        store1 = input("1=Potion, 2=Sword, 3=Armor, 4=Exit Store\n")
        if int(store1) == 1 or int(store1) == 2 or int(store1) == 3 or int(store1) == 4:
            break
        else:
            pass

    # If user wants to buy potions
    if int(store1) == 1:
        print(f"You currently have {potion} Small potions and {ultra_potion} Ultra potions with you.\n")
        typing("We have 2 types of potion.\n")
        typing("Small Potion and Ultra Potion\n")
        typing("Would you like to know more about them?\n")
        z = input("1=Yes, 2=No\n")

        # if invalid input of z
        while int(z) != 1 and int(z) != 2:
            typing("Invalid input. Try again")
            z = input("1=Yes, 2=No")
            if z == 1 or z == 2:
                break
            else:
                pass

        # if user wants to know about potions
        if int(z) == 1:
            typing("Small potion that costs 250 gold will increase your HP by 30")
            typing("And..")
            typing("Ultra potion that costs 600 gold will increase your HP by 50")
        # if user doesn't need to know about potions
        if int(z) == 2:
            typing("Okay then..")

        typing("Which potion would you like to buy?")
        shop_potion = input("1=Small Potion, 2=Ultra Potion")

        # for invalid inputs of shop potion
        while int(shop_potion) != 1 and int(shop_potion) != 2:
            typing("Invalid input. Try again")
            shop_potion = input("1=Small Potion, 2=Ultra Potion")
            if int(shop_potion) == 1 or int(shop_potion) == 2:
                break
            else:
                pass

        # If user wantes to buy small potion
        if int(shop_potion) == 1:
            typing("How many Small potions would you like to buy?\n")
            typing("Cost=250 gold\n")
            no_of_small_potions = int(input(""))
            # If user doesn't have enough gold
            if gold - (no_of_small_potions * 250) < 0:
                typing("You don't have enough gold.\n")
                typing("Let's shop for something else..\n")
                shopping()
            # If user has enough gold
            else:
                potion = potion + no_of_small_potions
                gold = gold - (250 * no_of_small_potions)
                print(f"You now have {gold} gold with you")
                print(f"You now have {potion} Small Potions with you")
                typing("Let's continue shopping..")
                shopping()
        # If user wants to buy Ultra Potion
        elif int(shop_potion) == 2:
            typing("How many Ultra Potions would you like to buy?\n")
            typing("Cost=600 gold\n")
            no_of_ultra_potions = int(input(""))
            if gold - (no_of_ultra_potions * 600) < 0:
                typing("You don't have enough gold.")
                typing("Let's shop for something else.")
                shopping()
            else:
                ultra_potion = ultra_potion + no_of_ultra_potions
                gold = gold - (600 * no_of_ultra_potions)
                print(f"You now have {gold} gold with you")
                print(f"You now have {ultra_potion} Ultra Potions with you")
                typing("Let's continue shopping..")
                shopping()

    # If user wants to buy swords
    if int(store1) == 2:
        # Checking what sword does the user currently has..
        if sword1 == True and sword2 == False and sword3 == False:
            typing("Right now, you have Sword1")
        elif sword1 == False and sword2 == True and sword3 == False:
            typing("Right now you have Sword2")
        elif sword1 == False and sword2 == False and sword3 == True:
            typing("Right now you have Sword3")
        typing("We have 3 types of swords..\n")
        typing("Sword1, Sword2, Sword3")
        typing("Would you like to know more about them?\n")
        y = input("1=Yes or 2=No\n")

        # for invalid input of y
        while int(y) != 1 and int(y) != 2:
            typing("Invalid input. Try again\n")
            y = input("1=Yes, 2=No\n")
            if y == 1 or y == 2:
                break
            else:
                pass

        # If user wants to know about swords
        if int(y) == 1:
            typing("Sword1 costs 200 gold and increases your attack by 20\n")
            typing("Sword2 costs 300 gold and increases your attack by 30\n")
            typing("Sword3 costs 400 gold and increases your attack by 40\n")
        # if user doesn't want to know about swords
        elif int(y) == 2:
            typing("Okay then..\n")

        # asking user about which sword that they wants to buy
        typing("Which sword would you like to buy?\n")
        shop_sword = input("1=Sword1, 2=Sword2, 3=Sword3\n")

        # checking for incorredct inputs for shop_sword
        while int(shop_sword) != 1 and int(shop_sword) != 2 and int(shop_sword) != 3:
            typing("Invalid Input. Try again\n")
            shop_sword = input("1=Sword1, 2=Sword2, 3=Sword3\n")
            if shop_sword == 1 or shop_sword == 2 or shop_sword == 3:
                break
            else:
                pass

                # If user wants sword1
        if int(shop_sword) == 1:
            # If user already has sword1
            if sword1 == True:
                typing("You are already carrying Sword1\n")
            # If user doesn't have enough gold.
            elif gold < 200:
                typing("You don't have enough gold.\n")
                print(f"You own {gold} gold.\n")
            # Purchasing sword1 and completing the transaction.
            elif sword1 == False:
                sword1 = True
                sword2 = False
                sword3 = False
                gold = gold - 200
                typing("You now have Sword1\n")
                print(f"You are left with {gold} gold left\n")
                typing("Let's continue shopping...\n")
                shopping()

        # If user wants to buy sword2
        elif int(shop_sword) == 2:
            # If user already has sword2
            if sword2 == True:
                typing("You are already carrying Sword2")
            # If user doesn't have enough gold.
            elif gold < 300:
                typing("You don't have enough gold..")
                print(f"You own {gold} gold.")
            # Purchasing sword2 and completing the transaction.
            elif sword2 == False:
                sword1 = False
                sword2 = True
                sword3 = False
                gold = gold - 300
                typing("You now have Sword2.")
                print(f"You are left with {gold} gold.")
                typing("Let's continue shopping.")
                shopping()

        # If user wants to buy sword3
        elif int(shop_sword) == 3:
            # If user already has sword3
            if sword3 == True:
                typing("You are already carrying Sword3")
            # If user doesn't have enough gold for sword3
            elif gold < 400:
                typing("You don't have enough gold.")
                print(f"You own {gold} gold.")
            # Purchasing sword3 and completing the transaction
            elif sword3 == False:
                sword1 = False
                sword2 = False
                sword3 = True
                gold = gold - 400
                typing("You now have Sword3")
                print(f"You are left with {gold} gold.")
                typing("Let's continue shopping..")
                shopping()

    # If user wants to buy armors
    if int(store1) == 3:
        # Checking what Armor does the user currently has..
        if armor1 == True and armor2 == False and armor3 == False and armor4 == False  and armor5 == False:
            typing("Right now, you have Armor1")
        elif armor1 == False and armor2 == True and armor3 == False and armor4 == False  and armor5 == False:
            typing("Right now you have Armor2")
        elif armor1 == False and armor2 == False and armor3 == True and armor4 == False  and armor5 == False:
            typing("Right now you have Armor3")
        elif armor1 == False and armor2 == False and armor3 == False and armor4 == True  and armor5 == False:
            typing("Right now you have Armor4")
        elif armor1 == False and armor2 == False and armor3 == False and armor4 == False  and armor5 == True:
            typing("Right now you have Armor5")
        
        typing("We have 5 types of armors..")
        typing("Armor1, Armor2, Armor3,Armor4 ,Armor5")
        typing("Would you like to know more about them?")
        x = input("1=Yes or 2=No")

        # for invalid input of x
        while int(x) != 1 and int(x) != 2:
            typing("Invalid input. Try again")
            x = input("1=Yes, 2=No")
            if x == 1 or x == 2:
                break
            else:
                pass

        # If user wants to know about armors
        if int(x) == 1:
            typing("Armor1 costs 100 gold and increases your defense by 10\n")
            typing("Armor2 costs 200 gold and increases your defense by 20\n")
            typing("Armor3 costs 300 gold and increases your defense by 30\n")
            typing("Armor4 costs 400 gold and increases your defense by 40\n")
            typing("Armor4 costs 600 gold and increases your defense by 45\n")

        # if user doesn't want to know about armors
        elif int(x) == 2:
            typing("Okay then..")

        # asking user about which armor that they wants to buy
        typing("Which armor would you like to buy?\n")
        shop_armor = input("1=Armor1, 2=Armor2, 3=Armor3, 4=Armor4, 5=Armor5")

        # checking for incorrect inputs for shop_armor
        while int(shop_armor) != 1 and int(shop_armor) != 2 and int(shop_armor) != 3 and int(shop_armor) != 4 and int(shop_armor) != 5 :
            typing("Invalid Input. Try again")
            shop_armor = input("1=Armor1, 2=Armor2, 3=Armor3, 4=Armor4,5=Armor5")
            if shop_armor == 1 or shop_armor == 2 or shop_armor == 3 or shop_armor == 4 or shop_armor == 5:
                break
            else:
                pass

                # If user wants armor1
        if int(shop_armor) == 1:
            # If user already has armor1
            if armor1 == True:
                typing("You are already carrying Armor1")
            # If user doesn't have enough gold.
            elif gold < 100:
                typing("You don't have enough gold.")
                print(f"You own {gold} gold.")
            # Purchasing armor1 and completing the transaction.
            elif armor1 == False:
                armor1 = True
                armor2 = False
                armor3 = False
                armor4 = False
                armor5 = False
                gold = gold - 100
                typing("You now have Armor1")
                print(f"You are left with {gold} gold left")
                typing("Let's continue shopping...")
                shopping()

        # If user wants to buy armor2
        elif int(shop_armor) == 2:
            # If user already has armor2
            if armor2 == True:
                typing("You are already carrying Armor2")
            # If user doesn't have enough gold.
            elif gold < 200:
                typing("You don't have enough gold..")
                print(f"You own {gold} gold.")
            # Purchasing armor2 and completing the transaction.
            elif armor2 == False:
                armor1 = False
                armor2 = True
                armor3 = False
                armor4 = False
                armor5 = False
                gold = gold - 200
                typing("You now have Armor2.")
                print(f"You are left with {gold} gold.")
                typing("Let's continue shopping.")
                shopping()

        # If user wants to buy Armor3
        elif int(shop_armor) == 3:
            # If user already has sword3
            if armor3 == True:
                typing("You are already carrying Armor3")
            # If user doesn't have enough gold for sword3
            elif gold < 300:
                typing("You don't have enough gold.")
                print(f"You own {gold} gold.")
            # Purchasing armor3 and completing the transaction
            elif armor3 == False:
                armor1 = False
                armor2 = False
                armor3 = True
                armor4 = False
                armor5 = False
                gold = gold - 300
                typing("You now have Armor3")
                print(f"You are left with {gold} gold.")
                typing("Let's continue shopping..")
                shopping()

        elif int(shop_armor) == 4:
            # If user already has sword4
            if armor4 == True:
                typing("You are already carrying Armor4")
            # If user doesn't have enough gold for sword3
            elif gold < 400:
                typing("You don't have enough gold.")
                print(f"You own {gold} gold.")
            # Purchasing armor3 and completing the transaction
            elif armor4 == False:
                armor1 = False
                armor2 = False
                armor3 = False
                armor4 = True
                armor5 = False
                gold = gold - 400
                typing("You now have Armor4")
                print(f"You are left with {gold} gold.")
                typing("Let's continue shopping..")
                shopping()

        elif int(shop_armor) == 5:
            # If user already has sword5
            if armor5 == True:
                typing("You are already carrying Armor3")
            # If user doesn't have enough gold for sword3
            elif gold < 600:
                typing("You don't have enough gold.")
                print(f"You own {gold} gold.")
            # Purchasing armor3 and completing the transaction
            elif armor5 == False:
                armor1 = False
                armor2 = False
                armor3 = False
                armor4 = False
                armor5 = True
                gold = gold - 600
                typing("You now have Armor5")
                print(f"You are left with {gold} gold.")
                typing("Let's continue shopping..")
                shopping()

    # If user wants to exit the store.
    if int(store1) == 4:
        typing("Leaving the store..")


n = 0
while n != 8:
    inside_room = random.choice(room)

    # if user has to face a monster
    if hp == 0:
        break
    elif inside_room == "monster":
        typing("You have to face a monster...\n")
        monsters = ("m1", "m2", "m3", "m4", "m5", "m6","m7","m8")
        monster = random.choice(monsters)

        if monster == "m1":
            m = 1
            # monster 1
            # Attack in range of 0-10
            typing("You have to face monster 1\n")
            opp_att = random.randint(0, 10)
            fight()
            potion_time()

        if monster == "m2":
            m = 2
            # monster 2
            # Attack in range of 10-20
            typing("You have to face monster 2\n")
            opp_att = random.randint(10, 20)
            fight()
            potion_time()

        if monster == "m3":
            m = 3
            # monster 3
            # Attack in range of 20-30
            typing("You have to face monster 3\n")
            opp_att = random.randint(20, 30)
            fight()
            potion_time()

        if monster == "m4":
            m = 4
            # monster 4
            # Attack in range of 30-40
            typing("You have to face monster 4\n")
            opp_att = random.randint(30, 40)
            fight()
            potion_time()

        if monster == "m5":
            m = 5
            # monster 5
            # Attack in range of 40-50
            typing("You have to face monster 5\n")
            opp_att = random.randint(40, 50)
            fight()
            potion_time()

        if monster == "m6":
            m = 6
            # monster 6
            # Attack in range of 50-60
            typing("You have to face monster 6\n")
            opp_att = random.randint(50, 60)
            fight()
            potion_time()

        if monster == "m7":
            m = 7
            # monster 6
            # Attack in range of 30-40
            typing("You have to face monster 7\n")
            opp_att = random.randint(30, 40)
            fight()
            potion_time()
        
        if monster == "m8":
            m = 8
            # monster 8
            # Attack in range of 60-70
            typing("You have to face monster 8\n")
            opp_att = random.randint(60, 70)
            fight()
            potion_time()

        n = n + 1

    # if user gets a treasure box
    if hp == 0:
        break
    elif inside_room == "treasure box":
        typing("You got a treasure box\n")

        prize = random.randint(2, 7)
        gold = gold + (prize * 100)

        typing(f"You now have {gold} gold\n")
        n = n + 1

    # if user encounters a shop
    if hp == 0:
        break
    elif inside_room == "shop":
        typing("You reached a shop..\n")
        typing(f"You have {gold} gold with you. Would you like to the enter the shop?\n")

        s = ''

        # for incorrect inputs
        while s != "YES" or s != "NO" or s != "yes" or s != "no" or s != "Yes" or s != "No":
            s = input("Yes or No?")
            if s == "YES" or s == "Yes" or s == "yes" or s == "NO" or s == "no" or s == "No":
                break
            else:
                pass
            typing("Incorrect input.Try again\n")

        # whether player wants to enter the shop or not...
        if s == "YES" or s == "Yes" or s == "yes":
            typing("Entering the shop..\n")
            shopping()
        elif s == "NO" or s == "no" or s == "No":
            typing("Leaving the store..\n")
        n = n + 1

# If lose anytime in between the game.
if hp == 0:
    typing("You lose. Better luck next time....\n")

# Boss round
elif hp != 0:
    typing("You have entered room 15\n")
    typing("You have to face the boss now..\n")
    extra_hp = 100
    fight()
    # If user loses the boss round
    if hp == 0:
        result = "lose"
        typing(f"You have {result} the game...\n")
    # If user wins the boss round
    elif hp != 0:
        result = "won"
        typing(f"You have {result} the game..\n")
    # Displaying the result
    if result == "won":
        typing("All the treasure is yours..\n")
    elif result == "lose":
        typing("Unfortunately you couldn't make it to the treasure...\n")

# root = Tk()
# next_button = Button(root, text='Next')
#
# root.mainloop()