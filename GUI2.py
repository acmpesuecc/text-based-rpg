from tkinter import *
import sys
import time


import random

monster = ""  # to store the current monster
turn = 1  # to keep track of turns in battle
ability = "" # abikity of the monster
reward = 0  # reward after defeating a monster
gold = 1500  # used in store to buy items
hp = 100  # user's hp
opp_hp = 100  # monster's hp
extra_hp = 0  # extra opponent hp for boss round
Iron_Sword = False  # increases attack by 20
Mythril_Sword = False  # increases attack by 30
Orichalium_Sword = False  # increases attack by 40
Iron_Armour = False  # decreases opp_att by 10
Mythril_Armour = False  # decreases opp_att by 20
Orichalium_Armour = False  # decreases opp_att by 30

BunSamosa_Armour= False #decreases opp_att by 50
ACM_Armour= False #decreases opp_att by 60
Jade_Armour = False # increases hp by 10
Diamond_Armour = False #increases hp by 20
Silver_Armour = False #decreaases Opp_ATT by 40
Gold_Armour= False #decreases opp_att by 70

potion = 1  # increases hp by 30. Cost=300 gold
ultra_potion = 1  # increases hp by 50. Cost=600 gold
medium_potion = 1  # increases hp by 40, cost=450 gold
# variable that lets you select the potion that you want to take.
which_potion = 0
rav = 0  # the current room number

def get_room():
    global rav
    rav += 1
    if (rav % 20 != 0):  # a loop to make sure that the bossmonster doesnt appear until upto 20 iterations in the game
        #room = ("monster", "shop", "treasure box", "monster", "shop")
        #inside_room = random.choice(room)
        # print(inside_room)
        prob_treasure = random.random()
        if prob_treasure > 0.8:
            frame1.destroy()
            treasure_box()
        else:
            prob_mons_shop = random.random()
            if prob_mons_shop > 0.5:
                frame1.destroy()
                get_monster(rav)
            else:
                frame1.destroy()
                shop()

    else:
        frame1.destroy()
        get_bossmonster()

# treasure box room


def treasure_box():
    global gold
    global frame_tb
    frame_tb = Frame(root)
    frame_tb.pack()
    L_TB = Label(frame_tb, text="You found a treasure box\n")
    L_TB.pack()

    prize = random.randint(2, 7)
    gold = gold + (prize * 100)

    L_TB_gold = Label(frame_tb, text=f"You now have {gold} gold\n")
    L_TB_gold.pack()

    B_TB = Button(frame_tb, text="Next", command=lambda: treasure_box_exit())
    B_TB .pack()


def treasure_box_exit():
    frame_tb.destroy()
    get_room()


def shop_Potion():
    global frame_shop_potion
    frame_shop_1.destroy()
    frame_shop_potion = Frame(root)
    frame_shop_potion.pack()
    L_Shop_Potion_1 = Label(frame_shop_potion, text=f"You currently have {potion} Small potions and {ultra_potion} Ultra potions with you.\n"
                                                    f"We have 3 types of potion.\n"
                                                    f"Small Potion, Ultra Potion and Medium potion\n"
                                                    f"Would you like to know more about them?\n")
    L_Shop_Potion_1.pack()
    B_Shop_Potion_Y = Button(
        frame_shop_potion, text="Yes", command=lambda: shop_potion_yes())
    B_Shop_Potion_N = Button(frame_shop_potion, text="No",
                             command=lambda: shop_potion_no())
    B_Shop_Potion_Y.pack(side=BOTTOM)
    B_Shop_Potion_N.pack(side=BOTTOM)


def shop_potion_no():
    global frame_shop_potion_no
    frame_shop_potion.destroy()

    frame_shop_potion_no = Frame(root)
    frame_shop_potion_no.pack()
    L_Shop_Potion_No = Label(frame_shop_potion_no, text="Okay then..\n"
                                                        "Which potion would you like to buy?")
    L_Shop_Potion_No.pack()
    B_Shop_Potion_No_SP = Button(
        frame_shop_potion_no, text="Small Potion", command=lambda: shop_potions_small())
    B_Shop_Potion_No_UP = Button(
        frame_shop_potion_no, text="Ultra Potion", command=lambda: shop_potions_ultra())
    B_Shop_Potion_No_MP = Button(
        frame_shop_potion_no, text="Medium Potion", command=lambda: shop_potions_medium())
    B_Shop_Potion_No_UP.pack()
    B_Shop_Potion_No_SP.pack()
    B_Shop_Potion_No_MP.pack()


def shop_potion_yes():
    global frame_shop_potion_yes
    frame_shop_potion.destroy()
    frame_shop_potion_yes = Frame(root)
    frame_shop_potion_yes.pack()
    L_Shop_Potion_Yes = Label(frame_shop_potion_yes, text="Small potion that costs 250 gold will increase your HP by 30\n"
                                                          "And..\n"
                                                          "Ultra potion that costs 600 gold will increase your HP by 50\n"
                                                          "And..\n"
                                                          "Medium potion that costs 450 gold will increase your HP by 40")
    L_Shop_Potion_Yes.pack()
    B_Shop_Potion_Yes = Button(
        frame_shop_potion_yes, text="Next", command=lambda: shop_potion_yestono())
    B_Shop_Potion_Yes.pack()


def shop_potion_yestono():
    frame_shop_potion_yes.destroy()
    shop_potion_no()


def shop_potions_small():
    global frame_shop_potion_small
    frame_shop_potion_no.destroy()
    frame_shop_potion_small = Frame(root)
    frame_shop_potion_small.pack()
    L_shop_potion_small = Label(frame_shop_potion_small, text="How many Small potions would you like to buy?\n"
                                                              "Cost=250 gold\n"
                                                              f"You have {gold} gold")
    L_shop_potion_small.pack()

    B_shop_potion_small = Button(
        frame_shop_potion_small, text="Buy", command=lambda: shop_potion_small_buy())
    B_shop_potion_small.pack()
    B_shop_potion_small_main = Button(
        frame_shop_potion_small, text="Back", command=lambda: shop_potions_small_to_main())
    B_shop_potion_small_main.pack(side=BOTTOM)


def shop_potions_small_to_main():
    frame_shop_potion_small.destroy()
    shop()


def shop_potion_small_buy():
    global gold
    global potion
    if gold - 250 < 0:
        L_shop_potion_small = Label(frame_shop_potion_small, text="You don't have enough gold.\n"
                                                                  "Let's shop for something else..\n")
        L_shop_potion_small.pack()
        # If user has enough gold
    else:
        potion = potion + 1
        gold = gold - 250
        L_shop_potion_small = Label(frame_shop_potion_small, text=(f"You now have {gold} gold with you\n"
                                                                   f"You now have {potion} Small Potions with you\n"
                                                                   "Let's continue shopping.."))
        L_shop_potion_small.pack()


def shop_potions_ultra():
    global frame_shop_potion_ultra
    frame_shop_potion_no.destroy()
    frame_shop_potion_ultra = Frame(root)
    frame_shop_potion_ultra.pack()
    L_shop_potion_ultra = Label(frame_shop_potion_ultra, text="How many Ultra potions would you like to buy?\n"
                                                              "Cost=600 gold\n"
                                                              f"You have {gold} gold")
    L_shop_potion_ultra.pack()
    B_shop_potion_ultra = Button(
        frame_shop_potion_ultra, text="Buy", command=lambda: shop_potion_ultra_buy())
    B_shop_potion_ultra.pack()
    B_shop_potion_ultra_main = Button(
        frame_shop_potion_ultra, text="Back", command=lambda: shop_potions_ultra_to_main())
    B_shop_potion_ultra_main.pack(side=BOTTOM)


def shop_potions_ultra_to_main():
    frame_shop_potion_ultra.destroy()
    shop()


def shop_potion_ultra_buy():
    global gold
    global ultra_potion
    # global frame_shop_potion_ultra_buy
    # frame_shop_potion_ultra_buy.destroy()
    # frame_shop_potion_ultra_buy = Frame(root)
    # frame_shop_potion_ultra_buy.pack()
    if gold - 600 < 0:
        L_shop_potion_ultra = Label(frame_shop_potion_ultra, text="You don't have enough gold.\n"
                                                                  f"You have {gold} gold with you\n"
                                    f"You have {ultra_potion} Ultra Potions with you\n"
                                    "Let's shop for something else..\n")
        L_shop_potion_ultra.pack()
        # B_shop_potion_ultra_main = Button(frame_shop_potion_ultra, text="Back")
        # B_shop_potion_ultra_main.pack()
        # If user has enough gold
    else:
        ultra_potion = ultra_potion + 1
        gold = gold - 600
        L_shop_potion_ultra = Label(frame_shop_potion_ultra, text=(f"You now have {gold} gold with you\n"
                                                                   f"You now have {ultra_potion} Ultra Potions with you\n"
                                                                   "Let's continue shopping.."))
        L_shop_potion_ultra.pack()


def shop_potions_medium():
    global frame_shop_potion_medium
    frame_shop_potion_no.destroy()
    frame_shop_potion_medium = Frame(root)
    frame_shop_potion_medium.pack()
    L_shop_potion_medium = Label(frame_shop_potion_medium, text="How many Medium potions would you like to buy?\n"
                                 "Cost=450 gold\n"
                                 f"You have {gold} gold")
    L_shop_potion_medium.pack()
    B_shop_potion_medium = Button(
        frame_shop_potion_medium, text="Buy", command=lambda: shop_potion_medium_buy())
    B_shop_potion_medium.pack()
    B_shop_potion_medium_main = Button(
        frame_shop_potion_medium, text="Back", command=lambda: shop_potions_medium_to_main())
    B_shop_potion_medium_main.pack(side=BOTTOM)


def shop_potions_medium_to_main():
    frame_shop_potion_medium.destroy()
    shop()


def shop_potion_medium_buy():
    global gold
    global medium_potion
    # global frame_shop_potion_ultra_buy
    # frame_shop_potion_ultra_buy.destroy()
    # frame_shop_potion_ultra_buy = Frame(root)
    # frame_shop_potion_ultra_buy.pack()
    if gold - 450 < 0:
        L_shop_potion_medium = Label(frame_shop_potion_medium, text="You don't have enough gold.\n"
                                     f"You have {gold} gold with you\n"
                                     f"You have {medium_potion} Medium Potions with you\n"
                                     "Let's shop for something else..\n")
        L_shop_potion_medium.pack()
        # B_shop_potion_ultra_main = Button(frame_shop_potion_ultra, text="Back")
        # B_shop_potion_ultra_main.pack()
        # If user has enough gold
    else:
        medium_potion = medium_potion + 1
        gold = gold - 450
        L_shop_potion_medium = Label(frame_shop_potion_medium, text=(f"You now have {gold} gold with you\n"
                                                                     f"You now have {medium_potion} Medium Potions with you\n"
                                                                     "Let's continue shopping.."))
        L_shop_potion_medium.pack()


def shop_sword():
    global frame_shop_sword
    global Iron_Sword
    global Mythril_Sword
    global Orichalium_Sword
    frame_shop_1.destroy()
    frame_shop_sword = Frame(root)
    frame_shop_sword.pack()
    if Iron_Sword:
        L_Shop_Sword_owned = Label(
            frame_shop_sword, text="Right now, you have Iron_Sword")
        L_Shop_Sword_owned.pack()
    elif Mythril_Sword:
        L_Shop_Sword_owned = Label(
            frame_shop_sword, text="Right now you have Mythril_Sword ")
        L_Shop_Sword_owned.pack()
    elif Orichalium_Sword:
        L_Shop_Sword_owned = Label(
            frame_shop_sword, text="Right now you have Orichalium_Sword")
        L_Shop_Sword_owned.pack()
    L_Shop_Sword_intro = Label(frame_shop_sword, text="We have 3 types of swords..\n"
                                                      "Iron_Sword, Mythril_Sword and Orichalium_Sword\n"
                                                      "Would you like to know more about them?\n")
    L_Shop_Sword_intro.pack()
    B_Shop_Sword_Y = Button(frame_shop_sword, text="Yes",
                            command=lambda: shop_sword_yes())
    B_Shop_Sword_N = Button(frame_shop_sword, text="No",
                            command=lambda: shop_sword_no())
    B_Shop_Sword_Y.pack()
    B_Shop_Sword_N.pack()


def shop_sword_yes():
    global frame_shop_sword_yes
    frame_shop_sword.destroy()
    frame_shop_sword_yes = Frame(root)
    frame_shop_sword_yes.pack()
    L_Shop_Sword_Y_info = Label(frame_shop_sword_yes, text="Iron_Sword costs 200 gold and increases your attack by 20\n"
                                "Mythril_Sword costs 300 gold and increases your attack by 30\n"
                                "Orichalium_Sword costs 400 gold and increases your attack by 40\n")
    L_Shop_Sword_Y_info.pack()

    B_Shop_Sword_Yes = Button(
        frame_shop_sword_yes, text="Next", command=lambda: shop_sword_yestono())
    B_Shop_Sword_Yes.pack()


def shop_sword_yestono():
    frame_shop_sword_yes.destroy()
    shop_sword_no()


def shop_sword_no():
    global frame_shop_swords_no
    frame_shop_sword.destroy()
    frame_shop_swords_no = Frame(root)
    frame_shop_swords_no.pack()
    L_Shop_Swords_N = Label(frame_shop_swords_no,
                            text="Which sword would you like to buy?\n")
    L_Shop_Swords_N.pack()
    B_Shop_Swords_Sword1 = Button(
        frame_shop_swords_no, text="Iron_Sword", command=lambda: shop_sword_sword1())
    B_Shop_Swords_Sword1.pack()
    B_Shop_Swords_Sword2 = Button(
        frame_shop_swords_no, text="Mythril_Sword", command=lambda: shop_sword_sword2())
    B_Shop_Swords_Sword2.pack()
    B_Shop_Swords_Sword3 = Button(
        frame_shop_swords_no, text="Orichalium_Sword", command=lambda: shop_sword_sword3())
    B_Shop_Swords_Sword3.pack()
    B_Shop_Swords_back = Button(
        frame_shop_swords_no, text="back", command=lambda: shop_sword_to_main())
    B_Shop_Swords_back.pack(side=BOTTOM)


def shop_sword_sword1():
    global Iron_Sword
    global Mythril_Sword
    global Orichalium_Sword
    global gold
    if Iron_Sword == False:
        if gold > 200:
            gold = gold - 200
            L_shop_swords_sword1 = Label(frame_shop_swords_no, text="You now have Iron_Sword\n"
                                                                    f"You now have {gold} gold")
            L_shop_swords_sword1.pack()
            Iron_Sword = True
            Mythril_Sword = False
            Orichalium_Sword = False

        else:
            L_shop_swords_sword1 = Label(frame_shop_swords_no, text="You don't have enough gold.\n"
                                                                    f"You have {gold} gold")
            L_shop_swords_sword1.pack()
    else:
        L_shop_swords_sword1 = Label(
            frame_shop_swords_no, text="You already have Iron_Sword")
        L_shop_swords_sword1.pack()


def shop_sword_sword2():
    global Iron_Sword
    global Mythril_Sword
    global Orichalium_Sword
    global gold
    if Mythril_Sword == False:
        if gold > 300:
            gold = gold - 300
            L_shop_swords_sword2 = Label(frame_shop_swords_no, text="You now have Mythril_Sword\n"
                                                                    f"You now have {gold} gold")
            L_shop_swords_sword2.pack()
            Iron_Sword = False
            Mythril_Sword = True
            Orichalium_Sword = False

        else:
            L_shop_swords_sword2 = Label(frame_shop_swords_no, text="You don't have enough gold.\n"
                                                                    f"You have {gold} gold")
            L_shop_swords_sword2.pack()
    else:
        L_shop_swords_sword2 = Label(
            frame_shop_swords_no, text="You already have Mythril_Sword")
        L_shop_swords_sword2.pack()


def shop_sword_sword3():
    global Iron_Sword
    global Mythril_Sword
    global Orichalium_Sword
    global gold
    if Orichalium_Sword == False:
        if gold > 400:
            gold = gold - 400
            L_shop_swords_sword3 = Label(frame_shop_swords_no, text="You now have Orichalium_Sword\n"
                                                                    f"You now have {gold} gold")
            L_shop_swords_sword3.pack()
            Iron_Sword = False
            Mythril_Sword = False
            Orichalium_Sword = True

        else:
            L_shop_swords_sword3 = Label(frame_shop_swords_no, text="You don't have enough gold.\n"
                                                                    f"You have {gold} gold")
            L_shop_swords_sword3.pack()
    else:
        L_shop_swords_sword3 = Label(
            frame_shop_swords_no, text="You already have Orichalium_Sword")
        L_shop_swords_sword3.pack()


def shop_sword_to_main():
    frame_shop_swords_no.destroy()
    shop()


def shop_armor():
    global frame_shop_armor
    global Iron_Armour
    global Mythril_Armour
    global Orichalium_Armour
    global BunSamosa_Armour
    global ACM_Armour
    global Silver_Armour
    global Gold_Armour
    frame_shop_1.destroy()
    frame_shop_armor = Frame(root)
    frame_shop_armor.pack()
    if Iron_Armour:
        L_Shop_armor_owned = Label(
            frame_shop_armor, text="Right now, you have Iron_Armour")
        L_Shop_armor_owned.pack()
    elif Mythril_Armour:
        L_Shop_armor_owned = Label(
            frame_shop_armor, text="Right now you have Mythril_Armour")
        L_Shop_armor_owned.pack()
    elif BunSamosa_Armour:
        L_Shop_armor_owned = Label(
            frame_shop_armor, text="Right now you have BunSamosa_Armour")
        L_Shop_armor_owned.pack()
    elif ACM_Armour:
        L_Shop_armor_owned = Label(
            frame_shop_armor, text="Right now you have ACM_Armour")
        L_Shop_armor_owned.pack()
    elif Orichalium_Armour:
        L_Shop_armor_owned = Label(
            frame_shop_armor, text="Right now you have Orichalium_Armour")
        L_Shop_armor_owned.pack()
    elif Gold_Armour:
        L_Shop_armor_owned = Label(frame_shop_armor, text="Right now you have Gold_Armour")
        L_Shop_armor_owned.pack()
    elif Silver_Armour:
        L_Shop_armor_owned = Label(frame_shop_armor, text="Right now you have Silver_Armour")
        L_Shop_armor_owned.pack()
    L_Shop_armor_intro = Label(frame_shop_armor, text="We have 7 types of armors..\n"
                                                      "Iron_Armour, Mythril_Armour, Orichalium_Armour, BunSamosa_Armour Silver_Armour, Gold_Armour and ACM_Armour\n"
                                                      "Would you like to know more about them?\n")
    L_Shop_armor_intro.pack()
    B_Shop_armor_Y = Button(frame_shop_armor, text="Yes",
                            command=lambda: shop_armor_yes())
    B_Shop_armor_N = Button(frame_shop_armor, text="No",
                            command=lambda: shop_armor_no())
    B_Shop_armor_Y.pack()
    B_Shop_armor_N.pack()


def shop_armor_yes():
    global frame_shop_armor_yes
    frame_shop_armor.destroy()
    frame_shop_armor_yes = Frame(root)
    frame_shop_armor_yes.pack()
    L_Shop_armor_Y_info = Label(frame_shop_armor_yes, text="Iron_Armour costs 200 gold and increases your attack by 20\n"

                                                            "Mythril_Armour costs 300 gold and increases your attack by 30\n"
                                                            "Orichalium_Armour costs 400 gold and increases your attack by 40\n"
                                                            "Jade_Armour costs 250 gold and increases your hp by 10\n"
                                                            "Diamond_Armour costs 350 gold and increases your hp by 20\n"
                                                            "BunSamosa_Armour costs 500 gold and increases your attack by 50\n"
                                                            "ACM_Armour costs 600 gold and increases your attack by 60\n"
                                                            "silver_Armour costs 550 gold and increases your attack by 65\n"
                                                            "Gold_Armour costs 700 gold and increases your attack by 70\n")
         

    L_Shop_armor_Y_info.pack()

    B_Shop_armor_Yes = Button(
        frame_shop_armor_yes, text="Next", command=lambda: shop_armor_yestono())
    B_Shop_armor_Yes.pack()


def shop_armor_yestono():
    frame_shop_armor_yes.destroy()
    shop_armor_no()


def shop_armor_no():
    global frame_shop_armors_no
    frame_shop_armor.destroy()
    frame_shop_armors_no = Frame(root)
    frame_shop_armors_no.pack()
    L_Shop_armors_N = Label(frame_shop_armors_no,
                            text="Which armor would you like to buy?\n")
    L_Shop_armors_N.pack()
    B_Shop_armors_armor1 = Button(
        frame_shop_armors_no, text="Iron_Armour", command=lambda: shop_armor_armor1())
    B_Shop_armors_armor1.pack()
    B_Shop_armors_armor2 = Button(
        frame_shop_armors_no, text="Mythril_Armour", command=lambda: shop_armor_armor2())
    B_Shop_armors_armor2.pack()
    B_Shop_armors_armor3 = Button(
        frame_shop_armors_no, text="Orichalium_Armour", command=lambda: shop_armor_armor3())
    B_Shop_armors_armor3.pack()

    B_Shop_armors_armor4 = Button(frame_shop_armors_no, text="Jade_Armour", command=lambda: shop_armor_armor4())
    B_Shop_armors_armor4.pack()
    B_Shop_armors_armor5 = Button(frame_shop_armors_no, text="Diamond_Armour", command=lambda: shop_armor_armor5())
    B_Shop_armors_armor5.pack()    
    B_Shop_armors_armor6= Button(frame_shop_armors_no, text="BunSamosa_Armour", command=lambda: shop_armor_armor6())
    B_Shop_armors_armor6.pack()
    B_Shop_armors_armor7 = Button(frame_shop_armors_no, text="ACM_Armour", command=lambda: shop_armor_armor7())
    B_Shop_armors_armor7.pack()
    B_Shop_armors_armor8 = Button(frame_shop_armors_no, text="Silver_Armour", command=lambda: shop_armor_armor8())
    B_Shop_armors_armor8.pack()
    B_Shop_armors_armor9 = Button(frame_shop_armors_no, text="Gold_Armour", command=lambda: shop_armor_armor9())
    B_Shop_armors_armor9.pack()
    B_Shop_armors_back = Button(frame_shop_armors_no, text="back", command=lambda: shop_armor_to_main())

    B_Shop_armors_back.pack(side=BOTTOM)


def shop_armor_armor1():
    global Iron_Armour
    global Mythril_Armour
    global Orichalium_Armour
    global gold
    global Jade_Armour
    global Diamond_Armour
    global BunSamosa_Armour
    global ACM_Armour
    global Silver_Armour
    global Gold_Armour
    if Iron_Armour == False:
        if gold > 200:
            gold = gold - 200
            L_shop_armors_armor1 = Label(frame_shop_armors_no, text="You now have Iron_Armour\n"
                                                                    f"You now have {gold} gold")
            L_shop_armors_armor1.pack()
            Iron_Armour = True
            Mythril_Armour = False
            Orichalium_Armour = False
            Jade_Armour = False
            Diamond_Armour = False
            ACM_Armour = False
            BunSamosa_Armour = False
            Gold_Armour=False
            Silver_Armour =False

        else:
            L_shop_armors_armor1 = Label(frame_shop_armors_no, text="You don't have enough gold.\n"
                                                                    f"You have {gold} gold")
            L_shop_armors_armor1.pack()
    else:
        L_shop_armors_armor1 = Label(
            frame_shop_armors_no, text="You already have Iron_Armour")
        L_shop_armors_armor1.pack()


def shop_armor_armor2():
    global Iron_Armour
    global Mythril_Armour
    global Orichalium_Armour
    global gold
    global Jade_Armour
    global Diamond_Armour
    global BunSamosa_Armour
    global ACM_Armour
    global Silver_Armour
    global Gold_Armour
    if Mythril_Armour == False:
        if gold > 300:
            gold = gold - 300
            L_shop_armors_armor2 = Label(frame_shop_armors_no, text="You now have Mythril_Armour\n"f"You now have {gold} gold")
            L_shop_armors_armor2.pack()
            Iron_Armour = False
            Mythril_Armour = True
            Orichalium_Armour = False
            Jade_Armour = False
            Diamond_Armour = False
            ACM_Armour = False
            BunSamosa_Armour = False
            Gold_Armour=False
            Silver_Armour =False

        else:
            L_shop_armors_armor2 = Label(frame_shop_armors_no, text="You don't have enough gold.\n"
                                                                    f"You have {gold} gold")
            L_shop_armors_armor2.pack()
    else:
        L_shop_armors_armor2 = Label(
            frame_shop_armors_no, text="You already have Mythril_Armour")
        L_shop_armors_armor2.pack()


def shop_armor_armor3():
    global Iron_Armour
    global Mythril_Armour
    global Orichalium_Armour
    global gold
    global Jade_Armour
    global Diamond_Armour
    global BunSamosa_Armour
    global ACM_Armour
    global Silver_Armour
    global Gold_Armour
    if Orichalium_Armour == False:
        if gold > 400:
            gold = gold - 400
            L_shop_armors_armor3 = Label(frame_shop_armors_no, text="You now have Orichalium_Armour\n"
                                                                    f"You now have {gold} gold")
            L_shop_armors_armor3.pack()
            Iron_Armour = False
            Mythril_Armour = False
            Orichalium_Armour = True
            Jade_Armour = False
            Diamond_Armour = False
            ACM_Armour = False
            BunSamosa_Armour = False
            Gold_Armour=False
            Silver_Armour =False

        else:
            L_shop_armors_armor3 = Label(frame_shop_armors_no, text="You don't have enough gold.\n"
                                                                    f"You have {gold} gold")
            L_shop_armors_armor3.pack()
    else:
        L_shop_armors_armor3 = Label(
            frame_shop_armors_no, text="You already have Orichalium_Armour")
        L_shop_armors_armor3.pack()


def shop_armor_armor4():
    global Iron_Armour
    global Mythril_Armour
    global Orichalium_Armour
    global gold
    global Jade_Armour
    global Diamond_Armour
    global BunSamosa_Armour
    global ACM_Armour

    global Silver_Armour
    global Gold_Armour
    if Jade_Armour == False:
        if gold > 250:
            gold = gold - 250
            L_shop_armors_armor4 = Label(frame_shop_armors_no, text="You now have Jade_Armour\n"

                                                                    f"You now have {gold} gold")
            L_shop_armors_armor4.pack()
            Iron_Armour = False
            Mythril_Armour = False
            Orichalium_Armour = False
            Jade_Armour = True
            Diamond_Armour = False
            ACM_Armour = False
            BunSamosa_Armour = False
            Gold_Armour=False
            Silver_Armour =False

        else:
            L_shop_armors_armor4 = Label(frame_shop_armors_no, text="You don't have enough gold.\n"
                                                                    f"You have {gold} gold")
            L_shop_armors_armor4.pack()
    else:

        L_shop_armors_armor4 = Label(frame_shop_armors_no, text="You already have Jade_Armour")
        L_shop_armors_armor4.pack()
        

def shop_armor_armor5():
    global Iron_Armour
    global Mythril_Armour
    global Orichalium_Armour
    global gold
    global Jade_Armour
    global Diamond_Armour
    global BunSamosa_Armour
    global ACM_Armour

    global Silver_Armour
    global Gold_Armour
    if Diamond_Armour == False:
        if gold > 350:
            gold = gold - 350
            L_shop_armors_armor5 = Label(frame_shop_armors_no, text="You now have Diamond_Armour\n"

                                                                    f"You now have {gold} gold")
            L_shop_armors_armor5.pack()
            Iron_Armour = False
            Mythril_Armour = False
            Orichalium_Armour = False
            Jade_Armour = False
            Diamond_Armour = True
            ACM_Armour = False
            BunSamosa_Armour = False
            Gold_Armour=False
            Silver_Armour =False

        else:
            L_shop_armors_armor5 = Label(frame_shop_armors_no, text="You don't have enough gold.\n"
                                                                    f"You have {gold} gold")
            L_shop_armors_armor5.pack()
    else:

        L_shop_armors_armor5 = Label(frame_shop_armors_no, text="You already have Diamond_Armour")

        L_shop_armors_armor5.pack()

def shop_armor_armor6():
    global Iron_Armour
    global Mythril_Armour
    global Orichalium_Armour
    global gold
    global Jade_Armour
    global Diamond_Armour
    global BunSamosa_Armour
    global ACM_Armour
    global Silver_Armour
    global Gold_Armour
    if ACM_Armour == False:
        if gold > 500:
            gold = gold - 500
            L_shop_armors_armor6 = Label(frame_shop_armors_no, text="You now have ACM_Armour\n"
                                                                    f"You now have {gold} gold")
            L_shop_armors_armor6.pack()
            Iron_Armour = False
            Mythril_Armour = False
            Orichalium_Armour = False
            Jade_Armour = False
            Diamond_Armour = False
            ACM_Armour = True
            BunSamosa_Armour = False
            Gold_Armour=False
            Silver_Armour =False

        else:
            L_shop_armors_armor6 = Label(frame_shop_armors_no, text="You don't have enough gold.\n"
                                                                    f"You have {gold} gold")
            L_shop_armors_armor6.pack()
    else:
        L_shop_armors_armor6 = Label(frame_shop_armors_no, text="You already have ACM_Armour")
        L_shop_armors_armor6.pack()
  
def shop_armor_armor7():
    global Iron_Armour
    global Mythril_Armour
    global Orichalium_Armour
    global gold
    global Jade_Armour
    global Diamond_Armour
    global BunSamosa_Armour
    global ACM_Armour
    global Silver_Armour
    global Gold_Armour
    if BunSamosa_Armour == False:
        if gold > 600:
            gold = gold - 600
            L_shop_armors_armor7 = Label(frame_shop_armors_no, text="You now have BunSamosa_Armour\n"
                                                                    f"You now have {gold} gold")
            L_shop_armors_armor7.pack()
            Iron_Armour = False
            Mythril_Armour = False
            Orichalium_Armour = False
            Jade_Armour = False
            Diamond_Armour = False
            ACM_Armour = False
            BunSamosa_Armour = True
            Gold_Armour=False
            Silver_Armour =False

        else:
            L_shop_armors_armor7 = Label(frame_shop_armors_no, text="You don't have enough gold.\n"
                                                                    f"You have {gold} gold")
            L_shop_armors_armor7.pack()
    else:
        L_shop_armors_armor7 = Label(frame_shop_armors_no, text="You already have BunSamosa_Armour")
        L_shop_armors_armor7.pack()

def shop_armor_armor8():
    global Iron_Armour
    global Mythril_Armour
    global Orichalium_Armour
    global gold
    global Jade_Armour
    global Diamond_Armour
    global BunSamosa_Armour
    global ACM_Armour
    global Silver_Armour
    global Gold_Armour
    if BunSamosa_Armour == False:
        if gold > 650:
            gold = gold - 650
            L_shop_armors_armor8 = Label(frame_shop_armors_no, text="You now have Silver_Armour\n"
                                                                    f"You now have {gold} gold")
            L_shop_armors_armor8.pack()
            Iron_Armour = False
            Mythril_Armour = False
            Orichalium_Armour = False
            Jade_Armour = False
            Diamond_Armour = False
            ACM_Armour = False
            BunSamosa_Armour = False
            Gold_Armour=False
            Silver_Armour =True

        else:
            L_shop_armors_armor8 = Label(frame_shop_armors_no, text="You don't have enough gold.\n"
                                                                    f"You have {gold} gold")
            L_shop_armors_armor8.pack()
    else:
        L_shop_armors_armor8 = Label(frame_shop_armors_no, text="You already have Silver_Armour")
        L_shop_armors_armor8.pack()

def shop_armor_armor9():
    global Iron_Armour
    global Mythril_Armour
    global Orichalium_Armour
    global gold
    global Jade_Armour
    global Diamond_Armour
    global BunSamosa_Armour
    global ACM_Armour
    global Silver_Armour
    global Gold_Armour
    if BunSamosa_Armour == False:
        if gold > 700:
            gold = gold - 700
            L_shop_armors_armor9 = Label(frame_shop_armors_no, text="You now have Gold_Armour\n"
                                                                    f"You now have {gold} gold")
            L_shop_armors_armor9.pack()
            Iron_Armour = False
            Mythril_Armour = False
            Orichalium_Armour = False
            Jade_Armour = False
            Diamond_Armour = False
            ACM_Armour = False
            BunSamosa_Armour = False
            Gold_Armour=True
            Silver_Armour =False

        else:
            L_shop_armors_armor9 = Label(frame_shop_armors_no, text="You don't have enough gold.\n"
                                                                    f"You have {gold} gold")
            L_shop_armors_armor9.pack()
    else:
        L_shop_armors_armor9 = Label(frame_shop_armors_no, text="You already have Gold_Armour")
        L_shop_armors_armor9.pack()



def shop_armor_to_main():
    frame_shop_armors_no.destroy()
    shop()




def shop_armor_to_main():
    frame_shop_armors_no.destroy()
    shop()


def shop_exit():
    # L_shop_exit = Label(frame_shop_1, text="Leaving shop...")
    # L_shop_exit.pack()
    # time.sleep(2)
    frame_shop_1.destroy()
    get_room()


def shop():
    global gold
    global Iron_Sword
    global Mythril_Sword
    global Orichalium_Sword
    global Iron_Armour
    global Mythril_Armour
    global Orichalium_Armour
    global potion
    global ultra_potion
    global frame_shop_1
    global BunSamosa_Armour
    global ACM_Armour
    global Jade_Armour
    global Diamond_Armour
    global Gold_Armour
    global Silver_Armour
    try:
        frame_shop_1.destroy()
    except NameError:
        pass

    frame_shop_1 = Frame(root)
    frame_shop_1.pack()
    L_Shop_Wel = Label(
        frame_shop_1, text="Welcome to the store..\nWhat would you like to buy?\n")
    L_Shop_Wel.pack()
    # store1 variable to ask user what necessity do they need to buy
    # store1 = input("1=Potion, 2=Sword, 3=Armor, 4=Exit Store\n")
    B_Shop_Potion = Button(frame_shop_1, text="Potion",
                           command=lambda: shop_Potion())
    B_Shop_Potion.pack()
    B_Shop_Sword = Button(frame_shop_1, text="Sword",
                          command=lambda: shop_sword())
    B_Shop_Sword.pack()
    B_Shop_Armor = Button(frame_shop_1, text="Armor",
                          command=lambda: shop_armor())
    B_Shop_Armor.pack()
    B_Shop_ExitStore = Button(
        frame_shop_1, text="Exit Store", command=lambda: shop_exit())
    B_Shop_ExitStore.pack()
    # if invalid input..

    # If user wants to buy potions

    # If user wants to buy swords

    # # If user wants to exit the store.
    # if int(store1) == 4:
    #     typing("Leaving the store..")


def monster_potion_1():
    global frame_monster_potion_1
    frame_monster_potion_1 = Frame(root)
    frame_monster_potion_1.pack()
    L_monster_potion_info = Label(frame_monster_potion_1, text="We have three types of potions."
                                  "Small potion that increase your HP by 30\n"
                                  "And..\n"
                                  "Ultra potion that increase your HP by 50\n"
                                  "And..\n"
                                  "Medium potion that increases your HP by 40\n"
                                  f"Your HP is {hp}\n"
                                  f"You have {ultra_potion} ultra potions"
                                  f" and {potion} potions\n"
                                  f" and {medium_potion} medium potions\n"
                                  "Which potion would you like to drink?\n")
    L_monster_potion_info.pack()
    B_monster_potion_small = Button(
        frame_monster_potion_1, text="Small Potion", command=lambda: monster_potion_1_small())
    B_monster_potion_ultra = Button(
        frame_monster_potion_1, text="Ultra Potion", command=lambda: monster_potion_1_ultra())
    B_monster_potion_medium = Button(
        frame_monster_potion_1, text="Medium Potion", command=lambda: monster_potion_1_medium())
    B_monster_potion_medium.pack()
    B_monster_potion_small.pack()
    B_monster_potion_ultra.pack()
    B_monster_potion_back = Button(
        frame_monster_potion_1, text="back to battle", command=lambda: monster_potion_to_attack())
    B_monster_potion_back.pack()


def monster_potion_to_attack():
    frame_monster_potion_1.destroy()
    fight_monster()


def monster_potion_1_small():
    global potion
    global hp
    if potion == 0:
        L_monster_potion_1_small = Label(
            frame_monster_potion_1, text="You have no small potions")
        L_monster_potion_1_small.pack()
    else:
        potion = potion - 1
        hp = hp + 30
        if hp > 100:
            hp = 100
        L_monster_potion_1_small = Label(frame_monster_potion_1, text=f"You HP is now {hp}\n"
                                                                      f"You have {potion} small potions remaining")
        L_monster_potion_1_small.pack()


def monster_potion_1_ultra():
    global ultra_potion
    global hp
    if ultra_potion == 0:
        L_monster_potion_1_ultra = Label(
            frame_monster_potion_1, text="You have no ultra potions")
        L_monster_potion_1_ultra.pack()
    else:
        ultra_potion = ultra_potion - 1
        hp = hp + 50
        if hp > 100:
            hp = 100
        L_monster_potion_1_ultra = Label(frame_monster_potion_1, text=f"You HP is now {hp}\n"
                                                                      f"You have {ultra_potion} ultra potions remaining")
        L_monster_potion_1_ultra.pack()


def monster_potion_1_medium():
    global medium_potion
    global hp
    if medium_potion == 0:
        L_monster_potion_1_medium = Label(
            frame_monster_potion_1, text="You have no medium potions")
        L_monster_potion_1_medium.pack()
    else:
        medium_potion = medium_potion - 1
        hp = hp + 40
        if hp > 100:
            hp = 100
        L_monster_potion_1_medium = Label(frame_monster_potion_1, text=f"You HP is now {hp}\n"
                                          f"You have {medium_potion} medium potions remaining")
        L_monster_potion_1_medium.pack()


def you_died():
    frame_you_died = Frame(root)
    frame_you_died.pack()
    L_You_Died = Label(frame_monster_attack_1, text=f"You got killed by {monster}.\n"
                                                    f"You couldn't reach the final treasure.\n"
                                                    f"Better luck next time.")
    L_You_Died.pack()
    B_You_died = Button(frame_monster_attack_1,
                        text="Quit", command=lambda: quit())
    B_You_died.pack()


def quit():
    root.quit()

def Special_ability_heal():
    global monster
    global ability
    global opp_hp
    global turn
    if turn > 2:
        return
    else:
        heal = opp_hp * 0.1
        L_monster_heal = Label(frame_monster_attack_1, text=f"{monster} uses {ability} and heals {heal} HP, Monster HP: {opp_hp}")

        L_monster_heal.pack()
        opp_hp = opp_hp + heal


def monster_counterattack_1():
    global monster
    global ability
    global turn
    global hp
    turn += 1
    L_monster_counterattack_1 = Label(
        frame_monster_attack_1, text=f"Now {monster} will take it's turn.\n")
    L_monster_counterattack_1.pack()

    if ability == "heal":
        Special_ability_heal()
    opp_attack = random.randint(((m - 1) * 10), (m * 10)) // 10
    if ability == "shield" and turn <= 2:
        opp_attack = opp_attack // 2
        L_monster_shield = Label(frame_monster_attack_1, text=f"{monster} uses {ability}, Its attack power is halfed this turn")
        L_monster_shield.pack()
    hp = hp - opp_attack
    if ability == "double attack" and turn <= 3:
        opp_attack = random.randint(((m - 1) * 10), (m * 10)) // 10
        L_monster_double = Label(frame_monster_attack_1, text=f"{monster} uses {ability}, It will attack twice this turn")
        L_monster_double.pack()
        hp = hp - opp_attack2

    if ability == "poison" and turn <= 3:
        poison_damage = 5
        hp = hp - poison_damage
    if Iron_Armour == True:
        hp = hp + 10
    elif Mythril_Armour == True:
        hp = hp + 20
    elif Orichalium_Armour == True:
        hp = hp + 30

    if hp < 0:
        hp = 0
        L_monster_counterattack_result = Label(
            frame_monster_attack_1, text=f"Your HP={hp}\n")
        L_monster_counterattack_result.pack()
        you_died()

    

    else:
        if hp >100 : hp = 100 

        L_monster_counterattack_result = Label(frame_monster_attack_1, text=f"Your HP={hp}\n")

        L_monster_counterattack_result.pack()
        B_monster_attack_2 = Button(
            frame_monster_attack_1, text="Attack", command=lambda: monster_counter_to_attack())
        B_monster_potion_2 = Button(
            frame_monster_attack_1, text="Potion", command=lambda: monster_counter_to_potion())
        B_monster_attack_2.pack()
        B_monster_potion_2.pack()

def monster_counter_to_potion():
    frame_monster_attack_1.destroy()
    monster_potion_1()


def monster_counter_to_attack():
    frame_monster_attack_1.destroy()
    monster_attack_1()


def monster_attack_1():
    global gold
    global reward
    global opp_hp
    global frame_monster_attack_1
    try:
        frame_monster_attack_1.destroy()
    except NameError:
        pass
    frame_monster_attack_1 = Frame(root)
    frame_monster_attack_1.pack()
    L_monster_attack_1 = Label(
        frame_monster_attack_1, text="You chose to attack.\n")
    L_monster_attack_1.pack()
    userattack = random.randint(40, 70)
    opp_hp = opp_hp - userattack
    if Iron_Sword == True:
        opp_hp = opp_hp - 20

    elif Mythril_Sword == True:
        opp_hp = opp_hp - 30

    elif Orichalium_Sword == True:
        opp_hp = opp_hp - 40

    if opp_hp > 0:
        L_monster_attack_result = Label(
            frame_monster_attack_1, text=f"{monster}'s HP={opp_hp}\n")
        L_monster_attack_result.pack()
        monster_counterattack_1()

    if opp_hp <= 0:
        turn = 1
        opp_hp = 0
        gold = gold + reward
        L_monster_attack_result = Label(frame_monster_attack_1, text=f"{monster}'s HP={opp_hp}\n"
                                                                     f"Your HP = {hp}\n"
                                                                     f"you defeated {monster}\n"
                                                                     "You have some time to rest.\n"
                                                                     "Would you like to use a potion?\n")
        L_monster_attack_result.pack()
        B__monster_attack_result_yes = Button(
            frame_monster_attack_1, text="Yes", command=lambda: drink_potion())
        B__monster_attack_result_no = Button(
            frame_monster_attack_1, text="No", command=lambda: monster_rest_no_to_room())
        B__monster_attack_result_yes.pack()
        B__monster_attack_result_no.pack()


def monster_rest_no_to_room():
    frame_monster_attack_1.destroy()
    get_room()


def monster_rest_to_room():
    frame_monster_potion_1.destroy()
    get_room()


def drink_potion():
    global frame_monster_potion_1
    frame_monster_attack_1.destroy()
    frame_monster_potion_1 = Frame(root)
    frame_monster_potion_1.pack()
    L_monster_potion_info = Label(frame_monster_potion_1, text="We have three types of potions."
                                  "Small potion that increase your HP by 30\n"
                                  "And..\n"
                                  "Ultra potion that increase your HP by 50\n"
                                  "And..\n"
                                  "Medium potion that increases your HP by 40\n"
                                  f"Your HP is {hp}\n"
                                  f"You have {ultra_potion} ultra potions"
                                  f" and {potion} potions\n"
                                  f" and {medium_potion} medium potions\n"
                                  "Which potion would you like to drink?\n")
    L_monster_potion_info.pack()
    B_monster_potion_small = Button(
        frame_monster_potion_1, text="Small Potion", command=lambda: monster_potion_1_small())
    B_monster_potion_ultra = Button(
        frame_monster_potion_1, text="Ultra Potion", command=lambda: monster_potion_1_ultra())
    B_monster_potion_medium = Button(
        frame_monster_potion_1, text="Medium Potion", command=lambda: monster_potion_1_medium())
    B_monster_potion_medium.pack()
    B_monster_potion_small.pack()
    B_monster_potion_ultra.pack()
    B_next_room = Button(frame_monster_potion_1, text="Next",
                         command=lambda: monster_rest_to_room())
    B_next_room.pack()


def fight_monster_to_monster_attack():
    frame_fight_monster.destroy()
    monster_attack_1()


def fight_monster_to_monster_potion():
    frame_fight_monster.destroy()
    monster_potion_1()


def fight_monster():
    global monster
    global opp_hp
    global hp
    global frame_fight_monster
    
    try:
        frame_fight_monster.destroy()
    except NameError:
        pass

    frame_fight_monster = Frame(root)
    frame_fight_monster.pack()
    L_monster_intro = Label(frame_fight_monster, text=f"Your HP = {hp}\n"
                                                      f"{monster}'s HP = {opp_hp}\n"
                                                      "Would you like to attack or use potion??\n")
    L_monster_intro.pack()
    B_monster_attack_1 = Button(
        frame_fight_monster, text="Attack", command=lambda: fight_monster_to_monster_attack())
    B_monster_potion_1 = Button(
        frame_fight_monster, text="Potion", command=lambda: fight_monster_to_monster_potion())
    B_monster_attack_1.pack()
    B_monster_potion_1.pack()


def get_monster(rav):
    global ability
    global m
    global opp_hp
    global monster
    global frame_monster_1
    global reward

    try:
        frame_monster_1.destroy()
    except:
        pass

    frame_monster_1 = Frame(root)
    frame_monster_1.pack()

    EASY_MONSTERS = ("Goblin", "Werewolf", "Golum", "Rhegar", "Basilisk")
    MEDIUM_MONSTERS = ("Minotaur", "Orc", "Griffin", "Lola")
    HARD_MONSTERS = ("Dragon", "Cyclop", "Mike", "Dark Elf")
    EXPERT_MONSTERS = ("Dave", "Siri", "GrimReaper", "Dementor", "UrGhast", "Robert", "Carlson", "Severus", "Snape")

    EASY_REWARD = 20
    MEDIUM_REWARD = 50
    HARD_REWARD = 80
    EXPERT_REWARD = 120

    opp_hp = 100

    monster_prob = random.random()

    if 1 <= rav <= 5:
        if monster_prob < 0.8:
            monster = random.choice(EASY_MONSTERS)
            reward = EASY_REWARD
            ability = "heal"
        else:
            monster = random.choice(MEDIUM_MONSTERS)
            reward = MEDIUM_REWARD
            opp_hp = 120
            ability = "poison"
    elif 6 <= rav <= 10:
        if monster_prob < 0.2:
            monster = random.choice(EASY_MONSTERS)
            reward = EASY_REWARD
            ability = "heal"
        elif 0.2 <= monster_prob <= 0.8:
            monster = random.choice(MEDIUM_MONSTERS)
            reward = MEDIUM_REWARD
            opp_hp = 120
            ability = "poison"
        else:
            monster = random.choice(HARD_MONSTERS)
            reward = HARD_REWARD
            opp_hp = 150
            ability = "shield"
    elif 11 <= rav <= 15:
        if monster_prob < 0.4:
            monster = random.choice(MEDIUM_MONSTERS)
            reward = MEDIUM_REWARD
            opp_hp = 120
            ability = "poison"
        elif 0.4 <= monster_prob <= 0.8:
            monster = random.choice(HARD_MONSTERS)
            reward = HARD_REWARD
            opp_hp = 150
            ability = "shield"
        else:
            monster = random.choice(EXPERT_MONSTERS)
            reward = EXPERT_REWARD
            opp_hp = 200
            ability = "double attack"
    elif 16 <= rav <= 19:
        if monster_prob < 0.2:
            monster = random.choice(HARD_MONSTERS)
            reward = HARD_REWARD
            opp_hp = 150
            ability = "shield"
        else:
            monster = random.choice(EXPERT_MONSTERS)
            reward = EXPERT_REWARD
            opp_hp = 200
            ability = "double attack"

    monster_lower = monster.lower()
    
    m_values = {
        "goblin": 1, "golum": 13, "rhegar": 14, "werewolf": 2, "basilisk": 3,
        "minotaur": 4, "griffin": 5, "dragon": 6, "orc": 9, "dark elf": 10,
        "mike": 7, "dave": 8, "severus": 11, "snape": 12, "lola": 19,
        "cyclop": 20, "siri": 13, "grimreaper": 14, "dementor": 15,
        "urghast": 16, "robert": 17, "carlson": 18
    }
    
    m = m_values.get(monster_lower, 1)
    
    L_m_intro = Label(frame_monster_1, text=f"You have to face {monster}\n"
                                           "The match starts. You get the first chance\n")
    L_m_intro.pack()
    
    fight_monster()

def quit_screen():
    quit_scr = Label(frame_monster_1, text="Game over")
    quit_scr.pack()


def get_bossmonster():
    global m
    global opp_hp
    global monster
    global frame_monster_1
    frame_monster_1 = Frame(root)
    frame_monster_1.pack()
    L_monster_Wel = Label(
        frame_monster_1, text="You have to fight a boss monster.")
    L_monster_Wel.pack()
    bossmonsters = ("Demon Slayer", "Big Tooth")
    monster = random.choice(bossmonsters)
    # print(monster)
    opp_hp = 100
    if monster == "Demon Slayer":
        m = 1
        # monster 1
        # Attack in range of 0-10
        L_m1_intro = Label(frame_monster_1, text="You have to face Demon Slayer\n"
                                                 "The match starts. You get the first chance\n")
        L_m1_intro.pack()
        fight_monster()
        # opp_att = random.randint(0, 10)

    if monster == "Big Tooth":
        m = 2
        # monster 2
        # Attack in range of 10-20
        L_m2_intro = Label(frame_monster_1, text="You have to face Big Tooth\n"
                                                 "The match starts. You get the first chance\n")
        L_m2_intro.pack()
        fight_monster()
        # opp_att = random.randint(10, 20)
    b = Button(frame1, text="Quit", command=quit_screen)
    b.pack()




def inventory():
    global Iron_Sword 
    global Mythril_Sword 
    global Orichalium_Sword 
    global Iron_Armour 
    global Mythril_Armour
    global Orichalium_Armour 
    global potion 
    global ultra_potion 
    global medium_potion
    global BunSamosa_Armour
    global ACM_Armour
    global Silver_Armour
    global Gold_Armour 
    newWindow = Toplevel(root)  
 
    newWindow.title("inventory")
 
    newWindow.geometry("250x250")
    Label(newWindow,text ="welcome to inventory").pack()

    if(Iron_Sword):
        iron_s_l=Label(newWindow,text ="iron sword\n").pack()
    if(Mythril_Sword):
        mythril_s_l=Label(newWindow,text ="mythril sword\n").pack()
    if(Orichalium_Sword):
        orichallium_s_l=Label(newWindow,text ="orichalium sword\n").pack()
    if(Iron_Armour):
        iron_a_l=Label(newWindow,text ="iron armour\n").pack()
    if(Mythril_Armour):
        mythril_a_l=Label(newWindow,text ="mythril armour\n").pack()
    if(Orichalium_Armour):
        orichalium_a_l=Label(newWindow,text ="orichalium armour\n").pack()
    if(BunSamosa_Armour):
        bun_a_l=Label(newWindow,text ="bunsamosa armour\n").pack()
    if(ACM_Armour):
        acm_a_l=Label(newWindow,text ="acm armour\n").pack()
    if(Silver_Armour):
        acm_a_l=Label(newWindow,text ="Silver armour\n").pack()
    if(Gold_Armour):
        acm_a_l=Label(newWindow,text ="Gold armour\n").pack()
    if(potion!=0):
        small_label=Label(newWindow,text =f"small potion x {potion}\n").pack()
    else:
        small_label=Label(newWindow,text ="").pack()
    if(medium_potion!=0):
        medium_label=Label(newWindow,text =f"medium potion x {medium_potion}\n").pack()
    else:
        medium_label=Label(newWindow,text ="").pack()
    if(ultra_potion!=0):
        ultra_label=Label(newWindow,text =f"ultra potion x {ultra_potion}\n").pack()
    else:
        ultra_label=Label(newWindow,text ="").pack()
 
 


root = Tk()
inventory_button=Button(text="inventory",command=inventory)
inventory_button.pack(side=BOTTOM)
root.title("The Quest")
frame1 = Frame(root, padx=50, pady=50)
frame1.pack(padx=50, pady=50)
root.geometry("500x500")
label = Label(frame1, text="Welcome to The Quest!!\nStory...\nIntro")
label.pack()

welcome_button = Button(frame1, text='Next', command=lambda: get_room())
welcome_button.pack()

root.mainloop()