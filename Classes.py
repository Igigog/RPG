from random import randint
from lists import *


class Player:
    def __init__(self):
        self.starthealth = 20
        self.health = 20
        self.attack = 3
        self.opponent = ''
        self.exp = 0
        self.armor = 0
        self.weapon = ['nothing', 0, 1]
        self.crit = 1
        self.dodge = 1
        self.inventory = []

    def search_weapon(self):
        sum = 0
        for x in range(1, len(weapons) + 1): #search for triangle num
            sum += x
        rand_ch = randint(1, sum)
        start_stat = 1
        for step in range(2, sum):             # sum = 1+2+3+4+...+n n=len(weapons)
            if rand_ch > start_stat:           # drop chance of last element = 1/sum etc.
                start_stat += step             # drop chance of reversed n'th element = n'th term/sum
            else:
                n = len(weapons) - (step - 1)  # step starts from 2 therefore we need to subtract 1
                break
        if weapons[n] not in self.inventory:
            self.inventory.append(weapons[n])
        return weapons[n][0]

    def find_opponent(self):
        opponent = randint(0, len(opponents) - 1)
        enemy = opponents[opponent]
        self.opponent = Mob(enemy[0], enemy[1], enemy[2], enemy[3])


class Mob:
    def __init__(self, name, health, attack, armor):
        self.name = name
        self.starthealth = health
        self.health = health
        self.attack = attack
        self.armor = armor
        self.crit = 1
        self.dodge = 1




