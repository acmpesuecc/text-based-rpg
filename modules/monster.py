import random

import modules.globalGameAttributes as globals

def monster_counterattack_1():
    globals.opp_attack = random.randint(((globals.m - 1) * 10), (globals.m * 10))
    globals.player.hp -= globals.opp_attack
    globals.uiManager.monster_counterattack()

def monster_attack_1():
    globals.opp_hp -= globals.player.attack
    globals.uiManager.monster_attack() 

def fight_monster():
    globals.uiManager.fight_monster()

def monster_counter_to_potion():
    globals.frame_monster_attack_1.destroy()
    globals.potions_functions.monster_potion_1()

def monster_counter_to_attack():
    globals.frame_monster_attack_1.destroy()
    monster_attack_1()