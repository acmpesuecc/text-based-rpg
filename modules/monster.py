import random

import modules.globalGameAttributes as globals

def monster_counterattack_1():
    globals.opp_attack = random.randint(((globals.m - 1) * 10), (globals.m * 10))
    globals.player.hp = globals.player.hp - globals.opp_attack

    if globals.player.Iron_Armour == True:
        globals.player.hp = globals.player.hp + 10
    elif globals.player.Mythril_Armour == True:
        globals.player.hp = globals.player.hp + 20
    elif globals.player.Orichalium_Armour == True:
        globals.player.hp = globals.player.hp + 30

    globals.uiManager.monster_counterattack()

def monster_attack_1():
    userattack = random.randint(40, 70)
    globals.opp_hp = globals.opp_hp - userattack
    if globals.player.Iron_Sword == True:
        globals.opp_hp = globals.opp_hp - 20
    elif globals.player.Mythril_Sword == True:
        globals.opp_hp = globals.opp_hp - 30
    elif globals.player.Orichalium_Sword == True:
        globals.opp_hp = globals.opp_hp - 40

    globals.uiManager.monster_attack() 

def fight_monster():
    globals.uiManager.fight_monster()