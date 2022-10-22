from tkinter import *

import modules.globalGameAttributes as globals

class UIManager:
    def __init__(self):
        pass

    def showMainWindow(self):
        inventory_button=Button(text="inventory",command=globals.inventory.inventory)
        inventory_button.pack(side=BOTTOM)
        globals.root.title("The Quest")
        globals.frame1 = Frame(globals.root, padx=50, pady=50)
        globals.frame1.pack(padx=50, pady=50)
        globals.root.geometry("500x500")
        Label(globals.frame1, text="Welcome to The Quest!!\nStory...\nIntro").pack()
        Button(globals.frame1, text='Next', command=lambda: globals.gameFunctions.get_room()).pack()
        globals.root.mainloop()

    def switch_room(self, new_room):
        globals.frame1.destroy()
        func = getattr(globals.rooms, new_room)
        func()

    def show_you_died(self):
        frame_you_died = Frame(globals.root).pack()
        Label(globals.frame_monster_attack_1, text=f"You got killed by {globals.monster}.\n"
                                                    f"You couldn't reach the final treasure.\n"
                                                    f"Better luck next time.").pack()
        Button(globals.frame_monster_attack_1, text="Quit", command=lambda: quit()).pack()
    
    def quit_screen(self):
        Label(globals.frame_monster_1, text="Game over").pack()

    def show_potion_drink_options(self):
        globals.frame_monster_attack_1.destroy()
        globals.frame_monster_potion_1 = Frame(globals.root)
        globals.frame_monster_potion_1.pack()
        Label(globals.frame_monster_potion_1, text="We have three types of potions."
                                    "Small potion that increase your HP by 30\n"
                                    "And..\n"
                                    "Ultra potion that increase your HP by 50\n"
                                    "And..\n"
                                    "Medium potion that increases your HP by 40\n"
                                    f"Your HP is {globals.player.hp}\n"
                                    f"You have {globals.player.ultra_potion} ultra potions"
                                    f" and {globals.player.potion} potions\n"
                                    f" and {globals.player.medium_potion} medium potions\n"
                                    "Which potion would you like to drink?\n").pack()
        Button(globals.frame_monster_potion_1, text="Small Potion", command=lambda: globals.potions_functions.monster_potion_1_small()).pack()
        Button(globals.frame_monster_potion_1, text="Ultra Potion", command=lambda: globals.potions_functions.monster_potion_1_ultra()).pack()
        Button(globals.frame_monster_potion_1, text="Medium Potion", command=lambda: globals.potions_functions.monster_potion_1_medium()).pack()
        Button(globals.frame_monster_potion_1, text="Next", command=lambda: self.monster_rest_to_room()).pack()

    def treasure_box(self):
        globals.frame_tb = Frame(globals.root)
        globals.frame_tb.pack()
        L_TB = Label(globals.frame_tb, text="You found a treasure box\n")
        L_TB.pack()
        L_TB_gold = Label(globals.frame_tb, text=f"You now have {globals.player.gold} gold\n")
        L_TB_gold.pack()
        B_TB = Button(globals.frame_tb, text="Next", command=lambda: self.treasure_box_exit())
        B_TB .pack()

    def treasure_box_exit(self):
        globals.frame_tb.destroy()
        globals.gameFunctions.get_room()

    def shop(self, shop_potion, shop_sword, shop_armor):
        globals.frame_shop_1 = Frame(globals.root)
        globals.frame_shop_1.pack()
        L_Shop_Wel = Label(globals.frame_shop_1, text="Welcome to the store..\nWhat would you like to buy?\n")
        L_Shop_Wel.pack()
        # store1 variable to ask user what necessity do they need to buy
        # store1 = input("1=Potion, 2=Sword, 3=Armor, 4=Exit Store\n")
        B_Shop_Potion = Button(globals.frame_shop_1, text="Potion",
                            command=lambda: shop_potion())
        B_Shop_Potion.pack()
        B_Shop_Sword = Button(globals.frame_shop_1, text="Sword",
                            command=lambda: shop_sword())
        B_Shop_Sword.pack()
        B_Shop_Armor = Button(globals.frame_shop_1, text="Armor",
                            command=lambda: shop_armor())
        B_Shop_Armor.pack()
        B_Shop_ExitStore = Button(globals.frame_shop_1, text="Exit Store", command=lambda: self.shop_exit())
        B_Shop_ExitStore.pack()
        # if invalid input..

        # If user wants to buy potions

        # If user wants to buy swords

        # # If user wants to exit the store.
        # if int(store1) == 4:
        #     typing("Leaving the store..")


    def shop_exit(self):
        # L_shop_exit = Label(frame_shop_1, text="Leaving shop...")
        # L_shop_exit.pack()
        # time.sleep(2)
        globals.frame_shop_1.destroy()
        globals.gameFunctions.get_room()

    def monster(self, fight_monster):
        globals.frame_monster_1 = Frame(globals.root)
        globals.frame_monster_1.pack()
        L_monster_Wel = Label(globals.frame_monster_1, text="You have to fight a monster.")
        L_monster_Wel.pack()
        L_m_intro = Label(globals.frame_monster_1, text=f"You have to face {globals.monster}\n"
                                                        "The match starts. You get the first chance\n")
        L_m_intro.pack()
        fight_monster()

    def bossmonster(self, fight_monster):
        globals.frame_monster_1 = Frame(globals.root)
        globals.frame_monster_1.pack()
        L_monster_Wel = Label(globals.frame_monster_1, text="You have to fight a boss monster.")
        L_monster_Wel.pack()
        L_m1_intro = Label(globals.frame_monster_1, text=f"You have to face {globals.monster}\n"
                                                        "The match starts. You get the first chance\n")
        L_m1_intro.pack()
        fight_monster()
        b = Button(globals.frame1, text="Quit", command=globals.gameFunctions.quit_screen)
        b.pack()

    def monster_counterattack(self):
        L_monster_counterattack_1 = Label(globals.frame_monster_attack_1, text=f"Now {globals.monster} will take it's turn.\n")
        L_monster_counterattack_1.pack()
        if globals.player.hp < 0:
            globals.player.hp = 0
            L_monster_counterattack_result = Label(globals.frame_monster_attack_1, text=f"Your HP={globals.player.hp}\n")
            L_monster_counterattack_result.pack()
            globals.gameFunctions.you_died()
        else:
            if globals.player.hp >100 : globals.player.hp = 100 
            L_monster_counterattack_result = Label(globals.frame_monster_attack_1, text=f"Your HP={globals.player.hp}\n")
            L_monster_counterattack_result.pack()
            B_monster_attack_2 = Button(globals.frame_monster_attack_1, text="Attack", command=lambda: self.monster_counter_go_to("monster_counter_to_attack"))
            B_monster_potion_2 = Button(globals.frame_monster_attack_1, text="Potion", command=lambda: self.monster_counter_go_to("monster_counter_to_potion"))
            B_monster_attack_2.pack()
            B_monster_potion_2.pack()
    
    def monster_counter_go_to(self, next_frame):
        globals.frame_monster_attack_1.destroy()
        func = getattr(globals.monster_functions, next_frame)
        func()

    def fight_monster(self):
        globals.frame_fight_monster = Frame(globals.root)
        globals.frame_fight_monster.pack()
        L_monster_intro = Label(globals.frame_fight_monster, text=f"Your HP = {globals.player.hp}\n"
                                                        f"{globals.monster}'s HP = {globals.opp_hp}\n"
                                                        "Would you like to attack or use potion??\n")
        L_monster_intro.pack()
        B_monster_attack_1 = Button(globals.frame_fight_monster, text="Attack", command=lambda: self.fight_monster_to_monster_attack())
        B_monster_potion_1 = Button(globals.frame_fight_monster, text="Potion", command=lambda: self.fight_monster_to_monster_potion())
        B_monster_attack_1.pack()
        B_monster_potion_1.pack()

    def fight_monster_to_monster_attack(self):
        globals.frame_fight_monster.destroy()
        globals.monster_functions.monster_attack_1()

    def fight_monster_to_monster_potion(self):
        globals.frame_fight_monster.destroy()
        globals.frame_monster_1.destroy()
        globals.potions_functions.monster_potion_1()

    def monster_attack(self):
        globals.frame_monster_1.destroy()
        globals.frame_monster_attack_1 = Frame(globals.root)
        globals.frame_monster_attack_1.pack()
        L_monster_attack_1 = Label(globals.frame_monster_attack_1, text="You chose to attack.\n")
        L_monster_attack_1.pack()

        if globals.opp_hp > 0:
            L_monster_attack_result = Label(globals.frame_monster_attack_1, text=f"{globals.monster}'s HP={globals.opp_hp}\n")
            L_monster_attack_result.pack()
            globals.monster_functions.monster_counterattack_1()

        if globals.opp_hp <= 0:
            globals.opp_hp = 0
            L_monster_attack_result = Label(globals.frame_monster_attack_1, text=f"{globals.monster}'s HP={globals.opp_hp}\n"
                                                                        f"Your HP = {globals.player.hp}\n"
                                                                        f"you defeated {globals.monster}\n"
                                                                        "You have some time to rest.\n"
                                                                        "Would you like to use a potion?\n")
            L_monster_attack_result.pack()
            B__monster_attack_result_yes = Button(globals.frame_monster_attack_1, text="Yes", command=lambda: globals.potions_functions.drink_potion())
            B__monster_attack_result_no = Button(globals.frame_monster_attack_1, text="No", command=lambda: self.monster_rest_no_to_room())
            B__monster_attack_result_yes.pack()
            B__monster_attack_result_no.pack()

    def monster_rest_no_to_room(self):
        globals.frame_monster_attack_1.destroy()
        globals.gameFunctions.get_room()

    def monster_rest_to_room(self):
        globals.frame_monster_potion_1.destroy()
        globals.gameFunctions.get_room()