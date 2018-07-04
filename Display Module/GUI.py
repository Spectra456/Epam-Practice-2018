import sys
from PyQt5.QtWidgets import QGridLayout, QLabel, QDialog, QComboBox, QApplication, QPushButton, QLineEdit, QTextEdit
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import functions as f


def computeGraphs(x, k, b, s):
    if s == 1:
        return f.linFunction(x, k, b)

    if s == 2:
        return f.sinFunction(x)

    if s == 3:
        return f.logFunction(x)

    if s == 4:
        return f.randFunction()


class Widget(QDialog):

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

        self.array = QLineEdit(self)

        self.firstArgument = QLineEdit(self)
        self.secondArgument = QLineEdit(self)

        self.comboBox = QComboBox(self)

        self.console = QTextEdit(self)
        self.console.setMaximumHeight(40)
        self.console.setDisabled(True)

        self.comboBox.addItem("Linear")
        self.comboBox.addItem("Sinus")
        self.comboBox.addItem("Log")
        self.comboBox.addItem("Random")

        self.button = QPushButton('Plot')
        self.button.clicked.connect(self.plot)

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

        grid.addWidget(self.button)


        self.setLayout(grid)

    def plot(self):

        typeFunc = self.comboBox.currentIndex()
        self.console.setText("")
        array = [0, 0]
        k = 0
        b = 0

        try:

            array = list(map(int, self.array.text().split()))
            k = int(self.firstArgument.text())
            b = int(self.secondArgument.text())
        except(TypeError, ValueError):

            if typeFunc == 0 or typeFunc == 1 or typeFunc == 2:
                self.console.setText("Please, enter correct data")

        self.figure.clear()

        ax = self.figure.add_subplot(111)

        ax.plot(computeGraphs(array, k, b, typeFunc + 1), '*-')

        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Widget()
    main.show()

    sys.exit(app.exec_())