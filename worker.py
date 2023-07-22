from cmath import sin
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog,QComboBox 
import sys
# from skimage.color import rgb2gray
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets 
import matplotlib.pyplot as plt
from GUI import Ui_MainWindow
import logging
import qdarkstyle
import math
from scipy.integrate import quad


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)
        self.gui.pushButton.clicked.connect(self.maxHeight)
        self.show()
	# def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.gui = Ui_MainWindow()
    #     self.gui.setupUi(self)
	# 	# Load the ui file

	# 	# Define our widgets
	# 	self.button = self.findChild(QPushButton, "pushButton")
    def maxHeight(self):
        self.g = 9.8
        self.distance = int(self.gui.textEdit_3.toPlainText())
        print(self.distance)
        self.angle = int(self.gui.textEdit.toPlainText())
        type(self.angle)

        self.velocity = int(self.gui.textEdit_2.toPlainText())
        print(self.velocity)

        self.t = (self.velocity * math.sin(math.radians(self.angle)))/self.g
        self.h = round((self.velocity * self.t * math.sin(math.radians(self.angle))) - (0.5 * self.g * self.t * self.t),3)
        self.gui.textEdit_4.setText(str(self.h))

        self.s = self.velocity * math.cos(math.radians(self.angle)) *self.t
        print(self.s)
        self.s_bar = self.distance - self.s
        self.tow = self.s_bar/(self.velocity * math.cos(math.radians(self.angle)))

        self.h_bar = round(self.h - (0.5 * self.g * self.tow * self.tow),3)

        self.gui.textEdit_5.setText(str(self.h_bar))



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    Interpoltor = MainWindow()
    logger = logging.getLogger("main.py")
    logger.setLevel(level=logging.DEBUG)
    logging.basicConfig(filename="logging_file.log")
    logger.info("lunching of the Application ")
    sys.exit(app.exec_())