from random import randint


def crit(player):
    print('crit before')
    critical = randint(1, 1000//player.crit)
    print('crit')
    if 10 >= critical:
        return True
    else:
        return False


def dodge(player):
    print('dodge')
    dodge_try = randint(1, 10)
    if player.dodge >= dodge_try:
        return True
    else:
        return False


def vivod(crit1, crit2, dodge1, dodge2, dmg1, dmg2, player):  # 1 - player, 2 - enemy
    enemy_dodge = 'Enemy dodged your attack.\n'
    your_dodge = 'Dodge! You get no damage.\n\n'
    critical = 'Crit! Damage doubled.\n'
    player_dmg = 'You deal %s dmg to enemy. %s is on %s hp.\n' % (
        dmg1, player.opponent.name.title(), player.opponent.health)
    enemy_dmg = '%s deal %s dmg to you. You are on %s hp.\n\n' % (player.opponent.name.title(), dmg2, player.health)
    main_text = ''
    if dodge2:
        main_text += enemy_dodge
    else:
        if crit1:
            main_text += critical
        main_text += player_dmg
    if dodge1:
        main_text += your_dodge
    else:
        if crit2:
            main_text += critical
        main_text += enemy_dmg
    return main_text


def attack(player):
    print('init')
    player_crit = 0
    enemy_crit = 0
    player_damage = 0
    enemy_damage = 0
    if dodge(player.opponent):
        print('ed')
        enemy_dodge = True
    else:
        enemy_dodge = False
        print(1)
        player_damage = player.attack + player.weapon[1]
        print(1)
        if crit(player):
            player_crit = True
            player_damage *= 2
        else:
            player_crit = False
        player.opponent.health -= player_damage
    if dodge(player):
        print('pd')
        player_dodge = True
    else:
        player_dodge = False
        enemy_damage = player.opponent.attack
        if crit(player.opponent):
            enemy_crit = True
            enemy_damage *= 2
        else:
            enemy_crit = False
        player.health -= enemy_damage
    return vivod(player_crit, enemy_crit, player_dodge, enemy_dodge, player_damage, enemy_damage, player)


def pobeditel(player):
    if player.health < 1:
        return False
    elif player.opponent.health < 1:
        return True
    else:
        return 'nothing'


def pobeg(player):
    if randint(1, 4) == 1:
        player.health = player.starthealth
        player.opponent = ''
        return True
    else:
        player.health -= player.opponent.attack
        return False
