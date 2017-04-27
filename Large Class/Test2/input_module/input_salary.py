from abstract_input import AbstractInput
from validator import Validator

class InputSalary(AbstractInput):
	""" docstring for InputSalary"""

	def __init__(self, validator, view):
		self.id = 'InputSalary'
		self.validator = validator
		self.view = view

	def input(self):
		while True:
			try:
				input_data = self.view.input(
					"Please input the 2or3 digit salary : ")
				if self.validator.is_valid_salary(input_data):
					break
				else:
					self.view.show("That was no valid input.  Try again...")
			except ValueError:
				self.view.show(
					"Oops!  That was no valid number.  Try again...")
		return {"Salary": input_data}
