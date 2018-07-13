import sys
from PyQt5.QtWidgets import QGridLayout, QLabel, QDialog, QComboBox, QApplication, QPushButton, QLineEdit, QTextEdit, \
    QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import ImageProcessing.transformations as t
import ImageProcessing.zoom as z


def computeImage(s, filename, factor, type):
    if s == 1:
        return t.Negative(filename)

    if s == 2:
        return t.Gamma(filename, factor)

    if s == 3:
        return t.Log(filename)

    if s == 4:
        return t.Linear(filename)
    if s == 5:
        return z.zoom(filename, factor, type)


class Widget(QDialog):
    filename = ""

    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)

        self.figure = plt.figure()

        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.consoleMessage = QLabel("Message")
        self.functionType = QLabel("Function")
        self.selectedFile = QLabel("")
        self.factorLabel = QLabel("Factor")
        self.factorLabel.setVisible(False)

        self.comboBox = QComboBox(self)
        self.comboBox.activated.connect(self.selectedFunction)

        self.factor = QLineEdit(self)
        self.factor.setVisible(False)
        self.console = QTextEdit(self)
        self.console.setMaximumHeight(40)
        self.console.setDisabled(True)

        self.comboBox.addItem("Negative")
        self.comboBox.addItem("Gamma")
        self.comboBox.addItem("Logarithm")
        self.comboBox.addItem("Linear")
        self.comboBox.addItem("From file")

        self.button = QPushButton('Apply')
        self.button.clicked.connect(self.plot)

        self.selectButton = QPushButton("Select File")
        self.selectButton.clicked.connect(self.showDialog)

        grid = QGridLayout()

        grid.addWidget(self.toolbar)
        grid.addWidget(self.canvas)

        grid.addWidget(self.functionType)
        grid.addWidget(self.comboBox)

        grid.addWidget(self.factorLabel)
        grid.addWidget(self.factor)

        grid.addWidget(self.consoleMessage)
        grid.addWidget(self.console)

        grid.addWidget(self.selectedFile)
        grid.addWidget(self.button)
        grid.addWidget(self.selectButton)

        self.setLayout(grid)

    def plot(self):

        typeFunc = self.comboBox.currentIndex()
        self.console.setText("")

        try:
            factor = self.factor.text()
            factor = int(factor)
        except (ValueError, TypeError):
            self.console.setText("Please, enter correct data.(Default factor = 1")
            factor = 1

        filename = self.filename

        self.figure.clear()
        self.figure.subplots_adjust(top=1.0, bottom=0.0, left=0.0, right=1.0)
        ax = self.figure.add_subplot(111)

        ax.axis("off")

        ax.imshow(computeImage(typeFunc + 1, filename, factor))

        self.canvas.draw()

    def showDialog(self):

        self.filename = QFileDialog.getOpenFileName(self, 'Open file')[0]
        self.selectedFile.setText(self.filename)

    def selectedFunction(self):

        print(self.comboBox.currentIndex())
        if self.comboBox.currentIndex() == 1:
            self.factorLabel.setVisible(True)
            self.factor.setVisible(True)
        else:
            self.factorLabel.setVisible(False)
            self.factor.setVisible(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Widget()
    main.show()

    sys.exit(app.exec_())
