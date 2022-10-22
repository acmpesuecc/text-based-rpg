from tkinter import *

def inventory():
    global root
    global Iron_Sword 
    global Mythril_Sword 
    global Orichalium_Sword 
    global Iron_Armour 
    global Mythril_Armour
    global Orichalium_Armour 
    global potion 
    global ultra_potion 
    global medium_potion
    global BunSamosa_Armour
    global ACM_Armour
    global Silver_Armour
    global Gold_Armour 
    newWindow = Toplevel(root)
 
    newWindow.title("Your inventory")
 
    newWindow.geometry("250x250")
    #Label(newWindow,text ="welcome to inventory").pack()

    if(Iron_Sword):
        iron_s_l=Label(newWindow,text ="iron sword").pack()
    if(Mythril_Sword):
        mythril_s_l=Label(newWindow,text ="mythril sword").pack()
    if(Orichalium_Sword):
        orichallium_s_l=Label(newWindow,text ="orichalium sword").pack()
    if(Iron_Armour):
        iron_a_l=Label(newWindow,text ="iron armour").pack()
    if(Mythril_Armour):
        mythril_a_l=Label(newWindow,text ="mythril armour").pack()
    if(Orichalium_Armour):
        orichalium_a_l=Label(newWindow,text ="orichalium armour").pack()
    if(BunSamosa_Armour):
        bun_a_l=Label(newWindow,text ="bunsamosa armour").pack()
    if(ACM_Armour):
        acm_a_l=Label(newWindow,text ="acm armour").pack()
    if(Silver_Armour):
        acm_a_l=Label(newWindow,text ="Silver armour").pack()
    if(Gold_Armour):
        acm_a_l=Label(newWindow,text ="Gold armour").pack()
    if(potion!=0):
        small_label=Label(newWindow,text =f"small potion x {potion}").pack()
    else:
        small_label=Label(newWindow,text ="").pack()
    if(medium_potion!=0):
        medium_label=Label(newWindow,text =f"medium potion x {medium_potion}").pack()
    else:
        medium_label=Label(newWindow,text ="").pack()
    if(ultra_potion!=0):
        ultra_label=Label(newWindow,text =f"ultra potion x {ultra_potion}").pack()
    else:
        ultra_label=Label(newWindow,text ="").pack()