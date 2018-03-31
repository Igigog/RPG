import sys
from PyQt5.QtWidgets import QApplication
from GUI import *
from Classes import *
from fighting_system import *
from mode_select import *

game = QApplication(sys.argv)
app = App()


def game_start():
    """ Hide start button and add some another """
    app.label.setText('Now the Game begins!\n\n')
    global player
    player = 0
    player = Player()
    app.startbtn.hide()
    app.grid.addWidget(app.invbtn, 3, 1)
    app.invbtn.show()
    main_mode(app)

def load_clicked():
    try:
        with open('save.txt', 'r') as f:
            pre_load = []
            for x in f.readline().split(','):
                pre_load.append(int(x))
            player.equip = pre_load[0]
            player.exp = pre_load[1]
            app.startbtn.hide()
            app.loadbtn.hide()
            app.grid.addWidget(app.invbtn, 3, 1)
            app.label.setText('Load successful!\n')
            app.invbtn.show()
            main_mode(app)
    except FileNotFoundError:
        app.label.setText('There is no saves!')
    except (IndexError, ValueError):
        app.label.setText('Save corrupted!')


def save_clicked():
    with open('save.txt', 'w') as f:
        f.write('%s,%s' % (player.inventory, player.exp))


def find_clicked():
    player.find_opponent()
    fight_mode(app)
    app.label.setText('Your opponent is %s\n\n' % (player.opponent.name))


def inv_clicked():
    app.label.setText('You weapon is %s\n\n' % (player.weapon[0]))
    for x in player.inventory:
        app.wpnbox.addItem(x[0])
    inv_mode(app)


def change_weapon():
    for x in player.inventory:
        if x[0] == app.wpnbox.currentText():
            player.weapon = x
            player.crit = player.weapon[2]
            break
    app.label.setText(app.label.text() + 'You weapon is %s\n\n' % (player.weapon[0]))


def exit_inv():
    if player.opponent:
        fight_mode(app)
        app.invbtn.show()
    else:
        main_mode(app)
        app.invbtn.show()


def atk_clicked():
    app.label.setText(app.label.text() + attack(player))
    if pobeditel(player) != 'nothing' and pobeditel(player):
        main_mode(app)
        player.health = player.starthealth
        player.exp += 1
        player.opponent = ''
        app.label.setText(app.label.text() + '\nCongratulations! You win!\nHealth restored\nExp +1\n\n')
    elif pobeditel(player) == 'nothing':
        pass
    else:
        app.label.setText(app.label.text() + 'You lose! Try again next time!')
        app.escbtn.hide()
        app.atkbtn.hide()
        app.invbtn.hide()
        app.startbtn.show()


def esc_clicked():
    if pobeg(player):
        app.label.setText(app.label.text() + 'You escaped c:\n\n')
        main_mode(app)
    else:
        app.label.setText(app.label.text() + 'Escape failed :c\nYou get %s damage' % (player.opponent.attack))


def sr_clicked():
    app.label.setText('You found %s\n' % (player.search_weapon()))


app.startbtn.clicked.connect(game_start)
app.fndbtn.clicked.connect(find_clicked)
app.srbtn.clicked.connect(sr_clicked)
app.escbtn.clicked.connect(esc_clicked)
app.atkbtn.clicked.connect(atk_clicked)
app.invbtn.clicked.connect(inv_clicked)
app.loadbtn.clicked.connect(load_clicked)
app.savebtn.clicked.connect(save_clicked)
app.extinvbtn.clicked.connect(exit_inv)
app.cngwpnbtn.clicked.connect(change_weapon)


sys.exit(game.exec_())
