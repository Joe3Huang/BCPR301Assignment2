from abstract_input import AbstractInput


class InputBMI(AbstractInput):
    """ docstring for InputEmployeeId"""

    def __init__(self):
        self.id = 'InputBMI'
        self.validator = Validator()
    def input(self):
        options = ['Normal', 'Overweight', 'Obesity', 'Underweight']
        for (i, item) in enumerate(options):
            self.__view.show(i + 1, item)
        while True:
            try:
                input_data = int(
                    self.__view.input("Please select the BMI number:"))
                if input_data >= 1 and input_data <= 4:
                    input_data = options[input_data - 1]
                if self.validator.is_valid_BMI(input_data):
                    break
                else:
                    self.__view.show("That was no valid input.  Try again...")
            except ValueError:
                self.__view.show(
                    "Oops!  That was no valid number.  Try again...")
        return {"BMI": input_data}
