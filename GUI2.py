from tkinter import *
import random
gold = 500  # used in store to buy items
hp = 100  # user's hp
opp_hp = 100  # monster's hp
extra_hp = 0  # extra opponent hp for boss round
Iron_Sword = False  # increases attack by 20
Mythril_Sword = False  # increases attack by 30
Orichalium_Sword = False  # increases attack by 40
Iron_Armour = False  # decreases opp_att by 10
Mythril_Armour = False  # decreases opp_att by 20
Orichalium_Armour = False  # decereases opp_att by 30
potion = 1  # increases hp by 30. Cost=300 gold
ultra_potion = 1  # increases hp by 50. Cost=600 gold
which_potion = 0  # variable that lets you select the potion that you want to take.
room = ("shopping")
# def fight_1():

n = 0
while n != 6:
    inside_room = random.choice(room)

    # if user has to face a monster
    if hp == 0:
        break
    elif inside_room == "monster":
        L_monster_intro = Label(root, text="You have to face a monster...\n")
        L_monster_intro.pack()
        monsters = ("m1", "m2", "m3", "m4", "m5", "m6")
        monster = random.choice(monsters)

        if monster == "m1":
            m = 1
            # monster 1
            # Attack in range of 0-10
            L_monster_1 = Label(root, text=("You have to face monster 1\n"))
            L_monster_1.pack()
            opp_att = random.randint(0, 10)
            fight()
            potion_time()
        #
        # if monster == "m2":
        #     m = 2
        #     # monster 2
        #     # Attack in range of 10-20
        #     typing("You have to face monster 2\n")
        #     opp_att = random.randint(10, 20)
        #     fight()
        #     potion_time()
        #
        # if monster == "m3":
        #     m = 3
        #     # monster 3
        #     # Attack in range of 20-30
        #     typing("You have to face monster 3\n")
        #     opp_att = random.randint(20, 30)
        #     fight()
        #     potion_time()
        #
        # if monster == "m4":
        #     m = 4
        #     # monster 4
        #     # Attack in range of 30-40
        #     typing("You have to face monster 4\n")
        #     opp_att = random.randint(30, 40)
        #     fight()
        #     potion_time()
        #
        # if monster == "m5":
        #     m = 5
        #     # monster 5
        #     # Attack in range of 40-50
        #     typing("You have to face monster 5\n")
        #     opp_att = random.randint(40, 50)
        #     fight()
        #     potion_time()
        #
        # if monster == "m6":
        #     m = 6
        #     # monster 6
        #     # Attack in range of 50-60
        #     typing("You have to face monster 6\n")
        #     opp_att = random.randint(50, 60)
        #     fight()
        #     potion_time()

        n = n + 1

    # if user gets a treasure box
    if hp == 0:
        break
    elif inside_room == "treasure box":
        typing("You got a treasure box\n")

        prize = random.randint(2, 7)
        gold = gold + (prize * 100)

        typing(f"You now have {gold} gold\n")
        n = n + 1

    # if user encounters a shop
    if hp == 0:
        break
    elif inside_room == "shop":
        typing("You reached a shop..\n")
        typing(f"You have {gold} gold with you. Would you like to the enter the shop?\n")

        s = ''

        # for incorrect inputs
        while s != "YES" or s != "NO" or s != "yes" or s != "no" or s != "Yes" or s != "No":
            s = input("Yes or No?")
            if s == "YES" or s == "Yes" or s == "yes" or s == "NO" or s == "no" or s == "No":
                break
            else:
                pass
            typing("Incorrect input.Try again\n")

        # whether player wants to enter the shop or not...
        if s == "YES" or s == "Yes" or s == "yes":
            typing("Entering the shop..\n")
            shopping()
        elif s == "NO" or s == "no" or s == "No":
            typing("Leaving the store..\n")
        n = n + 1

# If lose anytime in between the game.
if hp == 0:
    typing("You lose. Better luck next time....\n")

root = Tk()
fight_info = Label(root, text=)
root.mainloop()