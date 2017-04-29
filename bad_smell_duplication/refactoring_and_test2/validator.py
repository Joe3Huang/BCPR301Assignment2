
from abc import ABCMeta, abstractmethod
import datetime

#abstract factory
class AbstractCheck(metaclass=ABCMeta):
    @abstractmethod
    def check(self, data):
        pass
#singeton class inherit from AbstractCheck
class EmployeeIdChecker(object):
    class __EmployeeIdChecker(AbstractCheck):
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
    class __GenderChecker(AbstractCheck):
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
    class __AgeChecker(AbstractCheck):
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
    class __SalesChecker(AbstractCheck):
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
    class __BMIChecker(AbstractCheck):
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
    class __SalaryChecker(AbstractCheck):
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
    class __BirthdayChecker(AbstractCheck):
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
        result = 0
        data = input_data.split(',')
        if(data.__len__() == 7):
            if(self.is_valid_employee_id(data[0])):
                result += 1
            if(self.is_valid_gender(data[1])):
                result += 1
            if(self.is_valid_age(data[2])):
                result += 1
            if(self.is_valid_sales(data[3])):
                result += 1
            if(self.is_valid_BMI(data[4])):
                result += 1
            if(self.is_valid_salary(data[5])):
                result += 1
            if(self.is_valid_birthday(data[6])):
                result += 1
        if(result == 7):
            return True
        else:
            return False

