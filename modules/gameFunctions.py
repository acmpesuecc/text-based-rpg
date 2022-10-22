import random
import modules.globalGameAttributes as globals
from modules.potions import *

def get_room():
    rav = 1
    if (rav % 20 != 0):  # a loop to make sure that the bossmonster doesnt appear until upto 20 iterations in the game
        rav += 1
        #room = ("monster", "shop", "treasure box", "monster", "shop")
        #inside_room = random.choice(room)
        # print(inside_room)
        prob_treasure = random.random()
        if prob_treasure > 0.7:
            globals.uiManager.switch_room(globals.ROOM_TREASURE_BOX)
        else:
            prob_mons_shop = random.random()
            if prob_mons_shop > 0.5:
                globals.uiManager.switch_room(globals.ROOM_MONSTER)
            else:
                globals.uiManager.switch_room(globals.ROOM_SHOP)

    else:
        rav += 1
        globals.uiManager.switch_room(globals.ROOM_BOSSMONSTER)

def you_died():
    globals.uiManager.show_you_died()

def quit():
    globals.root.quit()


def drink_potion():
    globals.uiManager.show_potion_drink_options()

def quit_screen():
    globals.uiManager.quit_screen()
