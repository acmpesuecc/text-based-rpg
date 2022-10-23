
from tkinter import *

import modules.globalGameAttributes as globals
import modules.all_weapons as weapons
import modules.all_potions as potions
import modules.all_armours as armours

def shop_potion():
    pt_small = potions.Small_Potion()
    pt_medium = potions.Medium_Potion()
    pt_ultra = potions.Ultra_Potion()

    globals.frame_shop_1.destroy()
    globals.frame_shop_potion = Frame(globals.root).pack()
    Label(globals.frame_shop_potion, text=f"You currently have {globals.player.get_item_amount(pt_small.name)} x {pt_small.name} and {globals.player.get_item_amount(pt_ultra.name)} x {pt_ultra.name} with you.\n"
                                                    f"We have 3 types of potion.\n"
                                                    f"{pt_small.name}, {pt_ultra.name} and {pt_medium.name}\n"
                                                    f"Would you like to know more about them?\n").pack()
    Button(globals.frame_shop_potion, text="Yes", command=lambda: shop_potion_yes()).pack(side=BOTTOM)
    Button(globals.frame_shop_potion, text="No", command=lambda: shop_potion_no()).pack(side=BOTTOM)

def shop_potion_no():
    pt_small = potions.Small_Potion()
    pt_medium = potions.Medium_Potion()
    pt_ultra = potions.Ultra_Potion()

    globals.frame_shop_potion.destroy()
    globals.frame_shop_potion_no = Frame(globals.root).pack()
    Label(globals.frame_shop_potion_no, text="Okay then..\n"
                                            "Which potion would you like to buy?").pack()
    Button(globals.frame_shop_potion_no, text=pt_small.name, command=lambda: shop_potion_how_many(potions.Small_Potion)).pack()
    Button(globals.frame_shop_potion_no, text=pt_ultra.name, command=lambda: shop_potion_how_many(potions.Ultra_Potion)).pack()
    Button(globals.frame_shop_potion_no, text=pt_medium.name, command=lambda: shop_potion_how_many(potions.Medium_Potion)).pack()

def shop_potion_yes():
    pt_small = potions.Small_Potion()
    pt_medium = potions.Medium_Potion()
    pt_ultra = potions.Ultra_Potion()

    globals.frame_shop_potion.destroy()
    globals.frame_shop_potion_yes = Frame(globals.root).pack()
    Label(globals.frame_shop_potion_yes, text=f"{pt_small.name} that costs {pt_small.gold_cost} gold will increase your HP by {pt_small.heal}\n"
                                            "And..\n"
                                            f"{pt_ultra.name} that costs {pt_ultra.gold_cost} gold will increase your HP by {pt_ultra.heal}\n"
                                            "And..\n"
                                            f"{pt_medium.name} that costs {pt_medium.gold_cost} gold will increase your HP by {pt_medium.heal}").pack()
    Button(globals.frame_shop_potion_yes, text="Next", command=lambda: shop_potion_yestono()).pack()

def shop_potion_yestono():
    globals.frame_shop_potion_yes.destroy()
    shop_potion_no()

def shop_potion_how_many(potion):
    pt = potion()

    globals.frame_shop_potion_no.destroy()
    globals.frame_shop_potion_hm = Frame(globals.root).pack()
    Label(globals.frame_shop_potion_hm, text=f"How many {pt.name} would you like to buy?\n"
                                                f"Cost={pt.gold_cost} gold\n"
                                                f"You have {globals.player.gold} gold").pack()

    Button(globals.frame_shop_potion_hm, text="Buy", command=lambda: shop_potion_buy(pt)).pack()
    Button(globals.frame_shop_potion_hm, text="Back", command=lambda: shop_potions_hm_to_main()).pack(side=BOTTOM)

def shop_potion_buy(potion):
    if globals.player.gold - potion.gold_cost < 0:
        Label(globals.frame_shop_potion_hm, text="You don't have enough gold.\n"
                                                "Let's shop for something else..\n").pack()
    else:
        globals.player.add_to_inventory(potion, 1)
        globals.player.gold = globals.player.gold - potion.gold_cost
        Label(globals.frame_shop_potion_hm, text=(f"You now have {globals.player.gold} gold with you\n"
                                                    f"You now have {globals.player.get_item_amount(potion.name)} {potion.name} with you\n"
                                                    "Let's continue shopping..")).pack()

def shop_potions_hm_to_main():
    globals.frame_shop_potion_hm.destroy()
    globals.rooms.shop()

def shop_sword():
    iron_sword = weapons.Iron_Sword()
    mythril_sword = weapons.Mythril_Sword()
    orichalium_sword = weapons.Orichalium_Sword()

    globals.frame_shop_1.destroy()
    globals.frame_shop_sword = Frame(globals.root).pack()
    if globals.player.weapon != "":
        Label(globals.frame_shop_sword, text=f"Right now, you have {globals.player.weapon.name}").pack()

    Label(globals.frame_shop_sword, text="We have 3 types of swords..\n"
                                        f"{iron_sword.name}, {mythril_sword.name} and {orichalium_sword.name}\n"
                                        "Would you like to know more about them?\n").pack()
    Button(globals.frame_shop_sword, text="Yes",command=lambda: shop_sword_yes()).pack()
    Button(globals.frame_shop_sword, text="No",command=lambda: shop_sword_no()).pack()

def shop_sword_yes():
    iron_sword = weapons.Iron_Sword()
    mythril_sword = weapons.Mythril_Sword()
    orichalium_sword = weapons.Orichalium_Sword()

    globals.frame_shop_sword.destroy()
    globals.frame_shop_sword_yes = Frame(globals.root).pack()
    Label(globals.frame_shop_sword_yes, text=f"{iron_sword.name} costs {iron_sword.gold_cost} gold and increases your attack by {iron_sword.attack}\n"
                                f"{mythril_sword.name} costs {mythril_sword.gold_cost} gold and increases your attack by {mythril_sword.attack}\n"
                                f"{orichalium_sword.name} costs {orichalium_sword.gold_cost} gold and increases your attack by {orichalium_sword.attack}\n").pack()
    Button(globals.frame_shop_sword_yes, text="Next", command=lambda: shop_sword_yestono()).pack()

def shop_sword_yestono():
    globals.frame_shop_sword_yes.destroy()
    shop_sword_no()


def shop_sword_no():
    globals.frame_shop_sword.destroy()
    globals.frame_shop_swords_no = Frame(globals.root).pack()
    Label(globals.frame_shop_swords_no,text="Which sword would you like to buy?\n").pack()
    Button(globals.frame_shop_swords_no, text="Iron Sword", command=lambda: shop_buy_sword(weapons.Iron_Sword)).pack()
    Button(globals.frame_shop_swords_no, text="Mythril Sword", command=lambda: shop_buy_sword(weapons.Mythril_Sword)).pack()
    Button(globals.frame_shop_swords_no, text="Orichalium Sword", command=lambda: shop_buy_sword(weapons.Orichalium_Sword)).pack()
    Button(globals.frame_shop_swords_no, text="back", command=lambda: shop_sword_to_main()).pack(side=BOTTOM)

def shop_buy_sword(sword):
    wp = sword()

    if globals.player.weapon == "" or globals.player.weapon.name != wp.name:
        if globals.player.gold > wp.gold_cost:
            globals.player.gold -= wp.gold_cost
            globals.player.change_weapon(wp)

            Label(globals.frame_shop_swords_no, text=f"You now have {wp.name}\n"
                                                f"You now have {globals.player.gold} gold").pack()
        else:
            Label(globals.frame_shop_swords_no, text="You don't have enough gold.\n"
                                                    f"You have {globals.player.gold} gold").pack()
    else:
        Label(globals.frame_shop_swords_no, text=f"You already have {wp.name}").pack()

def shop_sword_to_main():
    globals.frame_shop_swords_no.destroy()
    globals.rooms.shop()


def shop_armor():
    acm_armour = armours.ACM_Armour()
    bunsamosa_armour = armours.BunSamosa_Armour()
    diamond_armour = armours.Diamond_Armour()
    gold_armour = armours.Gold_Armour()
    iron_armour = armours.Iron_Armour()
    jade_armour = armours.Jade_Armour()
    mythril_armour = armours.Mythril_Armour()
    orichalium_armour = armours.Orichalium_Armour()
    silver_armour = armours.Silver_Armour()

    globals.frame_shop_1.destroy()
    globals.frame_shop_armor = Frame(globals.root).pack()

    if globals.player.armour != "":
        Label(globals.frame_shop_armor, text=f"Right now, you have {globals.player.armour.name}").pack()

    Label(globals.frame_shop_armor, text="We have 9 types of armors..\n"
                                        f"{iron_armour.name}, {mythril_armour.name}, {orichalium_armour.name}, {bunsamosa_armour.name}, {silver_armour.name}, {gold_armour.name}, {diamond_armour.name}, {jade_armour.name} and {acm_armour.name}\n"
                                        "Would you like to know more about them?\n").pack()
    Button(globals.frame_shop_armor, text="Yes",command=lambda: shop_armor_yes()).pack()
    Button(globals.frame_shop_armor, text="No",command=lambda: shop_armor_no()).pack()

def shop_armor_yes():
    acm_armour = armours.ACM_Armour()
    bunsamosa_armour = armours.BunSamosa_Armour()
    diamond_armour = armours.Diamond_Armour()
    gold_armour = armours.Gold_Armour()
    iron_armour = armours.Iron_Armour()
    jade_armour = armours.Jade_Armour()
    mythril_armour = armours.Mythril_Armour()
    orichalium_armour = armours.Orichalium_Armour()
    silver_armour = armours.Silver_Armour()

    globals.frame_shop_armor.destroy()
    globals.frame_shop_armor_yes = Frame(globals.root).pack()
    Label(globals.frame_shop_armor_yes, text=f"{iron_armour.name} costs {iron_armour.gold_cost} gold and increases your attack by {iron_armour.attack}\n"
                                            f"{mythril_armour.name} costs {mythril_armour.gold_cost} gold and increases your attack by {mythril_armour.attack}\n"
                                            f"{orichalium_armour.name} costs {orichalium_armour.gold_cost} gold and increases your attack by {orichalium_armour.attack}\n"
                                            f"{jade_armour.name} costs {jade_armour.gold_cost} gold and increases your hp by {jade_armour.hp}\n"
                                            f"{diamond_armour.name} costs {diamond_armour.gold_cost} gold and increases your hp by {diamond_armour.hp}\n"
                                            f"{bunsamosa_armour.name} costs {bunsamosa_armour.gold_cost} gold and increases your attack by {bunsamosa_armour.attack}\n"
                                            f"{acm_armour.name} costs {acm_armour.gold_cost} gold and increases your attack by {acm_armour.attack}\n"
                                            f"{silver_armour.name} costs {silver_armour.gold_cost} gold and increases your attack by {silver_armour.attack}\n"
                                            f"{gold_armour.name} costs {gold_armour.gold_cost} gold and increases your attack by {gold_armour.attack}\n" ).pack()

    Button(globals.frame_shop_armor_yes, text="Next", command=lambda: shop_armor_yestono()).pack()


def shop_armor_yestono():
    globals.frame_shop_armor_yes.destroy()
    shop_armor_no()


def shop_armor_no():
    acm_armour = armours.ACM_Armour()
    bunsamosa_armour = armours.BunSamosa_Armour()
    diamond_armour = armours.Diamond_Armour()
    gold_armour = armours.Gold_Armour()
    iron_armour = armours.Iron_Armour()
    jade_armour = armours.Jade_Armour()
    mythril_armour = armours.Mythril_Armour()
    orichalium_armour = armours.Orichalium_Armour()
    silver_armour = armours.Silver_Armour()

    globals.frame_shop_armor.destroy()
    globals.frame_shop_armors_no = Frame(globals.root).pack()
    Label(globals.frame_shop_armors_no,text="Which armor would you like to buy?\n").pack()

    Button(globals.frame_shop_armors_no, text=iron_armour.name, command=lambda: shop_armor_buy(armours.Iron_Armour)).pack()
    Button(globals.frame_shop_armors_no, text=mythril_armour.name, command=lambda: shop_armor_buy(armours.Mythril_Armour)).pack()
    Button(globals.frame_shop_armors_no, text=orichalium_armour.name, command=lambda: shop_armor_buy(armours.Orichalium_Armour)).pack()
    Button(globals.frame_shop_armors_no, text=jade_armour.name, command=lambda: shop_armor_buy(armours.Jade_Armour)).pack()
    Button(globals.frame_shop_armors_no, text=diamond_armour.name, command=lambda: shop_armor_buy(armours.Diamond_Armour)).pack()    
    Button(globals.frame_shop_armors_no, text=bunsamosa_armour.name, command=lambda: shop_armor_buy(armours.BunSamosa_Armour)).pack()
    Button(globals.frame_shop_armors_no, text=acm_armour.name, command=lambda: shop_armor_buy(armours.ACM_Armour)).pack()
    Button(globals.frame_shop_armors_no, text=silver_armour.name, command=lambda: shop_armor_buy(armours.Silver_Armour)).pack()
    Button(globals.frame_shop_armors_no, text=gold_armour.name, command=lambda: shop_armor_buy(armours.Gold_Armour)).pack()

    Button(globals.frame_shop_armors_no, text="back", command=lambda: shop_armor_to_main()).pack(side=BOTTOM)

def shop_armor_buy(armour_type):
    armour = armour_type()

    if globals.player.armour == "" or globals.player.armour.name != armour.name:
        if globals.player.gold > armour.gold_cost:
            globals.player.gold -= armour.gold_cost
            globals.player.change_armour(armour)
            
            Label(globals.frame_shop_armors_no, text=f"You now have {armour.name}\n"
                                                    f"You now have {globals.player.gold} gold").pack()
        else:
            Label(globals.frame_shop_armors_no, text="You don't have enough gold.\n"
                                                    f"You have {globals.player.gold} gold").pack()
    else:
        Label(globals.frame_shop_armors_no, text=f"You already have {armour.name}").pack()

def shop_armor_to_main():
    globals.frame_shop_armors_no.destroy()
    globals.rooms.shop()