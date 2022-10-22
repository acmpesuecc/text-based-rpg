
class Player:

    def __init__(self):
        self.gold = 1500  # used in store to buy items
        self.hp = 100  # user's hp
        self.opp_hp = 100  # monster's hp
        self.extra_hp = 0  # extra opponent hp for boss round
        
        self.Iron_Sword = False  # increases attack by 20
        self.Mythril_Sword = False  # increases attack by 30
        self.Orichalium_Sword = False  # increases attack by 40
        self.Iron_Armour = False  # decreases opp_att by 10
        self.Mythril_Armour = False  # decreases opp_att by 20
        self.Orichalium_Armour = False  # decreases opp_att by 30

        self.BunSamosa_Armour= False #decreases opp_att by 50
        self.ACM_Armour= False #decreases opp_att by 60
        self.Jade_Armour = False # increases hp by 10
        self.Diamond_Armour = False #increases hp by 20
        self.Silver_Armour = False #decreaases Opp_ATT by 40
        self.Gold_Armour= False #decreases opp_att by 70

        self.potion = 1  # increases hp by 30. Cost=300 gold
        self.ultra_potion = 1  # increases hp by 50. Cost=600 gold
        self.medium_potion = 1  # increases hp by 40, cost=450 gold