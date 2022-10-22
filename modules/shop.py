def shop_Potion():
    global root
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
    global root
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
    global root
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
    global root
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
    global root
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
    global root
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
    global root
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
    global root
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
    global root
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
    global root
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
    global root
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
                                                            "Gold_Armour costs 700 gold and increases your attack by 70\n" )
         

    L_Shop_armor_Y_info.pack()

    B_Shop_armor_Yes = Button(
    frame_shop_armor_yes, text="Next", command=lambda: shop_armor_yestono())
    B_Shop_armor_Yes.pack()


def shop_armor_yestono():
    frame_shop_armor_yes.destroy()
    shop_armor_no()


def shop_armor_no():
    global root
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
            L_shop_armors_armor2 = Label(frame_shop_armors_no, text="You now have Mythril_Armour\n"
                                                                    f"You now have {gold} gold")
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