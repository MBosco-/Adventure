#!/usr/bin/env python
#Map Structure
#Holds the coordinates of the map
class WorldMap:
	def worldGenerate:
		#create array x by y with x,y values


	def __init__(self):
		self.data = []

#Area Structure
#Holds the attributes for a specific coord on the map
class Area:
	def __init__(self):
		self.data = []


#Container Structure
#Item with an invetory, essentially
class Container:
	pass
#Item Structure
#Holds the attributes for a specific entity
class Item:
	pass

#Creature Structure
#Holds a nonplayer creature's carried loot and attributes
class Creature:
	pass

#Player Structure
#Holds stats and drop/spawn specifics for the player
#Holds Inventory as well
class Player:
	def __init__(self, name=None):
		self.name = name
		self.stats = []
		self.inventory = []

	def store():
		#MongoDB stuff to store player object