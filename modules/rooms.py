# treasure box room
def treasure_box():
    global root
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


def shop():
    global root
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
    frame_shop_1 = Frame(root)
    frame_shop_1.pack()
    L_Shop_Wel = Label(frame_shop_1, text="Welcome to the store..\nWhat would you like to buy?\n")
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
    B_Shop_ExitStore = Button(frame_shop_1, text="Exit Store", command=lambda: shop_exit())
    B_Shop_ExitStore.pack()
    # if invalid input..

    # If user wants to buy potions

    # If user wants to buy swords

    # # If user wants to exit the store.
    # if int(store1) == 4:
    #     typing("Leaving the store..")

def shop_exit():
    # L_shop_exit = Label(frame_shop_1, text="Leaving shop...")
    # L_shop_exit.pack()
    # time.sleep(2)
    frame_shop_1.destroy()
    get_room()