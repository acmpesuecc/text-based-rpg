# Defining a function named typing.
# from dbm import whichdb
# from shutil import which
import time, sys
from tkinter import *
import random


def typing(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


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
Diamond_Armour = False
Mythril_Armour = False  # decreases opp_att by 20
Orichalium_Armour = False  # decereases opp_att by 30
potion = 1  # increases hp by 30. Cost=300 gold
ultra_potion = 1  # increases hp by 50. Cost=600 gold
medium_potion = 1  # increases hp by 40. cost=450 gold
which_potion = 0  # variable that lets you select the potion that you want to take.
sword1 = 0
sword2 = 0
sword3 = 0


def fight():
    global opp_hp
    global potion
    global ultra_potion
    global extra_hp
    opp_hp = int(100 + extra_hp)
    typing("The match starts. You get the first chance\n")
    global hp
    while hp > 0 or opp_hp > 0:
        typing("Would you like to attack or use potion??\n")
        d = int(float(input("1=Attack, 2=Use potions\n")))
        # for invalid inputs of d
        while 1 != d != 2 :
            typing("Invalid input. Try again.\n")
            d = int(input("1=Attack, 2=Use potion\n"))
            if d in (2, 1): break

        if d - 1: # If user decides to attack
            typing("Which potion would you like to drink?\n")
            which_potion = input("1=Potion, 2=Ultra Potion, 3=Medium Potion\n")

            # for invalid inputs of which_potion
            while which_potion != "1" and which_potion != "2" and which_potion != "3":
                typing("Invalid input. Try again..")
                which_potion = input("1=Potion, 2=Ultra Potion, 3=Medium Potion")

            if hp == 100: continue
            match int(which_potion):
                case "1":
                    if potion > 0:
                        hp = min(hp+30,100)
                        potion -= 1
                    else: typing("You don't have a potion with you.\n")
                case "2":
                    if ultra_potion > 0: min(hp+50,100)
                    elif ultra_potion == 0: typing("You don't have a ultra potion.\n")
                case "3":
                    if medium_potion > 0: min(hp+40,100)
                    elif not medium_potion: typing("You don't have a medium potion with you.\n")
                case _: typing("Invalid input. You lose your chance.\n")
            typing(f"Your HP={hp}\n")
        else: # If user decided to use potion
            userattack = random.randint(40, 70)
            typing("You will do the attack now\n")
            opp_hp = opp_hp - userattack
            if Iron_Sword: opp_hp = max(0, opp_hp - 20)
            elif Mythril_Sword: max(0, opp_hp - 30)
            elif Orichalium_Sword: max(0, opp_hp - 40)
            if opp_hp > 0: typing(f"Monster's HP={opp_hp}\n")
            elif opp_hp <= 0: typing(f"Monster's HP={(opp_hp:=0)}\n")

        # Monster's turn to attack
        if opp_hp <= 0: continue
        elif opp_hp != 0:
            typing("Now monster will take it's turn.\n")
            opp_attack = random.randint((m - 1) * 10, m * 10)
            hp = max(hp - opp_attack,0)
            if Orichalium_Armour: hp += 30
            elif Mythril_Armour: hp += 20
            elif Iron_Armour: hp += 10
            print(f"Your HP={hp}\n")


def potion_time():
    global hp
    global potion, ultra_potion, medium_potion
    typing("You have some time to rest.\n")
    typing("Would you like to use a potion?\n")
    a = input("1=Yes, 2=No\n")

    # If invalid input for whether user wants a potion or not
    while int(a) != 2 and int(a) != 1:
        typing("Invalid input. Try again.\n")
        a = input("1=Yes, 2=No\n")
        if int(a) in (2,1): break

            # If user wants to utilize potion break
    if int(a) == 1:
        typing("Which potion would you like to take?\n")
        potion_chosen = int(input("1=Potion, 2=Ultra Potion, 3=Medium Potion\n"))

        # If invalid input for potion chosen
        while potion_chosen not in (1,2,3):
            typing("Invalid input. Try again.\n")
            potion_chosen = int(input("1=Potion, 2=Ultra Potion, 3=Medium Potion\n"))

        # If user decides to take potion
        match int(potion_chosen):
            case 1:
                # If user's HP is already 100
                if hp == 100: typing("Your HP is already 100\n")
                elif potion > 0:
                    typing(f"Your HP={(hp:=min(hp + 30,100))}\n")
                    typing(f"You now have {(potion:=potion - 1)} Potions left\n")
                elif not potion: typing("You dont have any potions with you.")
            # If user decides to take ultra potion
            case 2:
                # If user's HP is already 100
                if hp == 100: typing("Your HP is already 100\n")
                elif ultra_potion > 0:
                    typing(f"Your HP={(hp:=min(hp + 50,100))}\n")
                    typing(f"You now have {(ultra_potion:=ultra_potion-1)} Ultra Potions left\n")
                elif not ultra_potion: typing("You don't have any ultra potions left with you.")
            case 3:
                # If user's HP is already 100
                if hp == 100: typing("Your HP is already 100\n")
                elif medium_potion > 0:
                    typing(f"Your HP={(hp:=min(hp+40,100))}\n")
                    typing(f"You now have {(medium_potion:=medium_potion-1)} Medium Potions left\n")
                elif not medium_potion: typing("You don't have any medium potions left with you.")
        potion_time()
    # If user decides not to take any potion..


def shopping():
    global gold
    global Iron_Sword, Mythril_Sword, Orichalium_Sword
    global Iron_Armour, Mythril_Armour, Orichalium_Armour
    global potion, ultra_potion, medium_potion
    print("")
    typing("Welcome to the store..\n")
    typing("What would you like to buy?\n")
    # store1 variable to ask user what necessity do they need to buy
    store1 = input("1=Potion, 2=Sword, 3=Armor, 4=Exit Store\n")

    # if invalid input..
    while int(store1) != 1 and int(store1) != 2 and int(store1) != 3 and int(store1) != 4:
        typing("Invalid Input. Try again\n")
        store1 = input("1=Potion, 2=Sword, 3=Armor, 4=Exit Store\n")
        if int(store1) in (1,2,3,4): break

    # If user wants to buy potions
    if int(store1) == 1:
        print(f"You currently have {potion} Small potions,"
              f" {ultra_potion} Ultra potions and {medium_potion} Medium potions with you.\n")
        typing("We have 3 types of potion.\n")
        typing("Small Potion, Ultra Potion and Medium Potion\n")
        typing("Would you like to know more about them?\n")
        z = int(input("1=Yes, 2=No\n"))

        # if invalid input of z
        while z not in (1,2):
            typing("Invalid input. Try again")
            z = int(input("1=Yes, 2=No"))

        if z - 1: typing("Okay then..")  # if user doesn't need to know about potions
        else:  # if user wants to know about potions
            typing("Small potion that costs 250 gold will increase your HP by 30")
            typing("And..")
            typing("Ultra potion that costs 600 gold will increase your HP by 50")
            typing("And..")
            typing("Medium potion that costs 450 gold will increase your HP by 40")

        typing("Which potion would you like to buy?")
        shop_potion = int(input("1=Small Potion, 2=Ultra Potion, 3=Medium Potion"))

        # for invalid inputs of shop potion
        while shop_potion not in (1,2,3):
            typing("Invalid input. Try again")
            shop_potion = int(input("1=Small Potion, 2=Ultra Potion, 3=Medium potion"))

        # If user wantes to buy small potion
        match shop_potion:
            case 1:
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
                    print(f"You now have {(gold:=gold - (250 * no_of_small_potions))} gold with you")
                    print(f"You now have {(potion:=potion + no_of_small_potions)} Small Potions with you")
                    typing("Let's continue shopping..")
                    shopping()
            # If user wants to buy Ultra Potion
            case 2:
                typing("How many Ultra Potions would you like to buy?\n")
                typing("Cost=600 gold\n")
                no_of_ultra_potions = int(input(""))
                if gold - (no_of_ultra_potions * 600) < 0:
                    typing("You don't have enough gold.")
                    typing("Let's shop for something else.")
                    shopping()
                else:
                    print(f"You now have {(gold:=gold - (600 * no_of_ultra_potions))} gold with you")
                    print(f"You now have {(ultra_potion:=ultra_potion + no_of_ultra_potions)} Ultra Potions with you")
                    typing("Let's continue shopping..")
                    shopping()
            #if user wants to buy medium potion
            case 3:
                typing("How many Medium Potions would you like to buy?\n")
                typing("Cost=450 gold\n")
                no_of_medium_potions = int(input(""))
                if gold - (no_of_medium_potions * 450) < 0:
                    typing("You don't have enough gold.")
                    typing("Let's shop for something else.")
                    shopping()
                else:
                    print(f"You now have {(gold:=gold - (450 * no_of_medium_potions))} gold with you")
                    print(f"You now have {(medium_potion:=medium_potion + no_of_medium_potions)} Medium Potions with you")
                    typing("Let's continue shopping..")
                    shopping()


    # If user wants to buy swords
    if int(store1) == 2:
        # Checking what sword does the user currently has..
        if sword1 and not sword2 and not sword3:typing("Right now, you have Sword1")
        elif not sword1 and sword2 and not sword3:typing("Right now you have Sword2")
        elif not sword1 and not sword2 and sword3:typing("Right now you have Sword3")
        typing("We have 3 types of swords..\n")
        typing("Sword1, Sword2, Sword3")
        typing("Would you like to know more about them?\n")


        # for invalid input of y
        while (y := int(input("1=Yes or 2=No\n"))) not in (1,2):
            typing("Invalid input. Try again\n")

        # If user wants to know about swords
        if y-1: typing("Okay then..\n")
        else:
            typing("Sword1 costs 200 gold and increases your attack by 20\n")
            typing("Sword2 costs 300 gold and increases your attack by 30\n")
            typing("Sword3 costs 400 gold and increases your attack by 40\n")


        # asking user about which sword that they wants to buy
        typing("Which sword would you like to buy?\n")


        # checking for incorredct inputs for shop_sword
        while (shop_sword := int(input("1=Sword1, 2=Sword2, 3=Sword3\n"))) not in (1,2,3):
            typing("Invalid Input. Try again\n")

                # If user wants sword1
        match shop_sword:
            case 1:
                # If user already has sword1
                if sword1: typing("You are already carrying Sword1\n")
                # If user doesn't have enough gold.
                elif gold < 200:
                    typing("You don't have enough gold.\n")
                    print(f"You own {gold} gold.\n")
                # Purchasing sword1 and completing the transaction.
                elif not sword1:
                    sword1 = True
                    sword2 = False
                    sword3 = False
                    typing("You now have Sword1\n")
                    print(f"You are left with {(gold:=gold - 200)} gold left\n")
                    typing("Let's continue shopping...\n")
                    shopping()

            # If user wants to buy sword2
            case 2:
                # If user already has sword2
                if sword2: typing("You are already carrying Sword2")
                # If user doesn't have enough gold.
                elif gold < 300:
                    typing("You don't have enough gold..")
                    print(f"You own {gold} gold.")
                # Purchasing sword2 and completing the transaction.
                else:
                    sword1 = False
                    sword2 = True
                    sword3 = False
                    typing("You now have Sword2.")
                    print(f"You are left with {(gold:=gold - 300)} gold.")
                    typing("Let's continue shopping.")
                    shopping()

            # If user wants to buy sword3
            case 3:
                # If user already has sword3
                if sword3: typing("You are already carrying Sword3")
                # If user doesn't have enough gold for sword3
                elif gold < 400:
                    typing("You don't have enough gold.")
                    print(f"You own {gold} gold.")
                # Purchasing sword3 and completing the transaction
                else:
                    sword1 = False
                    sword2 = False
                    sword3 = True
                    typing("You now have Sword3")
                    print(f"You are left with {(gold:= gold - 400)} gold.")
                    typing("Let's continue shopping..")
                    shopping()

    # If user wants to buy armors
    if int(store1) == 3:
        # Checking what Armor does the user currently has..
        if armor1 and not armor2 and not armor3: typing("Right now, you have Armor1")
        elif not armor1 and armor2 and not armor3: typing("Right now you have Armor2")
        elif not armor1 and not armor2 and armor3: typing("Right now you have Armor3")
        typing("We have 3 types of armors..")
        typing("Armor1, Armor2, Armor3")
        typing("Would you like to know more about them?")

        # for invalid input of x
        while (x := input("1=Yes, 2=No")) not in (1, 2):
            typing("Invalid input. Try again")

        # If user wants to know about armors
        if int(x) - 1: typing("Okay then..")
        else:
            typing("Armor1 costs 100 gold and increases your defense by 10\n")
            typing("Sword2 costs 200 gold and increases your defense by 20\n")
            typing("Sword3 costs 300 gold and increases your defense by 30\n")


        # asking user about which armor that they wants to buy
        typing("Which armor would you like to buy?\n")

        # checking for incorrect inputs for shop_armor
        while (shop_armor := input("1=Armor1, 2=Armor2, 3=Armor3")) not in (1,2,3):
            typing("Invalid Input. Try again")

                # If user wants armor1
        if int(shop_armor) == 1:
            # If user already has armor1
            if armor1: typing("You are already carrying Armor1")
            # If user doesn't have enough gold.
            elif gold < 100:
                typing("You don't have enough gold.")
                print(f"You own {gold} gold.")
            # Purchasing armor1 and completing the transaction.
            elif armor1:
                armor1 = True
                armor2 = False
                armor3 = False
                typing("You now have Armor1")
                print(f"You are left with {(gold:=gold - 100)} gold left")
                typing("Let's continue shopping...")
                shopping()

        # If user wants to buy armor2
        elif int(shop_armor) == 2:
            # If user already has armor2
            if armor2: typing("You are already carrying Armor2")
            # If user doesn't have enough gold.
            elif gold < 200:
                typing("You don't have enough gold..")
                print(f"You own {gold} gold.")
            # Purchasing armor2 and completing the transaction.
            elif armor2:
                armor1 = False
                armor2 = True
                armor3 = False
                typing("You now have Armor2.")
                print(f"You are left with {(gold:= gold - 200)} gold.")
                typing("Let's continue shopping.")
                shopping()

        # If user wants to buy Armor3
        elif int(shop_armor) == 3:
            # If user already has sword3
            if armor3:
                typing("You are already carrying Armor3")
            # If user doesn't have enough gold for sword3
            elif gold < 300:
                typing("You don't have enough gold.")
                print(f"You own {gold} gold.")
            # Purchasing armor3 and completing the transaction
            else:
                armor1 = False
                armor2 = False
                armor3 = True
                typing("You now have Armor3")
                print(f"You are left with {(gold:= gold - 300)} gold.")
                typing("Let's continue shopping..")
                shopping()

    # If user wants to exit the store.
    if int(store1) == 4: typing("Leaving the store..")


n = 0
while n != 10:
    inside_room = random.choice(room)

    # if user has to face a monster
    if not hp: break
    elif inside_room == "monster":
        typing("You have to face a monster...\n")

        monsters = ("m1", "m2", "m3", "m4", "m5", "m6", "m7", "m8","m9","m10","m11","m12")

        monster = random.choice(monsters)
        for i, mnstr in enumerate(monsters):
            if(mnstr == monster):
                m=i+1
                typing(f"You have to face monster {i+1}\n")
                opp_att = random.randint(10*i, 10*m)
                fight()
                potion_time()

        n += 1

    # if user gets a treasure box
    if not hp: break
    elif inside_room == "treasure box":
        typing("You got a treasure box\n")

        prize = random.randint(2, 7)

        typing(f"You now have {(gold:= gold + (prize * 100))} gold\n")
        n += 1

    # if user encounters a shop
    if not hp: break
    elif inside_room == "shop":
        typing("You reached a shop..\n")
        typing(f"You have {gold} gold with you. Would you like to the enter the shop?\n")

        s = ''

        # for incorrect inputs
        while s != "YES" or s != "NO" or s != "yes" or s != "no" or s != "Yes" or s != "No":
            s = input("Yes or No?").lower()
            if s == "yes" or s == "no": break
            typing("Incorrect input.Try again\n")

        # whether player wants to enter the shop or not...
        if s == "yes":
            typing("Entering the shop..\n")
            shopping()
        elif s == "no": typing("Leaving the store..\n")
        n += 1

# If lose anytime in between the game.
if hp == 0: ("You lose. Better luck next time....\n")

# Boss round
elif hp != 0:
    typing("You have entered room 15\n")
    typing("You have to face the boss now..\n")
    extra_hp = 100
    fight()
    # If user loses the boss round
    if hp == 0: typing(f'You have {(result:= "lose")} the game...\n')
    # If user wins the boss round
    elif hp != 0:
        result = "won"
        typing(f"You have {(result:= 'won')} the game..\n")
    # Displaying the result
    if result == "won": typing("All the treasure is yours..\n")
    else: typing("Unfortunately you couldn't make it to the treasure...\n")

# root = Tk()
# next_button = Button(root, text='Next')
#
# root.mainloop()


#...