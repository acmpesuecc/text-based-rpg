from tkinter import *

import modules.globalGameAttributes as globals
from modules.gameFunctions import *

from modules.player import *
from modules.shop import *
from modules.monster import *
from modules.inventory import *

from modules.UIManager import *

globals.init()

uiManager = UIManager(globals.root, globals.frame1)
uiManager.showMainWindow(inventory, get_room)