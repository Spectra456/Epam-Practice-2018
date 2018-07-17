import sys

from PyQt5.QtWidgets import QGridLayout, QLabel, QDialog, QComboBox, QApplication, QPushButton, QLineEdit, QTextEdit, \
    QFileDialog

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import cv2

import ImageProcessing.transformations as t
import ImageProcessing.zoom as z
import ImageProcessing.histograms as h
import ImageProcessing.operations as o
import ImageProcessing.blur as b


def computeImage(s, filename, factor, type, array):

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

    if s == 6:
        return h.equalize(filename)

    if s == 7:
        return h.addMask(filename, array[0], array[1], array[2], array[3])

    if s == 8:
        return o.averaging(filename)

    if s == 9:

        return o.difference(filename[0], filename[1])
    if s == 10:
        return b.blurAuto(filename, factor)




class Widget(QDialog):

    def __init__(self, parent=None):

        self.filename = ""
        self.type = 0

        super(Widget, self).__init__(parent)

        self.figure = plt.figure()

        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.consoleMessage = QLabel("Message")
        self.functionType = QLabel("Function")
        self.zoomType = QLabel("Zoom")
        self.coordinatesLabel = QLabel("Coordinates")
        self.selectedFile = QLabel("")
        self.factorLabel = QLabel("Factor")
        self.maskLabel = QLabel("Mask size")

        self.coordinatesLabel.setVisible(False)
        self.factorLabel.setVisible(False)
        self.zoomType.setVisible(False)
        self.maskLabel.setVisible(False)

        self.comboBox = QComboBox(self)
        self.comboBox.activated.connect(self.selectedFunction)

        self.zoomChoose = QComboBox(self)
        self.zoomChoose.setVisible(False)


        self.factor = QLineEdit(self)
        self.factor.setText("1")
        self.factor.setVisible(False)

        self.coordinates = QLineEdit(self)
        self.coordinates.setVisible(False)

        self.maskSize = QLineEdit(self)
        self.maskSize.setVisible(False)

        self.console = QTextEdit(self)
        self.console.setMaximumHeight(40)
        self.console.setDisabled(True)

        self.comboBox.addItem("Negative")
        self.comboBox.addItem("Gamma")
        self.comboBox.addItem("Logarithm")
        self.comboBox.addItem("Linear")
        self.comboBox.addItem("Zoom")
        self.comboBox.addItem("Equalize")
        self.comboBox.addItem("Adding mask")
        self.comboBox.addItem("Average")
        self.comboBox.addItem("Difference")
        self.comboBox.addItem("Blur")

        self.zoomChoose.addItem("Nearest neighbour interpolation")
        self.zoomChoose.addItem("Linear interpolation")

        self.button = QPushButton('Apply')
        self.button.clicked.connect(self.plot)

        self.selectButton = QPushButton("Select File")
        self.selectButton.clicked.connect(self.showDialog)

        grid = QGridLayout()

        grid.addWidget(self.toolbar)
        grid.addWidget(self.canvas)

        grid.addWidget(self.functionType)
        grid.addWidget(self.comboBox)

        grid.addWidget(self.coordinatesLabel)
        grid.addWidget(self.coordinates)

        grid.addWidget(self.zoomType)
        grid.addWidget(self.zoomChoose)

        grid.addWidget(self.factorLabel)
        grid.addWidget(self.factor)

        grid.addWidget(self.consoleMessage)
        grid.addWidget(self.console)

        grid.addWidget(self.selectedFile)
        grid.addWidget(self.button)
        grid.addWidget(self.selectButton)

        self.setLayout(grid)

    def plot(self):

        typeFunc = self.comboBox.currentIndex() + 1
        typeZoom = self.zoomChoose.currentIndex() + 1

        array = [0, 0]
        self.console.setText("")

        try:

            array = list(map(int, self.coordinates.text().split()))

        except(TypeError, ValueError):

            if typeFunc == 6:
                self.console.setText("Please, enter correct array")

        except:

            array = [0, 0, 0, 0]

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

        try:

            ax.imshow(computeImage(typeFunc, filename, factor, typeZoom, array), cmap="gray")

        except:

            self.console.setText("Error")

        self.canvas.draw()

    def showDialog(self):

        if self.type == 8:

            self.filename = QFileDialog.getOpenFileNames(self, 'Open files')[0]


        elif self.type == 7:

            self.filename = QFileDialog.getExistingDirectory(self, "Select Directory")
            self.selectedFile.setText(self.filename)

        else:

            self.filename = QFileDialog.getOpenFileName(self, 'Open file')[0]

            self.selectedFile.setText(self.filename)



    def selectedFunction(self):

        self.type = self.comboBox.currentIndex()

        if self.comboBox.currentIndex() == 1 or self.comboBox.currentIndex() == 4:

            self.factorLabel.setVisible(True)
            self.factor.setVisible(True)
        else:

            self.factorLabel.setVisible(False)
            self.factor.setVisible(False)

        if self.comboBox.currentIndex() == 4:

            self.zoomType.setVisible(True)
            self.zoomChoose.setVisible(True)
        else:

            self.zoomType.setVisible(False)
            self.zoomChoose.setVisible(False)

        if self.comboBox.currentIndex() == 6:

            self.coordinates.setVisible(True)
            self.coordinatesLabel.setVisible(True)
        else:

            self.coordinates.setVisible(False)
            self.coordinatesLabel.setVisible(False)

        if self.comboBox.currentIndex() == 9:

            self.factorLabel.setVisible(True)
            self.factor.setVisible(True)
            self.factorLabel.setText("Mask size")
        else:

            self.factorLabel.setVisible(False)
            self.factor.setVisible(False)
            self.factorLabel.setText("Factor")




if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Widget()
    main.show()

    sys.exit(app.exec_())