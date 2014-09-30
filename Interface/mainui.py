#!/usr/bin/python

import sys
from PyQt4 import QtGui, QtCore
from numpy import *
import os

class Area:
	def __init__(self, x_loc, y_loc):
		self.x_loc = x_loc
		self.y_loc = y_loc
		#Set the bitmap that we're going to draw at location x,y
		#self.imagery = QBitmap.__init__()
		self.image = QtGui.QImage(QtGui.QImage.Format_ARGB32)
		self.image.load(r'..\Assets\Images\tim.bmp')

		self.label = QtGui.QLabel('')
		self.label.setPixmap(QtGui.QPixmap.fromImage(self.image))


class MainWindow(QtGui.QWidget):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.initUI()

	def initUI(self):
		#Create a "layout", into which we draw, and tell it to use it
		layout = QtGui.QGridLayout(self)
		self.setLayout(layout)

		#this will eventually be a call to find what Areas need displayed
		#for now, instantiate a 5x5 array matrix
		currentDisplayed = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]

		for j in range(len(currentDisplayed)):
			for i in range(len(currentDisplayed)):
				area = Area(currentDisplayed[j][j], currentDisplayed[j][i])
				layout.addWidget(area.label, area.x_loc, area.y_loc)

		#Show it
		self.setGeometry(300, 300, 355, 280)
		self.setWindowTitle("Chechnya Adventure!")
		self.show()	

#MAIN LOOP FOR MAKING THINGS HAPPEN
def main():
	app = QtGui.QApplication(sys.argv)

	instance = MainWindow()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()