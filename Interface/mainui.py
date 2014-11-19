#!/usr/bin/python

from PyQt4 import QtGui, QtCore
from pymongo import MongoClient
import pdb #use with pdb.set_trace()
import sys
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

		#for each element in self.worldMap[][], generate area data for each location
		iter = 0
		for j in self.worldMap:
			for k in range(self.width):
				#Randomize content - to be replaced with actual content generation in the future
				roll = numpy.random.randint(0,21)
				if roll < 7:
					imageurl = r'..\Assets\Images\fieldtree.bmp'
				else:
					imageurl = r'..\Assets\Images\field.bmp'

				area = {
					"position":{"x_loc":iter+1,"y_loc":k+1},
					"imageurl":imageurl
				}
				pdb.set_trace()
				AREAS.insert(area)
				#j[k] = Area(iter, k)
			iter = iter + 1

class Area:
	def __init__(self, x_loc, y_loc):
		self.x_loc = x_loc
		self.y_loc = y_loc
		#Set the bitmap that we're going to draw at location x,y
		#self.imagery = QBitmap.__init__()

		areaDocument = AREAS.find(position={'x_loc':x_loc,'y_loc':y_loc})

		self.image = QtGui.QImage(QtGui.QImage.Format_ARGB32)
		self.image.load(areaDocument[0]['imageurl'])
		self.label = QtGui.QLabel('')
		self.label.setPixmap(QtGui.QPixmap.fromImage(self.image))

class MainWindow(QtGui.QWidget):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.initUI()

	def initUI(self):
		'''Initiate Mongo connection'''
		global CLIENT 
		CLIENT = MongoClient('localhost', 27017)
		global DB
		DB = CLIENT.test_database
		global AREAS
		AREAS = DB.areas

		'''Create the layout itself for the mainWindow'''
		#Create a "layout", into which we draw, and tell it to use it
		layout = QtGui.QGridLayout(self)
		layout.setSpacing(0)
		self.setLayout(layout)

		'''World generation'''
		#instantiate a world object with x by y dimensions
		world = World(8,8)

		#display only the first 5x5 of the world.worldMap
		for j in range(5):
			for i in range(5):
				area = Area(j,i)
				layout.addWidget(area.label, area.x_loc, area.y_loc)

		'''Display mainWindow'''
		#Show it
		self.setGeometry(300, 300, 355, 280)
		self.setWindowTitle("Chechnya Adventure!")
		self.show()	

	#def walk(x_loc, y_loc):
		#pull the surrounding x,ys for the new centerpoint, then wipe and redraw the gridlayout

#MAIN LOOP FOR MAKING THINGS HAPPEN
def main():
	app = QtGui.QApplication(sys.argv)

	instance = MainWindow()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()