import os
from validator import Validator
from serialization import Serialization
from graphy_display import Bar_chart
from db import DB
from abstract_controller import AbstractController
from importlib.machinery import SourceFileLoader

input_compositor = SourceFileLoader("input_compositor", os.getcwd()+"\\input_module\\input_compositor.py").load_module()
from input_compositor import InputCompositor
input_age = SourceFileLoader("input_age", os.getcwd(
    )+"//input_module//input_age.py").load_module()
from input_age import InputAge
input_birthday = SourceFileLoader("input_birthday", os.getcwd(
    )+"//input_module//input_birthday.py").load_module()
from input_birthday import InputBirthday
input_BMI = SourceFileLoader("input_BMI", os.getcwd(
    )+"//input_module//input_BMI.py").load_module()
from input_BMI import InputBMI
input_employee_id = SourceFileLoader("input_employee_id", os.getcwd(
    )+"//input_module//input_employee_id.py").load_module()
from input_employee_id import InputEmployeeId
input_gender = SourceFileLoader("input_gender", os.getcwd(
    )+"//input_module//input_gender.py").load_module()
from input_gender import InputGender
input_salary = SourceFileLoader("input_salary", os.getcwd(
    )+"//input_module//input_salary.py").load_module()
from input_salary import InputSalary
input_sales = SourceFileLoader("input_sales", os.getcwd(
    )+"//input_module//input_sales.py").load_module()
from input_sales import InputSales
class Controller(AbstractController):

    """ docstring for Controller"""

    def __init__(self, view, model):
        self.__view = view
        self.model = model
        self.validator = Validator()
        self.serialization = Serialization()
        self.bar_chart = Bar_chart()
        self.db = DB("company.db")
        self.input_compositor = InputCompositor(self.validator, self.__view)
        self.input_compositor.add(InputSales(self.validator, self.__view))
        self.input_compositor.add(InputSalary(self.validator, self.__view)) 
        self.input_compositor.add(InputGender(self.validator, self.__view))
        self.input_compositor.add(InputEmployeeId(self.validator, self.__view))
        self.input_compositor.add(InputBMI(self.validator, self.__view))
        self.input_compositor.add(InputBirthday(self.validator, self.__view))
        self.input_compositor.add(InputAge(self.validator, self.__view)) 

    def print_all_data(self):
        try:
            if self.model.employees.__len__() == 0:
                raise ValueError
            for employee in self.model.employees:
                self.__view.show(employee)
        except ValueError:
            self.__view.show('not data')

    def new_employee(self):
        input_data = dict(self.input_employee_id())
        input_data.update(self.input_birthday())
        input_data.update(self.input_gender())
        input_data.update(self.input_age())
        input_data.update(self.input_sales())
        input_data.update(self.input_BMI())
        input_data.update(self.input_salary())
        self.model.add_the_employee(input_data)
        self.__view.show(input_data)
        self.__view.show('success')

    def load_file(self, path):
        try:
            f = open(path, "r")
            lines = [line.rstrip('\n') for line in f]
            # print(lines)
            for the_line in lines:
                if self.validator.is_load_data(the_line):
                    array = the_line.split(',')
                    d = self.convert_dict("EMPID", array[0])
                    d.update(self.convert_dict("Gender", array[1]))
                    d.update(self.convert_dict("Age", array[2]))
                    d.update(self.convert_dict("Sales", array[3]))
                    d.update(self.convert_dict("BMI", array[4]))
                    d.update(self.convert_dict("Salary", array[5]))
                    d.update(self.convert_dict("Birthday", array[6]))
                    the_employee = self.model.add_the_employee(d)
                else:
                    self.__view.show("invalid data detected")
            f.close()
            self.__view.show("success")
        except IOError:
            self.__view.show('error : wrong path')

    def save_file(self, path):
        try:
            if(self.model.employees.__len__() == 0):
                raise ValueError
            f = open(path, "w+")
            for employee in self.model.employees:
                f.write(employee.__str__())
                f.write('\n')
                # f.truncate()
            f.close()
            self.__view.show('ok')
        except IOError:
            self.__view.show('error : wrong path')
        except ValueError:
            self.__view.show('not data')

    def convert_dict(self, key, string):
        d = dict({key: string})
        return d

    def serialise_objects(self, path):
        try:
            if os.path.exists(path) == False:
                raise IOError
            if self.model.employees.__len__() != 0:
                path += '/data.pickle'
                sf = self.serialization.open(path, "wb")
               # for employee in self.model.employees:
                self.serialization.dump(sf, self.model.employees)
                sf.close()
                self.__view.show("ok")
            else:
                raise ValueError
        except IOError:
            self.__view.show('error : wrong path')
        except ValueError:
            self.__view.show('data error')

    def pickle_load(self, path):
        try:
            #sf = self.serialization.open(path, "rb")
            with self.serialization.open(path, "rb") as f:
                object_list = self.serialization.load(f)
                if object_list == False:
                    raise ValueError
            valided_object_list = []
            for e in object_list:
                for ee in self.model.employees:
                    if ee.id == e.id:
                        self.__view.show('unique constraint failed')
                        valided_object_list.append(e)
            new = set(object_list) - set(valided_object_list)
            self.model.employees += list(new)
            for e in new:
                self.__view.show(e)
            f.close() 
        except IOError:
            self.__view.show('error : wrong path')
        except ValueError:
            self.__view.show('data error')
        except AttributeError:
            self.__view.show('error : wrong path')

    def display_bar(self):
        try:
            if(self.model.get_all_salaries().__len__() != 0):
                try:
                    os.remove('bar_chart.svg')
                except OSError:
                    pass
                self.bar_chart.title = 'Salary by Age'
                #self.bar_chart.delete('Salary')
                self.bar_chart.add('Salary', self.model.get_all_salaries())

                age_list = []
                for age in self.model.get_all_age():
                    age_list.append(str(age) + '-year-old')
                age_list.sort()
                self.bar_chart.x_labels = map(str, age_list)
                # self.bar_chart.render_to_png('/tmp/chart.png')
                self.bar_chart.render_to_file('bar_chart.svg')
                self.bar_chart.show_in_chrome('bar_chart.svg')
            else:
                raise ValueError
        except ValueError:
            self.__view.show('data error')

    def db_save(self):
        try:
            if(self.model.employees.__len__() == 0):
                raise Exception('no data to save')
            llist = []
            for employee in self.model.employees:
                string = employee.__str__()
                array = string.split(',')
                llist.append(tuple(array))
            self.__view.show(self.db.insert_employee_data(llist))
            self.__view.show('ok')
            # self.__view.show(llist)
        except Exception as e:
            self.__view.show(e)
        # except ValueError:
        #     self.__view.show('error')

    def db_load(self):
        try:
            l = self.db.fetch_all_employees()
            if(bool(l) == False):
                raise ValueError
            if l.__len__() == 0:
                raise ValueError
            for employee in l:
                d = self.convert_dict("EMPID", employee[0])
                d.update(self.convert_dict("Gender", employee[1]))
                d.update(self.convert_dict("Age", employee[2]))
                d.update(self.convert_dict("Sales", employee[3]))
                d.update(self.convert_dict("BMI", employee[4]))
                d.update(self.convert_dict("Salary", employee[5]))
                d.update(self.convert_dict("Birthday", employee[6]))
                the_employee = self.model.add_the_employee(d)
                self.__view.show(the_employee)
        except ValueError:
            self.__view.show('no data')

    def input_employee_id(self):
        inputObject= self.input_compositor.get_input_object('InputEmployeeId')
        return inputObject.input()

    def input_gender(self):
        inputObject= self.input_compositor.get_input_object('InputGender')
        return inputObject.input()

    def input_age(self):
        inputObject= self.input_compositor.get_input_object('InputAge')
        return inputObject.input()

    def input_sales(self):
        inputObject= self.input_compositor.get_input_object('InputSales')
        return inputObject.input()

    def input_BMI(self):
        inputObject= self.input_compositor.get_input_object('InputBMI')
        return inputObject.input()

    def input_salary(self):
        inputObject= self.input_compositor.get_input_object('InputSalary')
        return inputObject.input()

    def input_birthday(self):
        inputObject= self.input_compositor.get_input_object('InputBirthday')
        return inputObject.input()
