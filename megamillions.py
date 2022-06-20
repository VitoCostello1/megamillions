"""
Program: musicplayerGUI.py (page 251)
Author: Vito 6/14/2022

GUI-based app to simulate the Mega Millions lottery number picks. Five random numbers between 1 and 70 and a "Mega Ball" between 1 and 25
**MUST install the pygame package by running: pip install pygame 
"""

from breezypythongui import EasyFrame
from tkinter.font import Font 
import random
# other imports

class MegaMillions(EasyFrame):
	# "ApplicationName" will change from project to project 

	# definition of the __init__() method which is our class constructor
	def __init__(self):
		# call the EasyFrame version of the __init__
		EasyFrame.__init__(self, title = "Mega Millions!", background = "blue")
		titleFont = Font(family = "Impact", size = 24, weight = "bold")
		megaBallFont = Font(family = "Impact", size = 19)
		self.addLabel(text = "Mega Millions!", row = 0, column = 0,  font = titleFont, background = "blue", foreground = "yellow", sticky = "NSEW", columnspan = 5)
		# drawed numbers
		self.draw_1 = self.addIntegerField(value = 0, row = 1, column = 0,state = "readonly",sticky = "NE")
		self.draw_2 = self.addIntegerField(value = 0, row = 1, column = 1,state = "readonly", sticky = "NE")
		self.draw_3 = self.addIntegerField(value = 0, row = 1, column = 2,state = "readonly", sticky = "NWE", width = 5)
		self.draw_4 = self.addIntegerField(value = 0, row = 1, column = 3,state = "readonly", sticky = "NE")
		self.draw_5 = self.addIntegerField(value = 0, row = 1, column = 4,state = "readonly", sticky = "NE")
		self.megaball =self.addIntegerField(value = 0, row = 4, column = 2, state = "readonly", sticky = "NSEW")
		self.addLabel(text = "Mega Ball!",foreground = "red", row = 2, column = 0, columnspan = 5 ,sticky = "NSEW", font = megaBallFont, background = "blue")
		self.addButton(text = "Draw!", row = 5, column = 0, command = self.draw, columnspan = 5)
	def draw(self):
		self.draw_1.setNumber(random.randint(1,70))
		self.draw_2.setNumber(random.randint(1,70))
		self.draw_3.setNumber(random.randint(1,70))
		self.draw_4.setNumber(random.randint(1,70))
		self.draw_5.setNumber(random.randint(1,70))
		self.megaball.setNumber(random.randint(1,25))
# definition of the main() method which will establish class objects
def main():
	# instantiate an object from the class into mainloop()
	MegaMillions().mainloop()

# global call to the main() method 
main()