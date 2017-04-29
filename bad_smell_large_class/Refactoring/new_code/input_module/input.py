from abc import ABCMeta, abstractmethod


class AbstractInput(metaclass=ABCMeta):

    @abstractmethod
    def input(self):
        pass

    def input(self, prompt, output_key, validator_method):
        while True:
            try:
                input_data = self.view.input(prompt)
                if validator_method(input_data):
                    break
                else:
                    self.view.show("That was no valid input.  Try again...")
            except ValueError:
                self.view.show(
                    "Oops!  That was no valid number.  Try again...")
        return {output_key: input_data}


class InputCompositor(AbstractInput):
    """ docstring for InputCompositor"""

    def __init__(self):
        self.objects_dict = []

    def input(self):
        result_data = dict()
        for obj in self.objects_dict:
            input_data.update(obj.input)
        return result_data

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


class InputSales(AbstractInput):
    """ docstring for InputEmployeeId"""

    def __init__(self, validator, view):
        self.id = 'InputSales'
        self.validator = validator
        self.view = view


class InputAge(AbstractInput):
    """ docstring for InputEmployeeId"""

    def __init__(self, validator, view):
        self.id = 'InputAge'
        self.validator = validator
        self.view = view


class InputBirthday(AbstractInput):
    """ docstring for InputBirthday"""

    def __init__(self, validator, view):
        self.id = 'InputBirthday'
        self.validator = validator
        self.view = view


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


class InputEmployeeId(AbstractInput):
    """ docstring for InputEmployeeId"""

    def __init__(self, validator, view):
        self.id = 'InputEmployeeId'
        self.validator = validator
        self.view = view


class InputGender(AbstractInput):
    """ docstring for InputEmployeeId"""

    def __init__(self, validator, view):
        self.id = 'InputGender'
        self.validator = validator
        self.view = view


class InputSalary(AbstractInput):
    """ docstring for InputSalary"""

    def __init__(self, validator, view):
        self.id = 'InputSalary'
        self.validator = validator
        self.view = view
