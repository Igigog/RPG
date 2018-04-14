import sys
from itertools import chain
from PyQt5.QtWidgets import QApplication
from GUI import *
from Classes import *
from fighting_system import *
from mode_select import *


def update_stats():
    app.statlabel.setText('LVL: %s\nEXP: %s\nATK: %s\nDEF: %s\nARM: %s\nWPN: %s\nGOLD: %s' %
                          (player.lvl, player.exp, (player.attack + player.weapon[1]),
                           player.armor, player.equip[0], player.weapon[0], player.gold))


def game_start():
    """ Hide start buttons and start mainloop """
    global player
    player = Player()

    app.label.setText('Now the Game begins!\n\n')

    main_mode(app)


def load_clicked():
    try:
        with open('save.txt', 'r') as f:
            global player
            player = Player()
            player.wpninventory.clear()
            player.armorinventory.clear()
            player.weapon = []
            player.equip = []

            for x in f.readline().split(' '):
                try:
                    x = int(x)
                    player.wpninventory.append(weapons[x])
                except ValueError:
                    pass
            for x in f.readline().split(' '):
                try:
                    x = int(x)
                    player.armorinventory.append(armors[x])
                except ValueError:
                    pass
            for x in f.readline().split(' '):
                try:
                    x = int(x)
                    player.garbageinv.append(loot[x])
                except ValueError:
                    pass
            stats = f.readline().split(' ')
            player.exp = int(stats[0])
            player.armor = int(stats[1])
            player.gold = int(stats[2])
            player.weapon = weapons[int(stats[3])]
            player.equip = armors[int(stats[4])]
            player.lvl_up()

            app.label.setText('Load successful!\n')

            main_mode(app)

    except FileNotFoundError:
        app.label.setText('There is no saves!')
    except (IndexError, ValueError):
        app.label.setText('Save corrupted!')


def save_clicked():
    with open('save.txt', 'w') as f:
        for x in player.wpninventory:
            f.write('%s ' % x[5])
        f.write('\n')
        for x in player.armorinventory:
            f.write('%s ' % x[5])
        f.write('\n')
        for x in player.garbageinv:
            f.write('%s ' % x[3])
        f.write('\n')
        f.write('%s %s %s %s %s' % (player.exp, player.armor, player.gold, player.weapon[5], player.equip[5]))
        app.label.setText('Save successful')


def find_clicked():
    player.find_opponent()
    fight_mode(app)
    app.label.setText('Your opponent is %s\n\n' % player.opponent.name)


def search_clicked():
    app.label.clear()
    if randint(1, 10) < 3:
        find_clicked()
    elif player.energy:
        x = player.search_treasure()
        insert_text(app.label, ('You found %s\n' % x))
    else:
        insert_text(app.label, 'No energy\n')


def inv_clicked():
    app.armorbox.clear()
    app.wpnbox.clear()
    app.label.setText('You weapon is %s\n' % player.weapon[0])
    insert_text(app.label, 'You armor is %s\n\n' % player.equip[0])
    for x in player.wpninventory:
        app.wpnbox.addItem(x[0])
    for x in player.armorinventory:
        app.armorbox.addItem(x[0])
    inv_mode(app)


def change_armor():
    for x in player.armorinventory:
        if x[0] == app.armorbox.currentText():
            player.equip = x
            player.armor = x[1]
            player.dodge = x[2]
            break
    insert_text(app.label, 'You armor is %s\n\n' % player.equip[0])


def change_weapon():
    for x in player.wpninventory:
        if x[0] == app.wpnbox.currentText():
            player.weapon = x
            player.crit = player.weapon[2]
            break
    insert_text(app.label, 'You weapon is %s\n\n' % player.weapon[0])


def atk_clicked():
    startlvl = player.lvl
    insert_text(app.label, attack(player))
    if pobeditel(player):
        main_mode(app)
        insert_text(app.label, 'Congratulations! You win!\nHealth restored\nExp +1\nGold + %s\n\n' %
                    player.opponent.gold)
        player.health = player.starthealth
        player.exp += 1
        player.energy = 5
        player.gold += player.opponent.gold
        player.opponent = ''
        player.lvl_up()
        if player.lvl > startlvl:
            insert_text(app.label, 'Level up! Your lvl is now %s\n' % player.lvl)
    elif pobeditel(player) == 0:
        pass
    else:
        dead_mode(app)


def esc_clicked():
    if pobeg(player):
        insert_text(app.label, 'You escaped c:\n\n')
        main_mode(app)
    else:
        insert_text(app.label, 'Escape failed :c\nYou get %s damage\n\n' % player.opponent.attack)
        if player.health < 1:
            dead_mode(app)


def map_clicked():
    app.mapbox.clear()
    app.label.setText('Your location is %s\n\n' % player.location[0])
    for loc in locations:
        app.mapbox.addItem(loc[0])
    map_mode(app)


def change_loc():
    for loc in locations:
        if app.mapbox.currentText() == loc[0]:
            player.location = loc
            break
    insert_text(app.label, 'Your location is %s\n\n' % player.location[0])


def weapons_market():
    app.marketbox.clear()
    app.label.clear()
    for x in weapons:
        if x[3] in range(player.location[1], player.location[1] + 3):
            app.marketbox.addItem(x[0])
            insert_text(app.label, '%s  ATK:%s  COST:%s\n' % (x[0], x[1], x[4]))
    insert_text(app.label, '\n')


def armor_market():
    app.marketbox.clear()
    app.label.clear()
    for x in armors:
        if x[3] in range(player.location[1], player.location[1] + 3):
            app.marketbox.addItem(x[0])
            insert_text(app.label, '%s  DEF:%s  COST:%s\n' % (x[0], x[1], x[4]))
    insert_text(app.label, '\n')


def enter_market():
    market_mode(app)
    weapons_market()


def buy_clicked():
    for n in chain(weapons, armors):
        if app.marketbox.currentText() == n[0]:
            if player.gold < n[4]:
                insert_text(app.label, 'Not enough gold.\n\n')
                return False
            else:
                player.gold -= n[4]
                if n in weapons:
                    player.wpninventory.append(n)
                else:
                    player.armorinventory.append(n)
            insert_text(app.label, '%s in now yours.\n' % n[0])
            return True


def sell_clicked():
    summa = 0
    if not player.garbageinv:
        insert_text(app.label, 'No garbage.\n\n')
        return False
    for x in range(len(player.garbageinv)):
        summa += player.garbageinv[0][1]
        player.garbageinv.pop(0)
    player.gold += summa
    insert_text(app.label, 'Garbage sold. You get %s gold.\n\n' % summa)


def change_market_mode():
    if app.markettab.currentIndex():
        armor_market()
    else:
        weapons_market()


def connect_buttons():
    """connect all buttons from GUI with functions"""

    app.startbtn.clicked.connect(game_start)    # start mode
    app.loadbtn.clicked.connect(load_clicked)

    app.fndbtn.clicked.connect(find_clicked)    # main mode
    app.srbtn.clicked.connect(search_clicked)
    app.savebtn.clicked.connect(save_clicked)
    app.invbtn.clicked.connect(inv_clicked)
    app.mapbtn.clicked.connect(map_clicked)

    app.escbtn.clicked.connect(esc_clicked)     # fight mode
    app.atkbtn.clicked.connect(atk_clicked)

    app.extinvbtn.clicked.connect(lambda: main_mode(app))     # inv mode
    app.cngwpnbtn.clicked.connect(change_weapon)
    app.cngarmorbtn.clicked.connect(change_armor)

    app.cnglocbtn.clicked.connect(change_loc)   # map mode
    app.extmapbtn.clicked.connect(lambda: main_mode(app))
    app.marketbtn.clicked.connect(enter_market)

    app.extmarket.clicked.connect(lambda: map_mode(app))    # market mode
    app.buybtn.clicked.connect(buy_clicked)
    app.sellbtn.clicked.connect(sell_clicked)
    app.markettab.currentChanged.connect(change_market_mode)


def connect_anything():
    app.label.textChanged.connect(update_stats)


if __name__ == '__main__':
    game = QApplication(sys.argv)
    app = App()

    connect_buttons()
    connect_anything()
    sys.exit(game.exec_())
