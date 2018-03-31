import sys
from PyQt5.QtWidgets import QApplication
from GUI import *
from Classes import *
from fighting_system import *

game = QApplication(sys.argv)
app = App()
player = Player()


def game_start():
    """ Hide start button and add some another """
    app.label.setText('Let the Game begins!\n\n')
    app.startbtn.hide()
    app.grid.addWidget(app.invbtn, 3, 1)
    main_mode()

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
            main_mode()
    except FileNotFoundError:
        app.label.setText('There is no saves!')
    except IndexError:
        app.label.setText('Save corrupted!')


def save_clicked():
    with open('save.txt', 'w') as f:
        f.write('%s,%s' % (player.equip, player.exp))

def main_mode():
    app.escbtn.hide()
    app.atkbtn.hide()
    app.savebtn.show()
    app.fndbtn.show()
    app.srbtn.show()


def fight_mode():
    app.savebtn.hide()
    app.fndbtn.hide()
    app.srbtn.hide()
    app.escbtn.show()
    app.atkbtn.show()


def find_clicked():
    player.find_opponent()
    fight_mode()
    app.label.setText('Your opponent is %s\n\n' % (player.opponent.name))


def inv_clicked():
    app.label.setText(app.label.text() +  'You weapon is %s\n\n' % (weapons[player.equip]))


def atk_clicked():
    app.label.setText(app.label.text() + attack(player))
    if pobeditel(player) != 'nothing' and pobeditel(player):
        main_mode()
        player.health = player.starthealth
        player.exp += 1
        player.opponent = ''
        app.label.setText(app.label.text() + '\nCongratulations! You win!\nHealth restored\nExp +1')
    elif pobeditel(player) == 'nothing':
        pass
    else:
        app.label.setText(app.label.text() + 'You lose! Try again next time!')
        app.escbtn.hide()
        app.atkbtn.hide()


def esc_clicked():
    if pobeg(player):
        app.label.setText(app.label.text() + 'You escaped c:\n\n')
        main_mode()
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

sys.exit(game.exec_())
