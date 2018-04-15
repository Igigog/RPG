from random import randint


def crit(player):
    critical = randint(1, 1000)
    if player.crit * 100.0 >= critical:
        return True
    else:
        return False


def dodge(player):
    dodge_try = randint(1, 10)
    if player.dodge >= dodge_try:
        return True
    else:
        return False


def armor_stat(player, damage):
    if damage * 2 <= player.armor:
        return 0
    elif damage >= player.armor * 4:
        return damage - (player.armor//2)
    else:
        return damage//2 + 1


def vivod(result):
    main_text = ''
    if not result:
        return 'Dodge! No damage dealt.\n'
    else:
        if result[2]:
            main_text += 'Crit! Damage doubled.\n'
        main_text += '%s deal %s damage to %s. %s is on %s hp.\n' % (
            result[0].name.title(), result[3], result[1].name, result[1].name.title(), result[1].health)
        return main_text


def attack(player):
    enemy = player.opponent
    player_damage = player.attack + player.weapon[1]

    if dodge(player):
        return False
    else:
        if crit(player):
            player_crit = True
            player_damage *= 2
        else:
            player_damage = armor_stat(enemy, player_damage)
            player_crit = False
        enemy.health -= player_damage
        if enemy.health < 1:
            enemy.health = 0
        return [player, enemy, player_crit, player_damage]


def pobeditel(player):
    if player.opponent.health < 1:
        return True
    elif player.health < 1:
        return False
    else:
        return 0


def pobeg(player):
    if randint(1, 4) == 1:
        player.health = player.starthealth
        player.opponent = ''
        return True
    else:
        player.health -= player.opponent.attack
        return False


def win(player):
    startlvl = player.lvl
    win_text = 'Congratulations! You win!\nHealth restored\nExp +1\nGold + %s\n\n' % player.opponent.gold
    player.health = player.starthealth
    player.exp += 1
    player.energy = 5
    player.gold += player.opponent.gold
    player.opponent = ''
    player.lvl_up()
    if player.lvl > startlvl:
        win_text += 'Level up! Your lvl is now %s\n' % player.lvl
    return win_text
