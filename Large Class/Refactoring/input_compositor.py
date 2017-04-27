from abstract_input import AbstractInput
from input_compositor import InputCompositor
from input_age import InputAge
from input_birthday import InputBirthday
from input_employee_id import InputEmployeeId
from input_BMI import InputBMI
from input_gender import InputGender
from input_salary import InputSalary
class InputCompositor(AbstractInput):
	""" docstring for InputCompositor"""

	def __init__(self):
		self.objects_dict = dict()
	def input(self, data):
		result_data = dict()
		for obj in self.objects_dict:
			input_data.update(obj.input)
		return result_data

	def add(self, id):
		for obj in self.objects_dict:
			if obj.id == id:
				return obj
			else:
				self.objects_dict.update(id())

	def get_input_object(self, id):
		return self.add(id)

	def delete(self, id):
		for obj in self.objects_dict:
			if obj.id == id:
				self.objects_dict.remove(obj)
				return True
		return False
