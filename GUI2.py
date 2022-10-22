from tkinter import *

import modules.globalGameAttributes as globals
import modules.gameFunctions as gameFunctions
import modules.rooms as rooms
import modules.inventory as inventory
import modules.monster as monster_functions
import modules.potions as potions_functions

import modules.player as player
from modules.UIManager import *

globals.init()

globals.player = player.Player()
globals.gameFunctions = gameFunctions
globals.rooms = rooms
globals.inventory = inventory
globals.monster_functions = monster_functions
globals.potions_functions = potions_functions

globals.uiManager = UIManager()
globals.uiManager.showMainWindow()