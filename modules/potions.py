from tkinter import *

import modules.globalGameAttributes as globals

def monster_potion_1():
    globals.frame_monster_potion_1 = Frame(globals.root)
    globals.frame_monster_potion_1.pack()
    L_monster_potion_info = Label(globals.frame_monster_potion_1, text="We have three types of potions."
                                  "Small potion that increase your HP by 30\n"
                                  "And..\n"
                                  "Ultra potion that increase your HP by 50\n"
                                  "And..\n"
                                  "Medium potion that increases your HP by 40\n"
                                  f"Your HP is {globals.player.hp}\n"
                                  f"You have {globals.player.ultra_potion} ultra potions"
                                  f" and {globals.player.potion} potions\n"
                                  f" and {globals.player.medium_potion} medium potions\n"
                                  "Which potion would you like to drink?\n")
    L_monster_potion_info.pack()
    B_monster_potion_small = Button(globals.frame_monster_potion_1, text="Small Potion", command=lambda: monster_potion_1_small())
    B_monster_potion_ultra = Button(globals.frame_monster_potion_1, text="Ultra Potion", command=lambda: monster_potion_1_ultra())
    B_monster_potion_medium = Button(globals.frame_monster_potion_1, text="Medium Potion", command=lambda: monster_potion_1_medium())
    B_monster_potion_medium.pack()
    B_monster_potion_small.pack()
    B_monster_potion_ultra.pack()
    B_monster_potion_back = Button(globals.frame_monster_potion_1, text="back to battle", command=lambda: monster_potion_to_attack())
    B_monster_potion_back.pack()


def monster_potion_to_attack():
    globals.frame_monster_potion_1.destroy()
    globals.monster_functions.fight_monster()


def monster_potion_1_small():
    if globals.player.potion == 0:
        L_monster_potion_1_small = Label(globals.frame_monster_potion_1, text="You have no small potions")
        L_monster_potion_1_small.pack()
    else:
        globals.player.potion = globals.player.potion - 1
        globals.player.hp = globals.player.hp + 30
        if globals.player.hp > 100:
            globals.player.hp = 100
        L_monster_potion_1_small = Label(globals.frame_monster_potion_1, text=f"You HP is now {globals.player.hp}\n"
                                                                      f"You have {globals.player.potion} small potions remaining")
        L_monster_potion_1_small.pack()


def monster_potion_1_ultra():
    if globals.player.ultra_potion == 0:
        L_monster_potion_1_ultra = Label(globals.frame_monster_potion_1, text="You have no ultra potions")
        L_monster_potion_1_ultra.pack()
    else:
        globals.player.ultra_potion = globals.player.ultra_potion - 1
        globals.player.hp = globals.player.hp + 50
        if globals.player.hp > 100:
            globals.player.hp = 100
        L_monster_potion_1_ultra = Label(globals.frame_monster_potion_1, text=f"You HP is now {globals.player.hp}\n"
                                                                      f"You have {globals.player.ultra_potion} ultra potions remaining")
        L_monster_potion_1_ultra.pack()


def monster_potion_1_medium():
    if globals.player.medium_potion == 0:
        L_monster_potion_1_medium = Label(globals.frame_monster_potion_1, text="You have no medium potions")
        L_monster_potion_1_medium.pack()
    else:
        globals.player.medium_potion = globals.player.medium_potion - 1
        globals.player.hp = globals.player.hp + 40
        if globals.player.hp > 100:
            globals.player.hp = 100
        L_monster_potion_1_medium = Label(globals.frame_monster_potion_1, text=f"You HP is now {globals.player.hp}\n"
                                          f"You have {globals.player.medium_potion} medium potions remaining")
        L_monster_potion_1_medium.pack()