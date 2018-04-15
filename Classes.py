from random import randint
from lists import weapons, opponents, locations, armors, loot


class Mob:
    def __init__(self, self_list):
        self.opponent = ''
        self.weapon = weapons[0]
        self.equip = armors[0]
        self.name = self_list[0]
        self.starthealth = self_list[1]
        self.health = self_list[1]
        self.attack = self_list[2]
        self.armor = self_list[3]
        self.lvl = self_list[4]
        self.gold = self_list[5]
        self.crit = 1
        self.dodge = 1
        self.energy = 5


class Player(Mob):
    def __init__(self):
        self_list = ['player', 20, 1, 0, 1, 0]
        super().__init__(self_list)
        self.weapon = weapons[0]
        self.equip = armors[0]
        self.exp = 0
        self.wpninventory = [self.weapon]
        self.armorinventory = [self.equip]
        self.location = locations[0]
        self.garbageinv = []

    @classmethod
    def fibonacci(cls):
        x = 2
        y = 1
        while True:
            x, y = y, x+y
            yield y

    def search_treasure(self):
        summa = 0
        for x in range(1, len(loot) + 1):   # search for triangle num
            summa += x
        rand_ch = randint(1, summa)
        start_stat = 1
        for step in range(2, summa):           # summa = 1+2+3+4+...+n n=len(weapons)
            if rand_ch > start_stat:           # drop chance of last element = 1/summa etc.
                start_stat += step             # drop chance of reversed n'th element = n'th term/sum
            else:
                n = len(loot) - (step - 1)  # step starts from 2 therefore we need to subtract 1
                break
        self.garbageinv.append(loot[n])
        return loot[n][0]

    def find_opponent(self):
        enemy_list = []
        for x in opponents:
            if x[4] in range(self.location[1], self.location[1] + 2):
                enemy_list.append(x)
        num = randint(0, len(enemy_list) - 1)
        self.opponent = Mob(enemy_list[num])
        self.opponent.opponent = self

    def lvl_up(self):
        lvl = 1
        for x in self.fibonacci():
            if self.exp >= x:
                lvl += 1
            else:
                break
        self.lvl = lvl
