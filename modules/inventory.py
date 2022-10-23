from tkinter import *

import modules.globalGameAttributes as globals

def inventory():
    newWindow = Toplevel(globals.root)
    newWindow.title("Your inventory")
    newWindow.geometry("250x250")

    if(globals.player.weapon != ""):
        Label(newWindow,text = globals.player.weapon.name).pack()
    
    if(globals.player.armour != ""):
        Label(newWindow,text = globals.player.armour.name).pack()

    for itm in globals.player.items:
        Label(newWindow,text =f"{itm['name']} x {itm['amount']}").pack()