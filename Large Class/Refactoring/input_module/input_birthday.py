import os
from importlib.machinery import SourceFileLoader
abstract_input = SourceFileLoader("abstract_input", os.getcwd(
    )+"\\input_module\\abstract_input.py").load_module()
from abstract_input import AbstractInput

class InputBirthday(AbstractInput):
    """ docstring for InputBirthday"""

    def __init__(self, validator, view):
        self.id = 'InputBirthday'
        self.validator = validator
        self.view = view

    def input(self):
        prompt = "Please input the birthday day-month-year : "
        while True:
            try:
                input_data = self.view.input(prompt)
                if self.validator.is_valid_birthday(input_data):
                    break
                else:
                    self.view.show("That was no valid input.  Try again...")
            except ValueError:
                self.view.show(
                    "Oops!  That was no valid number.  Try again...")
        return {"Birthday": input_data}
