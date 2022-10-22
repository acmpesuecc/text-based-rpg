import random

def get_room():
    global root
    global frame1

    rav = 1
    if (rav % 20 != 0):  # a loop to make sure that the bossmonster doesnt appear until upto 20 iterations in the game
        rav += 1
        #room = ("monster", "shop", "treasure box", "monster", "shop")
        #inside_room = random.choice(room)
        # print(inside_room)
        prob_treasure = random.random()
        if prob_treasure > 0.7:
            frame1.destroy()
            treasure_box()
        else:
            prob_mons_shop = random.random()
            if prob_mons_shop > 0.5:
                frame1.destroy()
                get_monster()
            else:
                frame1.destroy()
                shop()

    else:
        rav += 1
        frame1.destroy()
        get_bossmonster()

def you_died():
    frame_you_died = Frame(root)
    frame_you_died.pack()
    L_You_Died = Label(frame_monster_attack_1, text=f"You got killed by {monster}.\n"
                                                    f"You couldn't reach the final treasure.\n"
                                                    f"Better luck next time.")
    L_You_Died.pack()
    B_You_died = Button(frame_monster_attack_1,
                        text="Quit", command=lambda: quit())
    B_You_died.pack()


def quit():
    root.quit()


def drink_potion():
    global frame_monster_potion_1
    frame_monster_attack_1.destroy()
    frame_monster_potion_1 = Frame(root)
    frame_monster_potion_1.pack()
    L_monster_potion_info = Label(frame_monster_potion_1, text="We have three types of potions."
                                "Small potion that increase your HP by 30\n"
                                "And..\n"
                                "Ultra potion that increase your HP by 50\n"
                                "And..\n"
                                "Medium potion that increases your HP by 40\n"
                                f"Your HP is {hp}\n"
                                f"You have {ultra_potion} ultra potions"
                                f" and {potion} potions\n"
                                f" and {medium_potion} medium potions\n"
                                "Which potion would you like to drink?\n")
    L_monster_potion_info.pack()
    B_monster_potion_small = Button(
        frame_monster_potion_1, text="Small Potion", command=lambda: monster_potion_1_small())
    B_monster_potion_ultra = Button(
        frame_monster_potion_1, text="Ultra Potion", command=lambda: monster_potion_1_ultra())
    B_monster_potion_medium = Button(
        frame_monster_potion_1, text="Medium Potion", command=lambda: monster_potion_1_medium())
    B_monster_potion_medium.pack()
    B_monster_potion_small.pack()
    B_monster_potion_ultra.pack()
    B_next_room = Button(frame_monster_potion_1, text="Next",
                        command=lambda: monster_rest_to_room())
    B_next_room.pack()


def quit_screen():
    quit_scr = Label(frame_monster_1, text="Game over")
    quit_scr.pack()
