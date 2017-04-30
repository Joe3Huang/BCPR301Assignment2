
from abc import ABCMeta, abstractmethod
import datetime
import validator

# abstract factory


class AbstractChecker(metaclass=ABCMeta):
    """AbstractChecker"""
    @abstractmethod
    def check(self, data):
        pass
# singeton class inherit from AbstractChecker


class EmployeeIdChecker(object):

    class __EmployeeIdChecker(AbstractChecker):

        def check(self, input_data):
            result = False
            if input_data.__len__() > 0:
                num_ascii = ord(input_data[0])
                if num_ascii > 64 and num_ascii < 91:
                    int_digit = input_data[1::]
                    if int_digit.isdigit() and int_digit.__len__() == 3:
                        result = True
                    else:
                        result = False
                else:
                    result = False
            return result
    instance = None

    def __init__(self):
        if not EmployeeIdChecker.instance:
            EmployeeIdChecker.instance = EmployeeIdChecker.__EmployeeIdChecker()

    def __getattr__(self, name):
        return getattr(self.instance, name)


class GenderChecker(object):

    class __GenderChecker(AbstractChecker):

        def check(self, input_data):
            result = False
            if input_data == 'M' or input_data == 'F':
                result = True
            else:
                result = False
            return result
    instance = None

    def __init__(self):
        if not GenderChecker.instance:
            GenderChecker.instance = GenderChecker.__GenderChecker()

    def __getattr__(self, name):
        return getattr(self.instance, name)


class AgeChecker(object):

    class __AgeChecker(AbstractChecker):

        def check(self, input_data):
            result = False
            if input_data.isdigit() and input_data.__len__() == 2:
                result = True
            else:
                result = False
            return result
    instance = None

    def __init__(self):
        if not AgeChecker.instance:
            AgeChecker.instance = AgeChecker.__AgeChecker()

    def __getattr__(self, name):
        return getattr(self.instance, name)


class SalesChecker(object):

    class __SalesChecker(AbstractChecker):

        def check(self, input_data):
            result = False
            if input_data.isdigit() and input_data.__len__() == 3:
                result = True
            else:
                result = False
            return result
    instance = None

    def __init__(self):
        if not SalesChecker.instance:
            SalesChecker.instance = SalesChecker.__SalesChecker()

    def __getattr__(self, name):
        return getattr(self.instance, name)


class BMIChecker(object):

    class __BMIChecker(AbstractChecker):

        def check(self, input_data):
            result = False
            options = ['Normal', 'Overweight', 'Obesity', 'Underweight']
            if input_data in options:
                result = True
            else:
                result = False
            return result
    instance = None

    def __init__(self):
        if not BMIChecker.instance:
            BMIChecker.instance = BMIChecker.__BMIChecker()

    def __getattr__(self, name):
        return getattr(self.instance, name)


class SalaryChecker(object):

    class __SalaryChecker(AbstractChecker):

        def check(self, input_data):
            result = False
            if input_data.isdigit() and input_data.__len__() >= 2 and input_data.__len__() <= 3:
                result = True
            else:
                result = False
            return result
    instance = None

    def __init__(self):
        if not SalaryChecker.instance:
            SalaryChecker.instance = SalaryChecker.__SalaryChecker()

    def __getattr__(self, name):
        return getattr(self.instance, name)


class BirthdayChecker(object):

    class __BirthdayChecker(AbstractChecker):

        def check(self, input_data):
            result = False
            try:
                if(datetime.datetime.strptime(input_data, '%d-%m-%Y')):
                    date = datetime.datetime.strptime(input_data, '%d-%m-%Y')
                    if(date.year > datetime.datetime.now().year):
                        result = False
                    else:
                        result = True
                else:
                    result = False
                return result
            except ValueError:
                return False
    instance = None

    def __init__(self):
        if not BirthdayChecker.instance:
            BirthdayChecker.instance = BirthdayChecker.__BirthdayChecker()

    def __getattr__(self, name):
        return getattr(self.instance, name)


class Validator(object):

    """docstring for ClassName"""
    # def __init__(self):

    def is_valid_employee_id(self, input_data):
        checker = EmployeeIdChecker()
        return checker.check(input_data)

    def is_valid_gender(self, input_data):
        checker = GenderChecker()
        return checker.check(input_data)

    def is_valid_age(self, input_data):
        checker = AgeChecker()
        return checker.check(input_data)

    def is_valid_sales(self, input_data):
        checker = SalesChecker()
        return checker.check(input_data)

    def is_valid_BMI(self, input_data):
        checker = BMIChecker()
        return checker.check(input_data)

    def is_valid_salary(self, input_data):
        checker = SalaryChecker()
        return checker.check(input_data)

    def is_valid_birthday(self, input_data):
        checker = BirthdayChecker()
        return checker.check(input_data)

    def is_load_data(self, input_data):
        result = True
        checker_list = ['EmployeeIdChecker', 'GenderChecker', 'AgeChecker', 'SalesChecker','BMIChecker', 'SalaryChecker', 'BirthdayChecker']
        datas = input_data.split(',')
        if(datas.__len__() == 7):
            for index, date in enumerate(datas):
                checker = getattr(validator, checker_list[index])()
                if checker.check(date) == False:
                    result = False
        return result
