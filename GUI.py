import sys
import time

import graph as g
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QTextEdit, QGridLayout, QApplication, QPushButton, QComboBox)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        array = QLabel('Array')
        karg = QLabel('K')
        barg = QLabel('B')
        console = QLabel("Message")
        functionType = QLabel("Function")

        self.arrayEdit = QLineEdit(self)
        self.kargEdit = QLineEdit(self)
        self.bargEdit = QLineEdit(self)
        self.selectFunction = QComboBox(self)

        self.selectFunction.addItem("Linear")
        self.selectFunction.addItem("Sinus")
        self.selectFunction.addItem("Log")
        self.selectFunction.addItem("Random")

        self.consoleEdit = QTextEdit(self)
        self.consoleEdit.setDisabled(True)

        okButton = QPushButton("OK", self)
        okButton.clicked.connect(self.buttonClicked)

        grid = QGridLayout()
        grid.setSpacing(5)

        grid.addWidget(okButton, 1, 3)
        grid.addWidget(functionType, 1, 0)
        grid.addWidget(self.selectFunction, 1, 1)

        grid.addWidget(array, 2, 0)
        grid.addWidget(self.arrayEdit, 2, 1)

        grid.addWidget(karg, 3, 0)
        grid.addWidget(self.kargEdit, 3, 1)

        grid.addWidget(barg, 4, 0)
        grid.addWidget(self.bargEdit, 4, 1)

        grid.addWidget(console, 5, 0)
        grid.addWidget(self.consoleEdit, 5, 1)

        self.setLayout(grid)
        self.setGeometry(1080, 300, 400, 100)
        self.setWindowTitle('Graph')
        self.show()

    def buttonClicked(self):

        sender = self.sender()
        typeFunc = self.selectFunction.currentIndex()
        self.consoleEdit.setText(" ")
        array = [0, 0]
        k = 0
        b = 0

        try:

            array = list(map(int, self.arrayEdit.text().split()))
            k = int(self.kargEdit.text())
            b = int(self.bargEdit.text())
        except(TypeError, ValueError):

            if typeFunc == 0 or typeFunc == 1 or typeFunc == 2:
                self.consoleEdit.setText("Please, enter correct data")

        g.show(typeFunc + 1, (array), k, b)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
