"""
Program: radiobuttondemo.py
Author: Serghie 10/19/20

This GUI-based program allows the user to select their food options via radio buttons and then outputs their selection.
"""

from breezypythongui import EasyFrame

class RadiobuttonDemo(EasyFrame):
	""" Allows the user to place a restaurant order from a set of radio button options."""

	def __init__(self):
		""" Sets up the window and the widgets."""
		EasyFrame.__init__(self, title = "Radio Button Demo")

		# Add the "Meat" label and group
		self.addLabel(text = "Meat", row = 0, column = 0)
		self.meatGroup = self.addRadiobuttonGroup(row = 1, column = 0, rowspan = 2)
		defaultRB = self.meatGroup.addRadiobutton(text = "Chicken")

		# Make the chicken radio button the pre-selected option
		self.meatGroup.setSelectedButton(defaultRB)

		# Add "Beef" to the "Meat" group
		self.meatGroup.addRadiobutton(text = "Beef")

		# Add the "Potato" label and group
		self.addLabel(text= "Potato", row = 0, column = 1)
		self.taterGroup = self.addRadiobuttonGroup(row = 1, column = 1, rowspan = 2)
		defaultRB = self.taterGroup.addRadiobutton(text = "French Fries")
	
		# Make the french fries radio button the pre-selected option
		self.taterGroup.setSelectedButton(defaultRB)

		# Add "Baked Potato" to the "Tater" group
		self.taterGroup.addRadiobutton(text = "Baked Potato")

		# Add the "Vegetable" label and group
		self.addLabel(text = "Vegetable", row = 0, column = 2)
		self.vegGroup = self.addRadiobuttonGroup(row = 1, column = 2, rowspan = 2)
		defaultRB = self.vegGroup.addRadiobutton(text = "Roasted Corn")

		# Make the roasted corn the pre-selected option
		self.vegGroup.setSelectedButton(defaultRB)

		# Add kale chips to the "Vegetable" group
		self.vegGroup.addRadiobutton(text = "Kale Chips")

		# Add the command button
		self.addButton(text = "Place Order", row = 3, column = 0, columnspan = 3, command = self.placeOrder)

	#Event handling method
	def placeOrder(self):
		""" Displays a message box with the order summary. It is not possible for there to be an empty selection or string because we have pre-selected choices."""
		message = ""
		message += self.meatGroup.getSelectedButton()["text"] + "\n\n"
		message += self.taterGroup.getSelectedButton()["text"] + "\n\n"
		message += self.vegGroup.getSelectedButton()["text"] + "\n\n"

		# Generate a message dialog with message variable text
		self.messageBox(title = "Customer Order", message = message)

# Definition of the main function
def main():
	RadiobuttonDemo().mainloop()

# Global call to the main() function
main()

