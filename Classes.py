from random import randint
from lists import weapons, opponents, locations, armors


class Player:
    def __init__(self):
        self.starthealth = 20
        self.health = 20
        self.attack = 3
        self.opponent = ''
        self.exp = 0
        self.armor = armors[0]
        self.weapon = weapons[0]
        self.crit = 1
        self.dodge = 1
        self.wpninventory = [self.weapon]
        self.armorinventory = [self.armor]
        self.lvl = 1
        self.location = locations[0]

    @classmethod
    def fibonacci(cls):
        x = 2
        y = 1
        while True:
            x, y = y, x+y
            yield y

    def search_weapon(self):
        summa = 0
        for x in range(1, len(weapons) + 1):   # search for triangle num
            summa += x
        rand_ch = randint(1, summa)
        start_stat = 1
        for step in range(2, summa):           # summa = 1+2+3+4+...+n n=len(weapons)
            if rand_ch > start_stat:           # drop chance of last element = 1/summa etc.
                start_stat += step             # drop chance of reversed n'th element = n'th term/sum
            else:
                n = len(weapons) - (step - 1)  # step starts from 2 therefore we need to subtract 1
                break
        if weapons[n] not in self.wpninventory:
            self.wpninventory.append(weapons[n])
        return weapons[n][0]

    def find_opponent(self):
        enemy_list = []
        for x in opponents:
            if x[4] in range(self.location[1], self.location[1] + 2):
                enemy_list.append(x)
        num = randint(0, len(enemy_list) - 1)
        self.opponent = Mob(enemy_list[num])

    def lvl_up(self):
        lvl = 1
        for x in self.fibonacci():
            if self.exp >= x:
                lvl += 1
            else:
                break
        self.lvl = lvl


class Mob:
    def __init__(self, enemy_list):
        self.name = enemy_list[0]
        self.starthealth = enemy_list[1]
        self.health = enemy_list[1]
        self.attack = enemy_list[2]
        self.armor = enemy_list[3]
        self.lvl = enemy_list[4]
        self.golddrop = enemy_list[5]
        self.crit = 1
        self.dodge = 1
