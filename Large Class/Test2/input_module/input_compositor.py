import os
from importlib.machinery import SourceFileLoader
abstract_input = SourceFileLoader("abstract_input", os.getcwd(
	)+"\\input_module\\abstract_input.py").load_module()
from abstract_input import AbstractInput
input_age = SourceFileLoader("input_age", os.getcwd(
	)+"//input_module//input_age.py").load_module()
from input_age import InputAge
input_birthday = SourceFileLoader("input_birthday", os.getcwd(
	)+"//input_module//input_birthday.py").load_module()
from input_birthday import InputBirthday
input_BMI = SourceFileLoader("input_BMI", os.getcwd(
	)+"//input_module//input_BMI.py").load_module()
from input_BMI import InputBMI
input_employee_id = SourceFileLoader("input_employee_id", os.getcwd(
	)+"//input_module//input_employee_id.py").load_module()
from input_employee_id import InputEmployeeId
input_gender = SourceFileLoader("input_gender", os.getcwd(
	)+"//input_module//input_gender.py").load_module()
from input_gender import InputGender
input_salary = SourceFileLoader("input_salary", os.getcwd(
	)+"//input_module//input_salary.py").load_module()
from input_salary import InputSalary
input_sales = SourceFileLoader("input_sales", os.getcwd(
	)+"//input_module//input_sales.py").load_module()
from input_sales import InputSales


class InputCompositor(AbstractInput):
	""" docstring for InputCompositor"""

	def __init__(self, validator, view):
		self.objects_dict = []
		self.validator = validator
		self.view = view

	def input(self, data):
		result_data = dict()
		for obj in self.objects_dict:
			input_data.update(obj.input)
		return result_data

	# def add(self, id):
	# 	for obj in self.objects_dict:
	# 		if obj.id == id:
	# 			return obj
	# 		else:
	# 			self.objects_dict.update(id(self.validator, self.view))
	def add(self, newObj):
		for obj in self.objects_dict:
			if obj.id == newObj.id:
				return obj
		self.objects_dict.append(newObj)
		return newObj

	def get_input_object(self, id):
		for obj in self.objects_dict:
			if obj.id == id:
				return obj

	def delete(self, id):
		for obj in self.objects_dict:
			if obj.id == id:
				self.objects_dict.remove(obj)
				return True
		return False
