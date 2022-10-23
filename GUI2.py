from tkinter import *

import modules.globalGameAttributes as globals
import modules.gameFunctions as gameFunctions
import modules.rooms as rooms
import modules.inventory as inventory
import modules.monster as monster_functions
import modules.potions_functions as potions_functions

import modules.player as player
from modules.UIManager import *
import modules.all_potions as potions

globals.init()

globals.player = player.Player()
pt_small = potions.Small_Potion()
pt_medium = potions.Medium_Potion()
pt_ultra = potions.Ultra_Potion()
globals.player.add_item_to_inventory(pt_small, 1)
globals.player.add_item_to_inventory(pt_medium, 1)
globals.player.add_item_to_inventory(pt_ultra, 1)

globals.gameFunctions = gameFunctions
globals.rooms = rooms
globals.inventory = inventory
globals.monster_functions = monster_functions
globals.potions_functions = potions_functions

globals.uiManager = UIManager()
globals.uiManager.showMainWindow()