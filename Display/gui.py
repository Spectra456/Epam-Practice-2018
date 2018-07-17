import sys
from PyQt5.QtWidgets import QGridLayout, QLabel, QDialog, QComboBox, QApplication, QPushButton, QLineEdit, QTextEdit, \
    QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import Display.functions as f
from Display import dataReader as r


def computeGraphs(x, k, b, s, filename):
    if s == 1:

        return f.linFunction(x, k, b)

    if s == 2:
        return f.sinFunction(x)

    if s == 3:
        return f.logFunction(x)

    if s == 4:
        return f.randFunction()

    if s == 5:
        return r.bin2float(filename, 1000)


class Widget(QDialog):
    filename = ""
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)

        self.figure = plt.figure()

        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.arrayText = QLabel("Array")
        self.fArg = QLabel("K")
        self.sArg = QLabel("B")
        self.consoleMessage = QLabel("Message")
        self.functionType = QLabel("Function")
        self.selectedFile = QLabel("")

        self.array = QLineEdit(self)

        self.firstArgument = QLineEdit(self)
        self.secondArgument = QLineEdit(self)

        self.comboBox = QComboBox(self)
        self.comboBox.activated.connect(self.selectedFunction)

        self.console = QTextEdit(self)
        self.console.setMaximumHeight(40)
        self.console.setDisabled(True)

        self.comboBox.addItem("Linear")
        self.comboBox.addItem("Sinus")
        self.comboBox.addItem("Log")
        self.comboBox.addItem("Random")
        self.comboBox.addItem("From file")

        self.button = QPushButton('Plot')
        self.button.clicked.connect(self.plot)

        self.selectButton = QPushButton("Select File")
        self.selectButton.clicked.connect(self.showDialog)

        grid = QGridLayout()

        grid.addWidget(self.toolbar)
        grid.addWidget(self.canvas)

        grid.addWidget(self.functionType)
        grid.addWidget(self.comboBox)

        grid.addWidget(self.arrayText)
        grid.addWidget(self.array)

        grid.addWidget(self.fArg)
        grid.addWidget(self.firstArgument)

        grid.addWidget(self.sArg)
        grid.addWidget(self.secondArgument)

        grid.addWidget(self.consoleMessage)
        grid.addWidget(self.console)

        grid.addWidget(self.selectedFile)
        grid.addWidget(self.button)
        grid.addWidget(self.selectButton)

        self.setLayout(grid)


    def plot(self):

        typeFunc = self.comboBox.currentIndex()
        self.console.setText("")
        array = [0, 0]
        k = 0
        b = 0
        filename = ""

        if typeFunc == 4:
            filename = self.filename

        try:

            array = list(map(int, self.array.text().split()))

        except(TypeError, ValueError):

            if typeFunc == 0 or typeFunc == 1 or typeFunc == 2:
                self.console.setText("Please, enter correct array")

        try:

            k = int(self.firstArgument.text())
            b = int(self.secondArgument.text())
        except(TypeError, ValueError):
            if typeFunc == 0:
                self.console.setText("Please, enter correct arguments")

        self.figure.clear()

        ax = self.figure.add_subplot(111)

        ax.plot(computeGraphs(array, k, b, typeFunc + 1, filename), '*-')

        self.canvas.draw()

    def showDialog(self):

        self.filename = QFileDialog.getOpenFileName(self, 'Open file')[0]
        self.selectedFile.setText(self.filename)

    def selectedFunction(self):

        if self.comboBox.currentIndex() == 0:
            self.fArg.setVisible(True)
            self.firstArgument.setVisible(True)
            self.sArg.setVisible(True)
            self.secondArgument.setVisible(True)
        else:
            self.fArg.setVisible(False)
            self.firstArgument.setVisible(False)
            self.sArg.setVisible(False)
            self.secondArgument.setVisible(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Widget()
    main.show()

    sys.exit(app.exec_())