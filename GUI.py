from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import \
    QWidget, QPushButton, QLabel, QGridLayout, QFrame
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
        self.atkbtn = QPushButton('Attack')
        self.srbtn = QPushButton('Search')
        self.fndbtn = QPushButton('Opponent')
        self.escbtn = QPushButton('Escape')
        self.invbtn = QPushButton('Inventory')
        self.savebtn = QPushButton('Save')
        self.loadbtn = QPushButton('Load')


    def initUI(self):
        self.okno()
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.label = QLabel()
        self.label.setFrameStyle(QFrame.Box)
        self.label.setFrameShadow(QFrame.Raised)
        self.label.setMidLineWidth(1)
        self.label.setLineWidth(1)
        self.label.setAlignment(Qt.AlignTop)
        self.grid.addWidget(self.label, 1, 1, 1, 2)

        self.buttons()
        self.grid.addWidget(self.startbtn, 2,1)
        self.grid.addWidget(self.loadbtn, 2, 2)

        self.grid.addWidget(self.srbtn, 2, 1)
        self.grid.addWidget(self.fndbtn, 2, 2)
        self.grid.addWidget(self.savebtn, 3, 2)
        self.savebtn.hide()
        self.srbtn.hide()
        self.fndbtn.hide()

        self.grid.addWidget(self.atkbtn, 2, 2)
        self.grid.addWidget(self.escbtn, 2, 1)
        self.atkbtn.hide()
        self.escbtn.hide()

        self.show()

