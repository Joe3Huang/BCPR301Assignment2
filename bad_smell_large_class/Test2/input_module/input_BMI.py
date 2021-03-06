from abstract_input import AbstractInput


class InputBMI(AbstractInput):
    """ docstring for InputEmployeeId"""

    def __init__(self, validator, view):
        self.id = 'InputBMI'
        self.validator = validator
        self.view = view
        
    def input(self, prompt, output_key, validator_method):
        options = ['Normal', 'Overweight', 'Obesity', 'Underweight']
        for (i, item) in enumerate(options):
            self.view.show(i + 1, item)
        while True:
            try:
                input_data = int(
                    self.view.input(prompt))
                if input_data >= 1 and input_data <= 4:
                    input_data = options[input_data - 1]
                if validator_method(input_data):
                    break
                else:
                    self.view.show("That was no valid input.  Try again...")
            except ValueError:
                self.view.show(
                    "Oops!  That was no valid number.  Try again...")
        return {output_key: input_data}
