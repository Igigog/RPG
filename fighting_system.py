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
        return damage//2


def vivod(crit1, crit2, dodge1, dodge2, dmg1, dmg2, player):  # 1 - player, 2 - enemy
    if player.opponent.health < 1:
        player.opponent.health = 0
    enemy_dodge = 'Enemy dodged your attack.\n'
    your_dodge = 'Dodge! You get no damage.\n\n'
    critical = 'Crit! Damage doubled.\n'
    player_dmg = 'You deal %s dmg to enemy. %s is on %s hp.\n' % (
        dmg1, player.opponent.name.title(), player.opponent.health)
    enemy_dmg = '%s deal %s dmg to you. You are on %s hp.\n\n' % (
        player.opponent.name.title(), dmg2, player.health)
    armor_zerodmg = 'Oops, armor is too strong. No damage dealt.'
    main_text = ''
    if player.opponent.health < 1 and player.health < 1:
        if crit1:
            main_text += critical
        main_text += player_dmg
        return '%sSo close!\n' % main_text
    if dodge2:
        main_text += enemy_dodge
    else:
        if crit1:
            main_text += critical
        if not enemy_dmg:
            main_text += armor_zerodmg
        else:
            main_text += player_dmg
    if dodge1:
        main_text += your_dodge
    else:
        if crit2:
            main_text += critical
        if not enemy_dmg:
            main_text += armor_zerodmg
        else:
            main_text += enemy_dmg
    return main_text


def attack(player):
    player_crit = 0
    enemy_crit = 0
    player_damage = 0
    enemy_damage = 0
    if dodge(player.opponent):
        enemy_dodge = True
    else:
        enemy_dodge = False
        player_damage = player.attack + player.weapon[1]
        if crit(player):
            player_crit = True
            player_damage *= 2
        else:
            player_damage = armor_stat(player.opponent, player_damage)
            player_crit = False
        player.opponent.health -= player_damage
    if dodge(player):
        player_dodge = True
    else:
        player_dodge = False
        enemy_damage = player.opponent.attack
        if crit(player.opponent):
            enemy_crit = True
            enemy_damage *= 2
        else:
            enemy_damage = armor_stat(player, enemy_damage)
            enemy_crit = False
        player.health -= enemy_damage
    return vivod(player_crit, enemy_crit, player_dodge, enemy_dodge, player_damage, enemy_damage, player)


def pobeditel(player):
    if player.opponent.health < 1:
        return True
    elif player.health < 1:
        return False
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
