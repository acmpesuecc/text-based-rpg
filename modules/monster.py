def monster_potion_1():
    global root
    global frame_monster_potion_1
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
    B_monster_potion_small = Button(frame_monster_potion_1, text="Small Potion", command=lambda: monster_potion_1_small())
    B_monster_potion_ultra = Button(frame_monster_potion_1, text="Ultra Potion", command=lambda: monster_potion_1_ultra())
    B_monster_potion_medium = Button(frame_monster_potion_1, text="Medium Potion", command=lambda: monster_potion_1_medium())
    B_monster_potion_medium.pack()
    B_monster_potion_small.pack()
    B_monster_potion_ultra.pack()
    B_monster_potion_back = Button(frame_monster_potion_1, text="back to battle", command=lambda: monster_potion_to_attack())
    B_monster_potion_back.pack()


def monster_potion_to_attack():
    frame_monster_potion_1.destroy()
    fight_monster()


def monster_potion_1_small():
    global potion
    global hp
    if potion == 0:
        L_monster_potion_1_small = Label(frame_monster_potion_1, text="You have no small potions")
        L_monster_potion_1_small.pack()
    else:
        potion = potion - 1
        hp = hp + 30
        if hp > 100:
            hp = 100
        L_monster_potion_1_small = Label(frame_monster_potion_1, text=f"You HP is now {hp}\n"
                                                                      f"You have {potion} small potions remaining")
        L_monster_potion_1_small.pack()


def monster_potion_1_ultra():
    global ultra_potion
    global hp
    if ultra_potion == 0:
        L_monster_potion_1_ultra = Label(frame_monster_potion_1, text="You have no ultra potions")
        L_monster_potion_1_ultra.pack()
    else:
        ultra_potion = ultra_potion - 1
        hp = hp + 50
        if hp > 100:
            hp = 100
        L_monster_potion_1_ultra = Label(frame_monster_potion_1, text=f"You HP is now {hp}\n"
                                                                      f"You have {ultra_potion} ultra potions remaining")
        L_monster_potion_1_ultra.pack()


def monster_potion_1_medium():
    global medium_potion
    global hp
    if medium_potion == 0:
        L_monster_potion_1_medium = Label(frame_monster_potion_1, text="You have no medium potions")
        L_monster_potion_1_medium.pack()
    else:
        medium_potion = medium_potion - 1
        hp = hp + 40
        if hp > 100:
            hp = 100
        L_monster_potion_1_medium = Label(frame_monster_potion_1, text=f"You HP is now {hp}\n"
                                          f"You have {medium_potion} medium potions remaining")
        L_monster_potion_1_medium.pack()

def monster_counterattack_1():
    global hp
    L_monster_counterattack_1 = Label(
        frame_monster_attack_1, text=f"Now {monster} will take it's turn.\n")
    L_monster_counterattack_1.pack()
    opp_attack = random.randint(((m - 1) * 10), (m * 10))
    hp = hp - opp_attack

    if Iron_Armour == True:
        hp = hp + 10
    elif Mythril_Armour == True:
        hp = hp + 20
    elif Orichalium_Armour == True:
        hp = hp + 30

    if hp < 0:
        hp = 0
        L_monster_counterattack_result = Label(
            frame_monster_attack_1, text=f"Your HP={hp}\n")
        L_monster_counterattack_result.pack()
        you_died()


    

    else:
        if hp >100 : hp = 100 

        L_monster_counterattack_result = Label(frame_monster_attack_1, text=f"Your HP={hp}\n")

        L_monster_counterattack_result.pack()
        B_monster_attack_2 = Button(
            frame_monster_attack_1, text="Attack", command=lambda: monster_counter_to_attack())
        B_monster_potion_2 = Button(
            frame_monster_attack_1, text="Potion", command=lambda: monster_counter_to_potion())
        B_monster_attack_2.pack()
        B_monster_potion_2.pack()

def monster_counter_to_potion():
    frame_monster_attack_1.destroy()
    monster_potion_1()


def monster_counter_to_attack():
    frame_monster_attack_1.destroy()
    monster_attack_1()


def monster_attack_1():
    global root
    global opp_hp
    global frame_monster_attack_1
    frame_monster_1.destroy()
    frame_monster_attack_1 = Frame(root)
    frame_monster_attack_1.pack()
    L_monster_attack_1 = Label(
        frame_monster_attack_1, text="You chose to attack.\n")
    L_monster_attack_1.pack()
    userattack = random.randint(40, 70)
    opp_hp = opp_hp - userattack
    if Iron_Sword == True:
        opp_hp = opp_hp - 20

    elif Mythril_Sword == True:
        opp_hp = opp_hp - 30

    elif Orichalium_Sword == True:
        opp_hp = opp_hp - 40

    if opp_hp > 0:
        L_monster_attack_result = Label(
            frame_monster_attack_1, text=f"{monster}'s HP={opp_hp}\n")
        L_monster_attack_result.pack()
        monster_counterattack_1()

    if opp_hp <= 0:
        opp_hp = 0
        L_monster_attack_result = Label(frame_monster_attack_1, text=f"{monster}'s HP={opp_hp}\n"
                                                                     f"Your HP = {hp}\n"
                                                                     f"you defeated {monster}\n"
                                                                     "You have some time to rest.\n"
                                                                     "Would you like to use a potion?\n")
        L_monster_attack_result.pack()
        B__monster_attack_result_yes = Button(
            frame_monster_attack_1, text="Yes", command=lambda: drink_potion())
        B__monster_attack_result_no = Button(
            frame_monster_attack_1, text="No", command=lambda: monster_rest_no_to_room())
        B__monster_attack_result_yes.pack()
        B__monster_attack_result_no.pack()


def monster_rest_no_to_room():
    frame_monster_attack_1.destroy()
    get_room()


def monster_rest_to_room():
    frame_monster_potion_1.destroy()
    get_room()

def fight_monster_to_monster_attack():
    frame_fight_monster.destroy()
    monster_attack_1()


def fight_monster_to_monster_potion():
    frame_fight_monster.destroy()
    frame_monster_1.destroy()
    monster_potion_1()


def fight_monster():
    global root
    global monster
    global opp_hp
    global hp
    global frame_fight_monster
    frame_fight_monster = Frame(root)
    frame_fight_monster.pack()
    L_monster_intro = Label(frame_fight_monster, text=f"Your HP = {hp}\n"
                                                      f"{monster}'s HP = {opp_hp}\n"
                                                      "Would you like to attack or use potion??\n")
    L_monster_intro.pack()
    B_monster_attack_1 = Button(
        frame_fight_monster, text="Attack", command=lambda: fight_monster_to_monster_attack())
    B_monster_potion_1 = Button(
        frame_fight_monster, text="Potion", command=lambda: fight_monster_to_monster_potion())
    B_monster_attack_1.pack()
    B_monster_potion_1.pack()


def get_monster():
    global root
    global m
    global opp_hp
    global monster
    global frame_monster_1
    frame_monster_1 = Frame(root)
    frame_monster_1.pack()
    L_monster_Wel = Label(frame_monster_1, text="You have to fight a monster.")
    L_monster_Wel.pack()



    monsters = ("Goblin", "Werewolf", "Basilisk", "Minotaur", "Griffin", "Dragon", "Mike", "Dave","severus","snape","orc","dark elf","Siri","GrimReaper","Dementor","UrGhast","Lola", "Cyclop","Robert","Carlson","golum","rhegar")


    monster = random.choice(monsters)
    # print(monster)
    opp_hp = 100
    if monster == "Goblin":
        m = 1
        # monster 1
        # Attack in range of 0-10
        L_m1_intro = Label(frame_monster_1, text="You have to face Goblin\n"
                                                 "The match starts. You get the first chance\n")
        L_m1_intro.pack()
        fight_monster()
        # opp_att = random.randint(0, 10)
    
    if monster == "golum":
        m = 13
        # monster 13
        # Attack in range of 10-20
        L_m2_intro = Label(frame_monster_1, text="You have to face Golum\n"
                                                 "The match starts. You get the first chance\n")
        L_m2_intro.pack()
        fight_monster()
        # opp_att = random.randint(10, 20)

    if monster == "rhegar":
        m = 14
        # monster 14
        # Attack in range of 10-20
        L_m2_intro = Label(frame_monster_1, text="You have to face Rhegar\n"
                                                 "The match starts. You get the first chance\n")
        L_m2_intro.pack()
        fight_monster()
        # opp_att = random.randint(10, 20)

    if monster == "Werewolf":
        m = 2
        # monster 2
        # Attack in range of 10-20
        L_m2_intro = Label(frame_monster_1, text="You have to face Werewolf\n"
                                                 "The match starts. You get the first chance\n")
        L_m2_intro.pack()
        fight_monster()
        # opp_att = random.randint(10, 20)

    if monster == "Basilisk":
        m = 3
        # monster 3
        # Attack in range of 20-30
        L_m3_intro = Label(frame_monster_1, text="You have to face Basilisk\n"
                                                 "The match starts. You get the first chance\n")
        L_m3_intro.pack()
        fight_monster()
        # opp_att = random.randint(20, 30)

    if monster == "Minotaur":
        m = 4
        # monster 4
        # Attack in range of 30-40
        L_m4_intro = Label(frame_monster_1, text="You have to face Minotaur\n"
                                                 "The match starts. You get the first chance\n")
        L_m4_intro.pack()
        fight_monster()
        # opp_att = random.randint(30, 40)

    if monster == "Griffin":
        m = 5
        # monster 5
        # Attack in range of 40-50
        L_m5_intro = Label(frame_monster_1, text="You have to face Griffin\n"
                                                 "The match starts. You get the first chance\n")
        L_m5_intro.pack()
        fight_monster()
        # opp_att = random.randint(40, 50)

    if monster == "Dragon":
        m = 6
        # monster 6
        # Attack in range of 50-60
        L_m6_intro = Label(frame_monster_1, text="You have to face Dragon\n"
                                                 "The match starts. You get the first chance\n")
        L_m6_intro.pack()
        fight_monster()
        # opp_att = random.randint(50, 60)

    if monster == "orc":
        m = 9
        # monster 9
        # Attack in range of 30-40
        L_m9_intro = Label(frame_monster_1, text="You have to face orc\n"
                                                 "The match starts. You get the first chance\n")
        L_m9_intro.pack()
        fight_monster()
        # opp_att = random.randint(30, 40)

    if monster == "darkelf":
        m = 10
        # monster 10
        # Attack in range of 60-70
        L_m10_intro = Label(frame_monster_1, text="You have to face Dark Elf\n"
                            "The match starts. You get the first chance\n")
        L_m10_intro.pack()
        fight_monster()
        # opp_att = random.randint(60, 70)

    if monster == "Mike":
        m = 7
        # monster 7
        # Attack in range of 60-70
        L_m7_intro = Label(frame_monster_1, text="You have to face Mike\n"
                                                 "The match starts. You get the first chance\n")
        L_m7_intro.pack()
        fight_monster()
        # opp_att = random.randint(60, 70)

    if monster == "Dave":
        m = 8
        # monster 8
        # Attack in range of 70-80
        L_m8_intro = Label(frame_monster_1, text="You have to face Dave\n"
                                                 "The match starts. You get the first chance\n")
        L_m8_intro.pack()
        fight_monster()
        # opp_att = random.randint(70, 80)
    if monster == "severus":
        m = 11
        # monster 11
        # Attack in range of 80-90
        L_m1_intro = Label(frame_monster_1, text="You have to face severus\n"
                                                 "The match starts. You get the first chance\n")
        L_m1_intro.pack()
        fight_monster()
        # opp_att = random.randint(80,90)
    if monster == "snape":
        m = 12
        # monster 12
        # Attack in range of 90-100
        L_m1_intro = Label(frame_monster_1, text="You have to face snape\n"
                                                 "The match starts. You get the first chance\n")
        L_m1_intro.pack()
        fight_monster()
        # opp_att = random.randint(90,100)
    if monster == "Lola":
        m = 19
        # monster 19
        # Attack in range of 40-70
        L_m19_intro = Label(frame_monster_1, text="You have to face Lola\n"
                            "The match starts. You get the first chance\n")
        L_m19_intro.pack()
        fight_monster()
        # opp_att = random.randint(50, 60)

    if monster == "Cyclop":
        m = 20
        # monster 20
        # Attack in range of 50-70
        L_m20_intro = Label(frame_monster_1, text="You have to face Cyclop\n"
                            "The match starts. You get the first chance\n")
        L_m20_intro.pack()
        fight_monster()
        # opp_att = random.randint(50, 60)

    if monster == "Siri":
        m = 13
        # monster 13
        # Attack in range of 70-80
        L_m9_intro = Label(frame_monster_1, text="You have to face Siri\n"
                                                 "The match starts. You get the first chance\n")
        L_m9_intro.pack()
        fight_monster()
        # opp_att = random.randint(70, 80)
    if monster == "GrimReaper":
        m = 14
        # monster 14
        # Attack in range of 70-80
        L_m10_intro = Label(frame_monster_1, text="You have to face Dave\n"
                            "The match starts. You get the first chance\n")
        L_m10_intro.pack()
        fight_monster()
        # opp_att = random.randint(70, 80)

    if monster == "dementor":
        m = 15
        # monster 15
        # Attack in range of 70-80
        L_m10_intro = Label(frame_monster_1, text="You have to face A Dementor\n"
                            "The match starts. You get the first chance as your life\n")
        L_m10_intro.pack()
        fight_monster()
        # opp_att = random.randint(70, 80)
    if monster == "UrGhast":
        m = 16
        # monster 16
        # Attack in range of 70-80
        L_m10_intro = Label(frame_monster_1, text="You have to face UrMom (A UrGhast)\n"
                            "The match starts. You get the first chance\n")
        L_m10_intro.pack()
        fight_monster()
        # opp_att = random.randint(70, 80)
    if monster == "Robert":
        m = 17
        # monster 17
        # Attack in range of 70-80
        L_m10_intro = Label(frame_monster_1, text="You have to face Robert\n"
                            "The match starts. You get the first chance\n")
        L_m10_intro.pack()
        fight_monster()
        # opp_att = random.randint(70, 80)

    if monster == "Carlson":
        m = 18
        # monster 18
        # Attack in range of 70-80
        L_m10_intro = Label(frame_monster_1, text="You have to face Carlson\n"
                            "The match starts. You get the first chance\n")
        L_m10_intro.pack()
        fight_monster()
        # opp_att = random.randint(70, 80)

def get_bossmonster():
    global root
    global m
    global opp_hp
    global monster
    global frame_monster_1
    frame_monster_1 = Frame(root)
    frame_monster_1.pack()
    L_monster_Wel = Label(frame_monster_1, text="You have to fight a boss monster.")
    L_monster_Wel.pack()
    bossmonsters = ("Demon Slayer", "Big Tooth")
    monster = random.choice(bossmonsters)
    # print(monster)
    opp_hp = 100
    if monster == "Demon Slayer":
        m = 1
        # monster 1
        # Attack in range of 0-10
        L_m1_intro = Label(frame_monster_1, text="You have to face Demon Slayer\n"
                                                 "The match starts. You get the first chance\n")
        L_m1_intro.pack()
        fight_monster()
        # opp_att = random.randint(0, 10)

    if monster == "Big Tooth":
        m = 2
        # monster 2
        # Attack in range of 10-20
        L_m2_intro = Label(frame_monster_1, text="You have to face Big Tooth\n"
                                                 "The match starts. You get the first chance\n")
        L_m2_intro.pack()
        fight_monster()
        # opp_att = random.randint(10, 20)
    b = Button(frame1, text="Quit", command=quit_screen)
    b.pack()