from abstract_input import AbstractInput


class InputSales(AbstractInput):
	""" docstring for InputEmployeeId"""

	def __init__(self, validator, view):
		self.id = 'InputSales'
		self.validator = validator
		self.view = view
		
	def input(self):
		while True:
			try:
				input_data = self.view.input(
					"Please input three digit sales : ")
				if self.validator.is_valid_sales(input_data):
					break
				else:
					self.view.show("That was no valid input.  Try again...")
			except ValueError:
				self.view.show(
					"Oops!  That was no valid number.  Try again...")
		return {"Sales": input_data}
