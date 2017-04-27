from abstract_input import AbstractInput


class InputAge(AbstractInput):
    """ docstring for InputEmployeeId"""

    def __init__(self):
        self.id = 'InputAge'

    def input(self):
    while True:
        try:
            input_data = self.__view.input("Please input employee ID : ")
            if self.validator.is_valid_employee_id(input_data):
                break
            else:
                self.__view.show("That was no valid id.  Try again...")
        except ValueError:
            self.__view.show(
                "Oops!  That was no valid number.  Try again...")
    return {"EMPID": input_data}
