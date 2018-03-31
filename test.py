def fight(self):
    if self.opponent != '':
        hitbar = opponents[self.opponent][1]
        attack = opponents[self.opponent][2]
        turn = 1
        while hitbar > 0 and self.health > 0:
            print(hitbar, self.health)
            if turn % 2 == 0:
                self.health -= attack
            else:
                hitbar -= self.attack + self.equip[0]
        if hitbar < 1:
            self.exp += 1
            self.health = self.starthealth
            self.opponent = ''
            return True
        else:
            return False
    else:
        return 0