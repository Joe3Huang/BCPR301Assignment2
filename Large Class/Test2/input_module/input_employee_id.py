from abstract_input import AbstractInput
from abstract_input import AbstractInput


class InputEmployeeId(AbstractInput):
    """ docstring for InputEmployeeId"""

    def __init__(self, validator, view):
        self.id = 'InputEmployeeId'
        self.validator = validator
        self.view = view

    def input(self):
        while True:
            try:
                input_data = self.view.input("Please input employee ID : ")
                if self.validator.is_valid_employee_id(input_data):
                    break
                else:
                    self.view.show("That was no valid id.  Try again...")
            except ValueError:
                self.view.show(
                    "Oops!  That was no valid number.  Try again...")
        return {"EMPID": input_data}
