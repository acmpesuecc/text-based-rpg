from tkinter import *

def init():
    # vars
    global player
    global root
    global frame1
    global which_potion
    global uiManager
    global gameFunctions
    global rooms
    global frame_monster_attack_1
    global frame_monster_potion_1
    global frame_monster_1
    global frame_fight_monster
    global frame_tb
    global frame_shop_1
    global frame_shop_potion
    global frame_shop_potion_no
    global frame_shop_potion_yes
    global frame_shop_potion_small
    global frame_shop_potion_ultra
    global frame_shop_potion_medium
    global frame_shop_sword
    global frame_shop_sword_yes
    global frame_shop_swords_no
    global frame_shop_armor
    global frame_shop_armor_yes
    global frame_shop_armors_no
    global m
    global opp_hp
    global opp_attack
    global monster
    global monsters
    global bossmonsters
    global inventory
    global monster_functions
    global potions_functions


    # constants
    global ROOM_TREASURE_BOX
    global ROOM_MONSTER
    global ROOM_SHOP
    global ROOM_BOSSMONSTER


    # inits
    player = ""
    root = Tk()
    which_potion = 0
    frame1 = ""
    uiManager = ""
    gameFunctions = ""
    rooms = ""
    frame_monster_attack_1 = ""
    frame_monster_potion_1 = ""
    frame_monster_1 = ""
    frame_fight_monster = ""
    frame_tb = ""
    frame_shop_1 = ""
    frame_shop_potion = ""
    frame_shop_potion_no = ""
    frame_shop_potion_yes = ""
    frame_shop_potion_small = ""
    frame_shop_potion_ultra = ""
    frame_shop_potion_medium = ""
    frame_shop_sword = ""
    frame_shop_sword_yes = ""
    frame_shop_swords_no = ""
    frame_shop_armor = ""
    frame_shop_armor_yes = ""
    frame_shop_armors_no = ""
    m = 0
    opp_hp = 0
    opp_attack = 0
    monster = ""
    monsters = ("Goblin", "Werewolf", "Basilisk", "Minotaur", "Griffin", "Dragon", "Mike", "Dave","severus","snape","orc","dark elf","Siri","GrimReaper","Dementor","UrGhast","Lola", "Cyclop","Robert","Carlson","golum","rhegar")
    bossmonsters = ("Demon Slayer", "Big Tooth")
    inventory = ""
    monster_functions = ""
    potions_functions = ""


    ROOM_TREASURE_BOX = "treasure_box"
    ROOM_MONSTER = "get_monster"
    ROOM_SHOP = "shop"
    ROOM_BOSSMONSTER = "get_bossmonster"