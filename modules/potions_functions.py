from tkinter import *

import modules.globalGameAttributes as globals
import modules.all_potions as potions

def monster_potion_1():
    pt_small = potions.Small_Potion()
    pt_medium = potions.Medium_Potion()
    pt_ultra = potions.Ultra_Potion()

    globals.frame_monster_potion_1 = Frame(globals.root)
    globals.frame_monster_potion_1.pack()
    Label(globals.frame_monster_potion_1, text="We have three types of potions."
                                  f"{pt_small.name} that increase your HP by {pt_small.heal}\n"
                                  "And..\n"
                                  f"{pt_ultra.name} that increase your HP by {pt_ultra.heal}\n"
                                  "And..\n"
                                  f"{pt_medium.name} that increases your HP by {pt_medium.heal}\n"
                                  f"Your HP is {globals.player.hp}\n"
                                  f"You have {globals.player.get_item_amount(pt_ultra.name)} x {pt_ultra.name}"
                                  f" and {globals.player.get_item_amount(pt_small.name)} x {pt_small.name}\n"
                                  f" and {globals.player.get_item_amount(pt_medium.name)} x {pt_medium.name}\n"
                                  "Which potion would you like to drink?\n").pack()
    Button(globals.frame_monster_potion_1, text=pt_small.name, command=lambda: drink_potion(potions.Small_Potion)).pack()
    Button(globals.frame_monster_potion_1, text=pt_ultra.name, command=lambda: drink_potion(potions.Ultra_Potion)).pack()
    Button(globals.frame_monster_potion_1, text=pt_medium.name, command=lambda: drink_potion(potions.Medium_Potion)).pack()

    Button(globals.frame_monster_potion_1, text="back to battle", command=lambda: monster_potion_to_attack()).pack()

def monster_potion_to_attack():
    globals.frame_monster_potion_1.destroy()
    globals.monster_functions.fight_monster()

def drink_potion(potion_type):
    potion = potion_type()

    if globals.player.get_item_amount(potion.name) == 0:
        Label(globals.frame_monster_potion_1, text=f"You have no {potion.name} in your inventory").pack()
    else:
        globals.player.remove_item_from_inventory(potion.name, 1)
        globals.player.hp = globals.player.hp + potion.heal
        if globals.player.hp > globals.player.max_hp:
            globals.player.hp = globals.player.max_hp

        Label(globals.frame_monster_potion_1, text=f"You HP is now {globals.player.hp}\n"
                                                f"You have {globals.player.get_item_amount(potion.name)} x {potion.name} remaining").pack()