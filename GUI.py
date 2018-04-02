from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import \
    QWidget, QPushButton, QLabel, QGridLayout, QFrame, QComboBox, QTabBar
from PyQt5.QtGui import QIcon


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def okno(self):
        self.setGeometry(300, 300, 600, 500)
        self.setWindowTitle('WITCHER WITH BLACKJACK AND PLOTVA')
        self.setWindowIcon(QIcon('ico.ico'))

    def buttons(self):
        self.startbtn = QPushButton('Start')
        self.loadbtn = QPushButton('Load')

        self.atkbtn = QPushButton('Attack')
        self.escbtn = QPushButton('Escape')

        self.invbtn = QPushButton('Inventory')
        self.savebtn = QPushButton('Save')
        self.srbtn = QPushButton('Search for a treasure')
        self.fndbtn = QPushButton('Opponent')
        self.mapbtn = QPushButton('Map')

        self.cngwpnbtn = QPushButton('Change weapon')
        self.extinvbtn = QPushButton('Leave inventory')
        self.cngarmorbtn = QPushButton('Change armor')
        self.armorbox = QComboBox()
        self.wpnbox = QComboBox()

        self.mapbox = QComboBox()
        self.cnglocbtn = QPushButton('Change location')
        self.extmapbtn = QPushButton('Exit Map')

        self.markettab = QTabBar()
        self.markettab.setShape(1)
        self.marketbox = QComboBox()
        self.markettab.addTab('Weapons')
        self.markettab.addTab('Armor')
        self.buybtn = QPushButton('Buy')
        self.marketbtn = QPushButton('Market')
        self.extmarket = QPushButton('Exit Market')
        self.sellbtn = QPushButton('Sell garbage')

    def initUI(self):
        self.okno()
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.label = QLabel()
        self.label.setFrameStyle(QFrame.Box)           # main label
        self.label.setFrameShadow(QFrame.Raised)
        self.label.setMidLineWidth(1)
        self.label.setLineWidth(1)
        self.label.setAlignment(Qt.AlignTop)
        self.grid.addWidget(self.label, 1, 1, 1, 2)
        self.label.setText('Are you ready for adventure?')

        self.buttons()

        self.grid.addWidget(self.startbtn, 2, 1)  # start screen
        self.grid.addWidget(self.loadbtn, 2, 2)

        self.grid.addWidget(self.srbtn, 2, 1)    # main mode
        self.grid.addWidget(self.fndbtn, 2, 2)
        self.grid.addWidget(self.savebtn, 3, 2)
        self.grid.addWidget(self.mapbtn, 4, 1)
        self.savebtn.hide()
        self.srbtn.hide()
        self.fndbtn.hide()
        self.mapbtn.hide()

        self.grid.addWidget(self.atkbtn, 2, 2)    # fight mode
        self.grid.addWidget(self.escbtn, 2, 1)
        self.atkbtn.hide()
        self.escbtn.hide()

        self.grid.addWidget(self.wpnbox, 2, 1)     # inventory mode
        self.grid.addWidget(self.extinvbtn, 4, 1)
        self.grid.addWidget(self.cngwpnbtn, 2, 2)
        self.grid.addWidget(self.armorbox, 3, 1)
        self.grid.addWidget(self.cngarmorbtn, 3, 2)
        self.armorbox.hide()
        self.cngarmorbtn.hide()
        self.cngwpnbtn.hide()
        self.extinvbtn.hide()
        self.wpnbox.hide()

        self.grid.addWidget(self.mapbox, 2, 1)      # map mode
        self.grid.addWidget(self.cnglocbtn, 2, 2)
        self.grid.addWidget(self.extmapbtn, 3, 1)
        self.grid.addWidget(self.marketbtn, 3, 2)
        self.marketbtn.hide()
        self.mapbox.hide()
        self.extmapbtn.hide()
        self.cnglocbtn.hide()

        self.grid.addWidget(self.markettab, 2, 1)   # market mode
        self.grid.addWidget(self.sellbtn, 4, 1)
        self.grid.addWidget(self.marketbox, 3, 1)
        self.grid.addWidget(self.buybtn, 3, 2)
        self.grid.addWidget(self.extmarket, 4, 2)

        self.buybtn.hide()
        self.sellbtn.hide()
        self.extmarket.hide()
        self.markettab.hide()
        self.marketbox.hide()

        self.show()





