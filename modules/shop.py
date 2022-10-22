
from tkinter import *

import modules.globalGameAttributes as globals

def shop_potion():
    globals.frame_shop_1.destroy()
    globals.frame_shop_potion = Frame(globals.root)
    globals.frame_shop_potion.pack()
    L_Shop_Potion_1 = Label(globals.frame_shop_potion, text=f"You currently have {globals.player.potion} Small potions and {globals.plyer.ultra_potion} Ultra potions with you.\n"
                                                    f"We have 3 types of potion.\n"
                                                    f"Small Potion, Ultra Potion and Medium potion\n"
                                                    f"Would you like to know more about them?\n")
    L_Shop_Potion_1.pack()
    B_Shop_Potion_Y = Button(globals.frame_shop_potion, text="Yes", command=lambda: shop_potion_yes())
    B_Shop_Potion_N = Button(globals.frame_shop_potion, text="No", command=lambda: shop_potion_no())
    B_Shop_Potion_Y.pack(side=BOTTOM)
    B_Shop_Potion_N.pack(side=BOTTOM)


def shop_potion_no():
    globals.frame_shop_potion.destroy()
    globals.frame_shop_potion_no = Frame(globals.root)
    globals.frame_shop_potion_no.pack()
    L_Shop_Potion_No = Label(globals.frame_shop_potion_no, text="Okay then..\n"
                                                        "Which potion would you like to buy?")
    L_Shop_Potion_No.pack()
    B_Shop_Potion_No_SP = Button(globals.frame_shop_potion_no, text="Small Potion", command=lambda: shop_potions_small())
    B_Shop_Potion_No_UP = Button(globals.frame_shop_potion_no, text="Ultra Potion", command=lambda: shop_potions_ultra())
    B_Shop_Potion_No_MP = Button(globals.frame_shop_potion_no, text="Medium Potion", command=lambda: shop_potions_medium())
    B_Shop_Potion_No_UP.pack()
    B_Shop_Potion_No_SP.pack()
    B_Shop_Potion_No_MP.pack()


def shop_potion_yes():
    globals.frame_shop_potion.destroy()
    globals.frame_shop_potion_yes = Frame(globals.root)
    globals.frame_shop_potion_yes.pack()
    L_Shop_Potion_Yes = Label(globals.frame_shop_potion_yes, text="Small potion that costs 250 gold will increase your HP by 30\n"
                                                          "And..\n"
                                                          "Ultra potion that costs 600 gold will increase your HP by 50\n"
                                                          "And..\n"
                                                          "Medium potion that costs 450 gold will increase your HP by 40")
    L_Shop_Potion_Yes.pack()
    B_Shop_Potion_Yes = Button(globals.frame_shop_potion_yes, text="Next", command=lambda: shop_potion_yestono())
    B_Shop_Potion_Yes.pack()


def shop_potion_yestono():
    globals.frame_shop_potion_yes.destroy()
    shop_potion_no()


def shop_potions_small():
    globals.frame_shop_potion_no.destroy()
    globals.frame_shop_potion_small = Frame(globals.root)
    globals.frame_shop_potion_small.pack()
    L_shop_potion_small = Label(globals.frame_shop_potion_small, text="How many Small potions would you like to buy?\n"
                                                              "Cost=250 gold\n"
                                                              f"You have {globals.player.gold} gold")
    L_shop_potion_small.pack()

    B_shop_potion_small = Button(globals.frame_shop_potion_small, text="Buy", command=lambda: shop_potion_small_buy())
    B_shop_potion_small.pack()
    B_shop_potion_small_main = Button(globals.frame_shop_potion_small, text="Back", command=lambda: shop_potions_small_to_main())
    B_shop_potion_small_main.pack(side=BOTTOM)

def shop_potions_small_to_main():
    globals.frame_shop_potion_small.destroy()
    globals.rooms.shop()

def shop_potion_small_buy():
    if globals.player.gold - 250 < 0:
        L_shop_potion_small = Label(globals.frame_shop_potion_small, text="You don't have enough gold.\n"
                                                                  "Let's shop for something else..\n")
        L_shop_potion_small.pack()
        # If user has enough globals.player.gold
    else:
        potion = potion + 1
        globals.player.gold = globals.player.gold - 250
        L_shop_potion_small = Label(globals.frame_shop_potion_small, text=(f"You now have {globals.player.gold} gold with you\n"
                                                                   f"You now have {globals.player.potion} Small Potions with you\n"
                                                                   "Let's continue shopping.."))
        L_shop_potion_small.pack()


def shop_potions_ultra():
    globals.frame_shop_potion_no.destroy()
    globals.frame_shop_potion_ultra = Frame(globals.root)
    globals.frame_shop_potion_ultra.pack()
    L_shop_potion_ultra = Label(globals.frame_shop_potion_ultra, text="How many Ultra potions would you like to buy?\n"
                                                              "Cost=600 gold\n"
                                                              f"You have {globals.player.gold} gold")
    L_shop_potion_ultra.pack()
    B_shop_potion_ultra = Button(globals.frame_shop_potion_ultra, text="Buy", command=lambda: shop_potion_ultra_buy())
    B_shop_potion_ultra.pack()
    B_shop_potion_ultra_main = Button(globals.frame_shop_potion_ultra, text="Back", command=lambda: shop_potions_ultra_to_main())
    B_shop_potion_ultra_main.pack(side=BOTTOM)

def shop_potions_ultra_to_main():
    globals.frame_shop_potion_ultra.destroy()
    globals.rooms.shop()


def shop_potion_ultra_buy():
    if globals.player.gold - 600 < 0:
        L_shop_potion_ultra = Label(globals.frame_shop_potion_ultra, text="You don't have enough gold.\n"
                                                                  f"You have {globals.player.gold} gold with you\n"
                                    f"You have {ultra_potion} Ultra Potions with you\n"
                                    "Let's shop for something else..\n")
        L_shop_potion_ultra.pack()
    else:
        ultra_potion = ultra_potion + 1
        globals.player.gold = globals.player.gold - 600
        L_shop_potion_ultra = Label(globals.frame_shop_potion_ultra, text=(f"You now have {globals.player.gold} gold with you\n"
                                                                   f"You now have {globals.player.ultra_potion} Ultra Potions with you\n"
                                                                   "Let's continue shopping.."))
        L_shop_potion_ultra.pack()


def shop_potions_medium():
    globals.frame_shop_potion_no.destroy()
    globals.frame_shop_potion_medium = Frame(globals.root)
    globals.frame_shop_potion_medium.pack()
    L_shop_potion_medium = Label(globals.frame_shop_potion_medium, text="How many Medium potions would you like to buy?\n"
                                 "Cost=450 gold\n"
                                 f"You have {globals.player.gold} gold")
    L_shop_potion_medium.pack()
    B_shop_potion_medium = Button(globals.frame_shop_potion_medium, text="Buy", command=lambda: shop_potion_medium_buy())
    B_shop_potion_medium.pack()
    B_shop_potion_medium_main = Button(globals.frame_shop_potion_medium, text="Back", command=lambda: shop_potions_medium_to_main())
    B_shop_potion_medium_main.pack(side=BOTTOM)


def shop_potions_medium_to_main():
    globals.frame_shop_potion_medium.destroy()
    globals.rooms.shop()


def shop_potion_medium_buy():
    if globals.player.gold - 450 < 0:
        L_shop_potion_medium = Label(globals.frame_shop_potion_medium, text="You don't have enough gold.\n"
                                     f"You have {globals.player.gold} gold with you\n"
                                     f"You have {globals.player.medium_potion} Medium Potions with you\n"
                                     "Let's shop for something else..\n")
        L_shop_potion_medium.pack()
    else:
        medium_potion = medium_potion + 1
        globals.player.gold = globals.player.gold - 450
        L_shop_potion_medium = Label(globals.frame_shop_potion_medium, text=(f"You now have {globals.player.gold} gold with you\n"
                                                                     f"You now have {globals.player.medium_potion} Medium Potions with you\n"
                                                                     "Let's continue shopping.."))
        L_shop_potion_medium.pack()


def shop_sword():
    globals.frame_shop_1.destroy()
    globals.frame_shop_sword = Frame(globals.root)
    globals.frame_shop_sword.pack()
    if globals.player.Iron_Sword:
        L_Shop_Sword_owned = Label(
        globals.frame_shop_sword, text="Right now, you have Iron_Sword")
        L_Shop_Sword_owned.pack()
    elif globals.player.Mythril_Sword:
        L_Shop_Sword_owned = Label(
        globals.frame_shop_sword, text="Right now you have Mythril_Sword ")
        L_Shop_Sword_owned.pack()
    elif globals.player.Orichalium_Sword:
        L_Shop_Sword_owned = Label(
        globals.frame_shop_sword, text="Right now you have Orichalium_Sword")
        L_Shop_Sword_owned.pack()
    L_Shop_Sword_intro = Label(globals.frame_shop_sword, text="We have 3 types of swords..\n"
                                                      "Iron_Sword, Mythril_Sword and Orichalium_Sword\n"
                                                      "Would you like to know more about them?\n")
    L_Shop_Sword_intro.pack()
    B_Shop_Sword_Y = Button(globals.frame_shop_sword, text="Yes",
                            command=lambda: shop_sword_yes())
    B_Shop_Sword_N = Button(globals.frame_shop_sword, text="No",
                            command=lambda: shop_sword_no())
    B_Shop_Sword_Y.pack()
    B_Shop_Sword_N.pack()


def shop_sword_yes():
    globals.frame_shop_sword.destroy()
    globals.frame_shop_sword_yes = Frame(globals.root)
    globals.frame_shop_sword_yes.pack()
    L_Shop_Sword_Y_info = Label(globals.frame_shop_sword_yes, text="Iron_Sword costs 200 gold and increases your attack by 20\n"
                                "Mythril_Sword costs 300 gold and increases your attack by 30\n"
                                "Orichalium_Sword costs 400 gold and increases your attack by 40\n")
    L_Shop_Sword_Y_info.pack()

    B_Shop_Sword_Yes = Button(
    globals.frame_shop_sword_yes, text="Next", command=lambda: shop_sword_yestono())
    B_Shop_Sword_Yes.pack()


def shop_sword_yestono():
    globals.frame_shop_sword_yes.destroy()
    shop_sword_no()


def shop_sword_no():
    globals.frame_shop_sword.destroy()
    globals.frame_shop_swords_no = Frame(globals.root)
    globals.frame_shop_swords_no.pack()
    L_Shop_Swords_N = Label(globals.frame_shop_swords_no,
                            text="Which sword would you like to buy?\n")
    L_Shop_Swords_N.pack()
    B_Shop_Swords_Sword1 = Button(
    globals.frame_shop_swords_no, text="Iron_Sword", command=lambda: shop_sword_sword1())
    B_Shop_Swords_Sword1.pack()
    B_Shop_Swords_Sword2 = Button(
    globals.frame_shop_swords_no, text="Mythril_Sword", command=lambda: shop_sword_sword2())
    B_Shop_Swords_Sword2.pack()
    B_Shop_Swords_Sword3 = Button(
    globals.frame_shop_swords_no, text="Orichalium_Sword", command=lambda: shop_sword_sword3())
    B_Shop_Swords_Sword3.pack()
    B_Shop_Swords_back = Button(
    globals.frame_shop_swords_no, text="back", command=lambda: shop_sword_to_main())
    B_Shop_Swords_back.pack(side=BOTTOM)


def shop_sword_sword1():
    if globals.player.Iron_Sword == False:
        if globals.player.gold > 200:
            globals.player.gold = globals.player.gold - 200
            L_shop_swords_sword1 = Label(globals.frame_shop_swords_no, text="You now have Iron_Sword\n"
                                                                    f"You now have {globals.player.gold} gold")
            L_shop_swords_sword1.pack()
            globals.player.Iron_Sword = True
            globals.player.Mythril_Sword = False
            globals.player.Orichalium_Sword = False

        else:
            L_shop_swords_sword1 = Label(globals.frame_shop_swords_no, text="You don't have enough gold.\n"
                                                                    f"You have {globals.player.gold} gold")
            L_shop_swords_sword1.pack()
    else:
        L_shop_swords_sword1 = Label(
        globals.frame_shop_swords_no, text="You already have Iron_Sword")
        L_shop_swords_sword1.pack()


def shop_sword_sword2():
    if globals.player.Mythril_Sword == False:
        if globals.player.gold > 300:
            globals.player.gold = globals.player.gold - 300
            L_shop_swords_sword2 = Label(globals.frame_shop_swords_no, text="You now have Mythril_Sword\n"
                                                                    f"You now have {globals.player.gold} gold")
            L_shop_swords_sword2.pack()
            globals.player.Iron_Sword = False
            globals.player.Mythril_Sword = True
            globals.player.Orichalium_Sword = False

        else:
            L_shop_swords_sword2 = Label(globals.frame_shop_swords_no, text="You don't have enough gold.\n"
                                                                    f"You have {globals.player.gold} gold")
            L_shop_swords_sword2.pack()
    else:
        L_shop_swords_sword2 = Label(
        globals.frame_shop_swords_no, text="You already have Mythril_Sword")
        L_shop_swords_sword2.pack()


def shop_sword_sword3():
    if globals.player.Orichalium_Sword == False:
        if globals.player.gold > 400:
            globals.player.gold = globals.player.gold - 400
            L_shop_swords_sword3 = Label(globals.frame_shop_swords_no, text="You now have Orichalium_Sword\n"
                                                                    f"You now have {globals.player.gold} gold")
            L_shop_swords_sword3.pack()
            globals.player.Iron_Sword = False
            globals.player.Mythril_Sword = False
            globals.player.Orichalium_Sword = True

        else:
            L_shop_swords_sword3 = Label(globals.frame_shop_swords_no, text="You don't have enough gold.\n"
                                                                    f"You have {globals.player.gold} gold")
            L_shop_swords_sword3.pack()
    else:
        L_shop_swords_sword3 = Label(
        globals.frame_shop_swords_no, text="You already have Orichalium_Sword")
        L_shop_swords_sword3.pack()


def shop_sword_to_main():
    globals.frame_shop_swords_no.destroy()
    globals.rooms.shop()


def shop_armor():
    globals.frame_shop_1.destroy()
    globals.frame_shop_armor = Frame(globals.root)
    globals.frame_shop_armor.pack()
    if globals.player.Iron_Armour:
        L_Shop_armor_owned = Label(
        globals.frame_shop_armor, text="Right now, you have Iron_Armour")
        L_Shop_armor_owned.pack()
    elif globals.player.Mythril_Armour:
        L_Shop_armor_owned = Label(
        globals.frame_shop_armor, text="Right now you have Mythril_Armour")
        L_Shop_armor_owned.pack()
    elif globals.player.BunSamosa_Armour:
        L_Shop_armor_owned = Label(
        globals.frame_shop_armor, text="Right now you have BunSamosa_Armour")
        L_Shop_armor_owned.pack()
    elif globals.player.ACM_Armour:
        L_Shop_armor_owned = Label(
        globals.frame_shop_armor, text="Right now you have ACM_Armour")
        L_Shop_armor_owned.pack()
    elif globals.player.Orichalium_Armour:
        L_Shop_armor_owned = Label(
        globals.frame_shop_armor, text="Right now you have Orichalium_Armour")
        L_Shop_armor_owned.pack()
    elif globals.player.Gold_Armour:
        L_Shop_armor_owned = Label(globals.frame_shop_armor, text="Right now you have Gold_Armour")
        L_Shop_armor_owned.pack()
    elif globals.player.Silver_Armour:
        L_Shop_armor_owned = Label(globals.frame_shop_armor, text="Right now you have Silver_Armour")
        L_Shop_armor_owned.pack()
    L_Shop_armor_intro = Label(globals.frame_shop_armor, text="We have 7 types of armors..\n"
                                                      "Iron_Armour, Mythril_Armour, Orichalium_Armour, BunSamosa_Armour, Silver_Armour, Gold_Armour and ACM_Armour\n"
                                                      "Would you like to know more about them?\n")
    L_Shop_armor_intro.pack()
    B_Shop_armor_Y = Button(globals.frame_shop_armor, text="Yes",
                            command=lambda: shop_armor_yes())
    B_Shop_armor_N = Button(globals.frame_shop_armor, text="No",
                            command=lambda: shop_armor_no())
    B_Shop_armor_Y.pack()
    B_Shop_armor_N.pack()


def shop_armor_yes():
    globals.frame_shop_armor.destroy()
    globals.frame_shop_armor_yes = Frame(globals.root)
    globals.frame_shop_armor_yes.pack()
    L_Shop_armor_Y_info = Label(globals.frame_shop_armor_yes, text="Iron_Armour costs 200 gold and increases your attack by 20\n"

                                                            "Mythril_Armour costs 300 gold and increases your attack by 30\n"
                                                            "Orichalium_Armour costs 400 gold and increases your attack by 40\n"
                                                            "Jade_Armour costs 250 gold and increases your hp by 10\n"
                                                            "Diamond_Armour costs 350 gold and increases your hp by 20\n"
                                                            "BunSamosa_Armour costs 500 gold and increases your attack by 50\n"
                                                            "ACM_Armour costs 600 gold and increases your attack by 60\n"
                                                            "Silver_Armour costs 550 gold and increases your attack by 65\n"
                                                            "Gold_Armour costs 700 gold and increases your attack by 70\n" )
         

    L_Shop_armor_Y_info.pack()

    B_Shop_armor_Yes = Button(
    globals.frame_shop_armor_yes, text="Next", command=lambda: shop_armor_yestono())
    B_Shop_armor_Yes.pack()


def shop_armor_yestono():
    globals.frame_shop_armor_yes.destroy()
    shop_armor_no()


def shop_armor_no():
    globals.frame_shop_armor.destroy()
    globals.frame_shop_armors_no = Frame(globals.root)
    globals.frame_shop_armors_no.pack()
    L_Shop_armors_N = Label(globals.frame_shop_armors_no,
                            text="Which armor would you like to buy?\n")
    L_Shop_armors_N.pack()
    B_Shop_armors_armor1 = Button(
    globals.frame_shop_armors_no, text="Iron_Armour", command=lambda: shop_armor_armor1())
    B_Shop_armors_armor1.pack()
    B_Shop_armors_armor2 = Button(
    globals.frame_shop_armors_no, text="Mythril_Armour", command=lambda: shop_armor_armor2())
    B_Shop_armors_armor2.pack()
    B_Shop_armors_armor3 = Button(
    globals.frame_shop_armors_no, text="Orichalium_Armour", command=lambda: shop_armor_armor3())
    B_Shop_armors_armor3.pack()

    B_Shop_armors_armor4 = Button(globals.frame_shop_armors_no, text="Jade_Armour", command=lambda: shop_armor_armor4())
    B_Shop_armors_armor4.pack()
    B_Shop_armors_armor5 = Button(globals.frame_shop_armors_no, text="Diamond_Armour", command=lambda: shop_armor_armor5())
    B_Shop_armors_armor5.pack()    
    B_Shop_armors_armor6= Button(globals.frame_shop_armors_no, text="BunSamosa_Armour", command=lambda: shop_armor_armor6())
    B_Shop_armors_armor6.pack()
    B_Shop_armors_armor7 = Button(globals.frame_shop_armors_no, text="ACM_Armour", command=lambda: shop_armor_armor7())
    B_Shop_armors_armor7.pack()
    B_Shop_armors_armor8 = Button(globals.frame_shop_armors_no, text="Silver_Armour", command=lambda: shop_armor_armor8())
    B_Shop_armors_armor8.pack()
    B_Shop_armors_armor9 = Button(globals.frame_shop_armors_no, text="Gold_Armour", command=lambda: shop_armor_armor9())
    B_Shop_armors_armor9.pack()
    B_Shop_armors_back = Button(globals.frame_shop_armors_no, text="back", command=lambda: shop_armor_to_main())

    B_Shop_armors_back.pack(side=BOTTOM)


def shop_armor_armor1():
    if globals.player.Iron_Armour == False:
        if globals.player.gold > 200:
            globals.player.gold = globals.player.gold - 200
            L_shop_armors_armor1 = Label(globals.frame_shop_armors_no, text="You now have Iron_Armour\n"
                                                                    f"You now have {globals.player.gold} gold")
            L_shop_armors_armor1.pack()
            globals.player.Iron_Armour = True
            globals.player.Mythril_Armour = False
            globals.player.Orichalium_Armour = False
            globals.player.Jade_Armour = False
            globals.player.Diamond_Armour = False
            globals.player.ACM_Armour = False
            globals.player.BunSamosa_Armour = False
            globals.player.Gold_Armour=False
            globals.player.Silver_Armour =False

        else:
            L_shop_armors_armor1 = Label(globals.frame_shop_armors_no, text="You don't have enough gold.\n"
                                                                    f"You have {globals.player.gold} gold")
            L_shop_armors_armor1.pack()
    else:
        L_shop_armors_armor1 = Label(
        globals.frame_shop_armors_no, text="You already have Iron_Armour")
        L_shop_armors_armor1.pack()


def shop_armor_armor2():
    if globals.player.Mythril_Armour == False:
        if globals.player.gold > 300:
            globals.player.gold = globals.player.gold - 300
            L_shop_armors_armor2 = Label(globals.frame_shop_armors_no, text="You now have Mythril_Armour\n"
                                                                    f"You now have {globals.player.gold} gold")
            L_shop_armors_armor2.pack()
            globals.player.Iron_Armour = False
            globals.player.Mythril_Armour = True
            globals.player.Orichalium_Armour = False
            globals.player.Jade_Armour = False
            globals.player.Diamond_Armour = False
            globals.player.ACM_Armour = False
            globals.player.BunSamosa_Armour = False
            globals.player.Gold_Armour=False
            globals.player.Silver_Armour =False

        else:
            L_shop_armors_armor2 = Label(globals.frame_shop_armors_no, text="You don't have enough gold.\n"
                                                                    f"You have {globals.player.gold} gold")
            L_shop_armors_armor2.pack()
    else:
        L_shop_armors_armor2 = Label(
        globals.frame_shop_armors_no, text="You already have Mythril_Armour")
        L_shop_armors_armor2.pack()


def shop_armor_armor3():
    if globals.player.Orichalium_Armour == False:
        if globals.player.gold > 400:
            globals.player.gold = globals.player.gold - 400
            L_shop_armors_armor3 = Label(globals.frame_shop_armors_no, text="You now have Orichalium_Armour\n"
                                                                    f"You now have {globals.player.gold} gold")
            L_shop_armors_armor3.pack()
            globals.player.Iron_Armour = False
            globals.player.Mythril_Armour = False
            globals.player.Orichalium_Armour = True
            globals.player.Jade_Armour = False
            globals.player.Diamond_Armour = False
            globals.player.ACM_Armour = False
            globals.player.BunSamosa_Armour = False
            globals.player.Gold_Armour=False
            globals.player.Silver_Armour =False

        else:
            L_shop_armors_armor3 = Label(globals.frame_shop_armors_no, text="You don't have enough gold.\n"
                                                                    f"You have {globals.player.gold} gold")
            L_shop_armors_armor3.pack()
    else:
        L_shop_armors_armor3 = Label(
        globals.frame_shop_armors_no, text="You already have Orichalium_Armour")
        L_shop_armors_armor3.pack()


def shop_armor_armor4():
    if globals.player.Jade_Armour == False:
        if globals.player.gold > 250:
            globals.player.gold = globals.player.gold - 250
            L_shop_armors_armor4 = Label(globals.frame_shop_armors_no, text="You now have Jade_Armour\n"

                                                                    f"You now have {globals.player.gold} gold")
            L_shop_armors_armor4.pack()
            globals.player.Iron_Armour = False
            globals.player.Mythril_Armour = False
            globals.player.Orichalium_Armour = False
            globals.player.Jade_Armour = True
            globals.player.Diamond_Armour = False
            globals.player.ACM_Armour = False
            globals.player.BunSamosa_Armour = False
            globals.player.Gold_Armour=False
            globals.player.Silver_Armour =False

        else:
            L_shop_armors_armor4 = Label(globals.frame_shop_armors_no, text="You don't have enough gold.\n"
                                                                    f"You have {globals.player.gold} gold")
            L_shop_armors_armor4.pack()
    else:
        L_shop_armors_armor4 = Label(globals.frame_shop_armors_no, text="You already have Jade_Armour")
        L_shop_armors_armor4.pack()
        

def shop_armor_armor5():
    if globals.player.Diamond_Armour == False:
        if globals.player.gold > 350:
            globals.player.gold = globals.player.gold - 350
            L_shop_armors_armor5 = Label(globals.frame_shop_armors_no, text="You now have Diamond_Armour\n"

                                                                    f"You now have {globals.player.gold} gold")
            L_shop_armors_armor5.pack()
            globals.player.Iron_Armour = False
            globals.player.Mythril_Armour = False
            globals.player.Orichalium_Armour = False
            globals.player.Jade_Armour = False
            globals.player.Diamond_Armour = True
            globals.player.ACM_Armour = False
            globals.player.BunSamosa_Armour = False
            globals.player.Gold_Armour=False
            globals.player.Silver_Armour =False

        else:
            L_shop_armors_armor5 = Label(globals.frame_shop_armors_no, text="You don't have enough gold.\n"
                                                                    f"You have {globals.player.gold} gold")
            L_shop_armors_armor5.pack()
    else:

        L_shop_armors_armor5 = Label(globals.frame_shop_armors_no, text="You already have Diamond_Armour")
        L_shop_armors_armor5.pack()

def shop_armor_armor6():
    if globals.player.ACM_Armour == False:
        if globals.player.gold > 500:
            globals.player.gold = globals.player.gold - 500
            L_shop_armors_armor6 = Label(globals.frame_shop_armors_no, text="You now have ACM_Armour\n"
                                                                    f"You now have {globals.player.gold} gold")
            L_shop_armors_armor6.pack()
            globals.player.Iron_Armour = False
            globals.player.Mythril_Armour = False
            globals.player.Orichalium_Armour = False
            globals.player.Jade_Armour = False
            globals.player.Diamond_Armour = False
            globals.player.ACM_Armour = True
            globals.player.BunSamosa_Armour = False
            globals.player.Gold_Armour=False
            globals.player.Silver_Armour =False
        else:
            L_shop_armors_armor6 = Label(globals.frame_shop_armors_no, text="You don't have enough gold.\n"
                                                                    f"You have {globals.player.gold} gold")
            L_shop_armors_armor6.pack()
    else:
        L_shop_armors_armor6 = Label(globals.frame_shop_armors_no, text="You already have ACM_Armour")
        L_shop_armors_armor6.pack()
  
def shop_armor_armor7():
    if globals.player.BunSamosa_Armour == False:
        if globals.player.gold > 600:
            globals.player.gold = globals.player.gold - 600
            L_shop_armors_armor7 = Label(globals.frame_shop_armors_no, text="You now have BunSamosa_Armour\n"
                                                                    f"You now have {globals.player.gold} gold")
            L_shop_armors_armor7.pack()
            globals.player.Iron_Armour = False
            globals.player.Mythril_Armour = False
            globals.player.Orichalium_Armour = False
            globals.player.Jade_Armour = False
            globals.player.Diamond_Armour = False
            globals.player.ACM_Armour = False
            globals.player.BunSamosa_Armour = True
            globals.player.Gold_Armour=False
            globals.player.Silver_Armour =False
        else:
            L_shop_armors_armor7 = Label(globals.frame_shop_armors_no, text="You don't have enough gold.\n"
                                                                    f"You have {globals.player.gold} gold")
            L_shop_armors_armor7.pack()
    else:
        L_shop_armors_armor7 = Label(globals.frame_shop_armors_no, text="You already have BunSamosa_Armour")
        L_shop_armors_armor7.pack()

def shop_armor_armor8():
    if globals.player.BunSamosa_Armour == False:
        if globals.player.gold > 650:
            globals.player.gold = globals.player.gold - 650
            L_shop_armors_armor8 = Label(globals.frame_shop_armors_no, text="You now have Silver_Armour\n"
                                                                    f"You now have {globals.player.gold} gold")
            L_shop_armors_armor8.pack()
            globals.player.Iron_Armour = False
            globals.player.Mythril_Armour = False
            globals.player.Orichalium_Armour = False
            globals.player.Jade_Armour = False
            globals.player.Diamond_Armour = False
            globals.player.ACM_Armour = False
            globals.player.BunSamosa_Armour = False
            globals.player.Gold_Armour=False
            globals.player.Silver_Armour =True
        else:
            L_shop_armors_armor8 = Label(globals.frame_shop_armors_no, text="You don't have enough gold.\n"
                                                                    f"You have {globals.player.gold} gold")
            L_shop_armors_armor8.pack()
    else:
        L_shop_armors_armor8 = Label(globals.frame_shop_armors_no, text="You already have Silver_Armour")
        L_shop_armors_armor8.pack()

def shop_armor_armor9():
    if globals.player.BunSamosa_Armour == False:
        if globals.player.gold > 700:
            globals.player.gold = globals.player.gold - 700
            L_shop_armors_armor9 = Label(globals.frame_shop_armors_no, text="You now have Gold_Armour\n"
                                                                    f"You now have {globals.player.gold} gold")
            L_shop_armors_armor9.pack()
            globals.player.Iron_Armour = False
            globals.player.Mythril_Armour = False
            globals.player.Orichalium_Armour = False
            globals.player.Jade_Armour = False
            globals.player.Diamond_Armour = False
            globals.player.ACM_Armour = False
            globals.player.BunSamosa_Armour = False
            globals.player.Gold_Armour=True
            globals.player.Silver_Armour =False
        else:
            L_shop_armors_armor9 = Label(globals.frame_shop_armors_no, text="You don't have enough gold.\n"
                                                                    f"You have {globals.player.gold} gold")
            L_shop_armors_armor9.pack()
    else:
        L_shop_armors_armor9 = Label(globals.frame_shop_armors_no, text="You already have Gold_Armour")
        L_shop_armors_armor9.pack()

def shop_armor_to_main():
    globals.frame_shop_armors_no.destroy()
    globals.rooms.shop()

def shop_armor_to_main():
    globals.frame_shop_armors_no.destroy()
    globals.rooms.shop()