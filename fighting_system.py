from random import randint


def attack(player):
    damage = player.attack + player.equip
    player.opponent.health -= damage
    player.health -= player.opponent.attack
    return ("You deal %s damage, your opponent's health %s\n%s hit you for %s hp, your hp is %s\n\n" % (
        damage, player.opponent.health, player.opponent.name.title(), player.opponent.attack, player.health))


def pobeditel(player):
    if player.health < 1:
        return False
    elif player.opponent.health < 1:
        return True
    else:
        return 'nothing'


def pobeg(player):
    if randint(0, 1) > 0:
        player.health = player.starthealth
        player.opponent = ''
        return True
    else:
        player.health -= player.opponent.attack
        return False
