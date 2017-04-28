from abstract_input import AbstractInput


class InputAge(AbstractInput):
    """ docstring for InputEmployeeId"""

    def __init__(self, validator, view):
        self.id = 'InputAge'
        self.validator = validator
        self.view = view

    # def input(self):
    #     while True:
    #         try:
    #             input_data = self.view.input("Please input two digit age : ")
    #             if self.validator.is_valid_age(input_data):
    #                 break
    #             else:
    #                 self.view.show("That was no valid input.  Try again...")
    #         except ValueError:
    #             self.view.show(
    #                 "Oops!  That was no valid number.  Try again...")
    #     return {"Age": input_data}
