from abstract_input import AbstractInput


class InputGender(AbstractInput):
    """ docstring for InputEmployeeId"""

    def __init__(self):
        self.id = 'InputGender'

    def input(self):
        while True:
            try:
                input_data = self.__view.input("Please input gender M/F : ")
                if self.validator.is_valid_gender(input_data):
                    break
                else:
                    self.__view.show("That was no valid input.  Try again...")
            except ValueError:
                self.__view.show(
                    "Oops!  That was no valid number.  Try again...")
        return {"Gender": input_data}
