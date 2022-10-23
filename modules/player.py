
class Player:

    def __init__(self):
        self.gold = 1500  # used in store to buy items

        self.base_hp = 100
        self.max_hp = self.base_hp # can be increased by items
        self.hp = self.base_hp # current hp

        self.base_attack = 40
        self.max_attack = self.base_attack # can be increased by items
        self.attack = self.base_attack # current attack

        self.weapon = ""
        self.armour = ""

        self.Iron_Armour = False  # decreases opp_att by 10
        self.Mythril_Armour = False  # decreases opp_att by 20
        self.Orichalium_Armour = False  # decreases opp_att by 30

        self.BunSamosa_Armour= False #decreases opp_att by 50
        self.ACM_Armour= False #decreases opp_att by 60
        self.Jade_Armour = False # increases hp by 10
        self.Diamond_Armour = False #increases hp by 20
        self.Silver_Armour = False #decreaases Opp_ATT by 40
        self.Gold_Armour= False #decreases opp_att by 70

        self.items = []

    def change_weapon(self, new_weapon):
        if self.weapon != "":
            self.max_attack -= self.weapon.attack

        self.weapon = new_weapon
        if new_weapon.attack:
            self.max_attack += new_weapon.attack

    def change_armour(self, new_armour):
        if self.armour != "":
            if new_armour.attack:
                self.max_attack -= self.armour.attack
            if new_armour.hp:
                self.max_hp -= self.armour.hp

        self.armour = new_armour
        if new_armour.attack:
            self.max_attack += new_armour.attack
        if new_armour.hp:
            self.max_hp += new_armour.hp

    def add_item_to_inventory(self, item, amount):
        item_found = False
        for x in self.items:
            if x["name"] == item.name:
                item_found = True
                x["amount"] += amount
                break

        if item_found == False:
            self.items.append({ "name": item.name, "amount": amount, "ref": item })
    
    def remove_item_from_inventory(self, itemname, amount):
        for x in self.items:
            if x["name"] == itemname:
                item_found = True
                x["amount"] -= amount
                if x["amount"] == 0:
                    self.items.remove(x)
                break

    def get_item_amount(self, itemname):
        for x in self.items:
            if x["name"] == itemname:
                return x["amount"]
        return 0