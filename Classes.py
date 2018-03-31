from random import randint
from lists import *


class Player:
    def __init__(self,sth, atk):
        self.starthealth = sth
        self.health = sth
        self.attack = atk
        self.equip = 0 #only one int
        self.opponent = ''
        self.exp = 0

    def search_weapon(self):
        sum = 0
        for x in range(1, len(weapons) + 1): #search for triangle num
            sum += x
        rand_ch = randint(1, sum)
        start_stat = 1
        for step in range(2, sum):           # sum = 1+2+3+4+...+n n=len(weapons)
            if rand_ch > start_stat:         # drop chance of last element = 1/sum etc.
                start_stat += step           # drop chance of reversed n'th element = n'th term/sum
            else:
                n = len(weapons) + 1 - step  # step starts from 2 therefore we need to subtract 1
                break
        self.equip = max(self.equip, n)
        return weapons[n]

    def find_opponent(self):
        opponent = randint(0, len(opponents) - 1)
        enemy = opponents[opponent]
        self.opponent = Mob(enemy[0], enemy[1], enemy[2])


class Mob:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack




