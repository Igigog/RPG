from random import randint


def crit(player):
    critical = randint(1,100)
    if player.crit > critical:
        return True
    else:
        return False


def dodge(player):
    standart_dodge = 1
    dodge_try = randint(1, 10)
    if player.dodge * standart_dodge >= dodge_try:
        return True
    else:
        return False


def vivod(crit1, crit2, dodge1, dodge2, dmg1, dmg2, player):  # 1 - player, 2 - enemy
    enemy_dodge = 'Enemy dodged your attack.\n'
    your_dodge = 'Dodge! You get no damage.\n\n'
    critical = 'Crit! Damage doubled.\n'
    player_dmg = 'You deal %s dmg to enemy. %s is on %s hp.\n' % (
        dmg1, player.opponent.name.title(), player.opponent.health)
    enemy_dmg = '%s deal %s dmg to you.\n\n' % (player.opponent.name.title(), dmg2)
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
    player_crit = 0
    enemy_crit = 0
    player_damage = 0
    enemy_damage = 0
    if dodge(player.opponent):
        print('ed')
        enemy_dodge = True
    else:
        enemy_dodge = False
        player_damage = player.attack + player.equip
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
    if randint(0, 1) > 0:
        player.health = player.starthealth
        player.opponent = ''
        return True
    else:
        player.health -= player.opponent.attack
        return False
