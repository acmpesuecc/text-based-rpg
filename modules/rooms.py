import random

import modules.globalGameAttributes as globals
from modules.shop import *
from modules.monster import *

def treasure_box():
    prize = random.randint(2, 7)
    globals.player.gold = globals.player.gold + (prize * 100)
    globals.uiManager.treasure_box()

def shop():
    globals.uiManager.shop(shop_potion, shop_sword, shop_armor)

def get_monster():
    globals.monster = random.choice(globals.monsters)
    globals.opp_hp = 100
    globals.m = globals.monsters.index(globals.monster)
    globals.uiManager.monster(fight_monster)

def get_bossmonster():
    globals.monster = random.choice(globals.bossmonsters)
    globals.opp_hp = 100
    globals.m = globals.bossmonsters.index(globals.monster)
    globals.uiManager.bossmonster(fight_monster)