from tkinter import *

import modules.globalGameAttributes as globals

def inventory():
    newWindow = Toplevel(globals.root)
    newWindow.title("Your inventory")
    newWindow.geometry("250x250")
    #Label(newWindow,text ="welcome to inventory").pack()
    if(globals.player.Iron_Sword):
        iron_s_l=Label(newWindow,text ="iron sword").pack()
    if(globals.player.Mythril_Sword):
        mythril_s_l=Label(newWindow,text ="mythril sword").pack()
    if(globals.player.Orichalium_Sword):
        orichallium_s_l=Label(newWindow,text ="orichalium sword").pack()
    if(globals.player.Iron_Armour):
        iron_a_l=Label(newWindow,text ="iron armour").pack()
    if(globals.player.Mythril_Armour):
        mythril_a_l=Label(newWindow,text ="mythril armour").pack()
    if(globals.player.Orichalium_Armour):
        orichalium_a_l=Label(newWindow,text ="orichalium armour").pack()
    if(globals.player.BunSamosa_Armour):
        bun_a_l=Label(newWindow,text ="bunsamosa armour").pack()
    if(globals.player.ACM_Armour):
        acm_a_l=Label(newWindow,text ="acm armour").pack()
    if(globals.player.Silver_Armour):
        acm_a_l=Label(newWindow,text ="Silver armour").pack()
    if(globals.player.Gold_Armour):
        acm_a_l=Label(newWindow,text ="Gold armour").pack()
    if(globals.player.potion!=0):
        small_label=Label(newWindow,text =f"small potion x {globals.player.potion}").pack()
    else:
        small_label=Label(newWindow,text ="").pack()
    if(globals.player.medium_potion!=0):
        medium_label=Label(newWindow,text =f"medium potion x {globals.player.medium_potion}").pack()
    else:
        medium_label=Label(newWindow,text ="").pack()
    if(globals.player.ultra_potion!=0):
        ultra_label=Label(newWindow,text =f"ultra potion x {globals.player.ultra_potion}").pack()
    else:
        ultra_label=Label(newWindow,text ="").pack()