from abstract_input import AbstractInput
from validator import Validator


class InputBirthday(AbstractInput):
    """ docstring for InputBirthday"""

    def __init__(self):
        self.id = 'InputBirthday'
        self.validator = Validator()
    def input(self):
        prompt = "Please input the birthday day-month-year : "
        while True:
            try:
                input_data = self.__view.input(prompt)
                if self.validator.is_valid_birthday(input_data):
                    break
                else:
                    self.__view.show("That was no valid input.  Try again...")
            except ValueError:
                self.__view.show(
                    "Oops!  That was no valid number.  Try again...")
        return {"Birthday": input_data}
