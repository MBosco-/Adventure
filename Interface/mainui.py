#!/usr/bin/python

import sys
from PyQt4 import QtGui, QtCore
import numpy
import os

class World:
	def __init__(self, width, height):
		self.width = width
		self.height = height

		#Initialize the worldMap 2d array. IMPORTANT. Must allow dtype='object' to allow
		#the array to store arrays
		self.worldMap = numpy.empty((self.width, self.height), dtype='object')
		for j in range(self.height):
			self.worldMap[j] = numpy.arange(self.width)

		#for each element in self.worldMap[][], generate an Area() at that location
		iter = 0
		for j in self.worldMap:
			for k in range(self.width):
				j[k] = Area(iter, k)
			iter = iter + 1

class Area:
	def __init__(self, x_loc, y_loc):
		self.x_loc = x_loc + 1
		self.y_loc = y_loc + 1
		#Set the bitmap that we're going to draw at location x,y
		#self.imagery = QBitmap.__init__()
		self.image = QtGui.QImage(QtGui.QImage.Format_ARGB32)

		#Roll for yee
		roll = numpy.random.randint(0,21)
		if roll < 7:
			self.image.load(r'..\Assets\Images\yee.bmp')
		else:
			self.image.load(r'..\Assets\Images\tim.bmp')

		self.label = QtGui.QLabel('')
		self.label.setPixmap(QtGui.QPixmap.fromImage(self.image))


class MainWindow(QtGui.QWidget):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.initUI()

	def initUI(self):
		'''Create the layout itself for the mainWindow'''
		#Create a "layout", into which we draw, and tell it to use it
		layout = QtGui.QGridLayout(self)
		self.setLayout(layout)

		'''World generation'''
		#instantiate a world object with x by y dimensions
		world = World(8,8)

		#eventually, we'll be pulling the viewport here, but for now display entire world
		#display only the first 5x5 of the world.worldMap

		for j in range(5):
			for i in range(5):
				layout.addWidget(world.worldMap[j][i].label, world.worldMap[j][i].x_loc, world.worldMap[j][i].y_loc)

		'''Display mainWindow'''
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