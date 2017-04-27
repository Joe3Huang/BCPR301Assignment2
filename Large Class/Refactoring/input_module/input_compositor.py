from abstract_input import AbstractInput


class InputCompositor(AbstractInput):
	""" docstring for InputCompositor"""

	def __init__(self):
		self.objects_dict = dict()
		self.activeChild = self

	def input(self, data):
		result_data = dict()
		for obj in self.objects_dict:
			input_data.update(obj.input)
		return result_data

	def add(self, obj):
		if obj.id not in self.objects_dict:
			self.objects_dict.update(obj)

	def get_input_object(self, id):
		for obj in self.objects_dict:
		if obj.id == id:
		return obj
		return False

	def delete(self, id):
		for obj in self.objects_dict:
		if obj.id == id:
		self.objects_dict.remove(obj)
			return True
		return False
