# """
# >>> model = new Model()
# >>> data = ["EMPID" : 'A123', ""]
# >>> model.add_the_employee()

# """
from employee import Employee


class Model(object):

    """docstring for Model"""

    def __init__(self):
        self.employees = []

    def add_the_employee(self, data):
        result = ""
        sign   = True
        # new_employee = Employee(data['EMPID'], data['Gender'], data['Age'], data[
        #                         'Sales'], data['BMI'], data['Salary'], data['Birthday'])
        new_employee = Employee(data)
        for e in self.employees:
            if e.id == new_employee.id:
                result = "unique constraint failed"
                sign = False
        if sign :
            result = new_employee      
            self.employees.append(new_employee)
        # print(self.employees)
        return result

    def get_all_salaries(self):
        salary_list = []
        for employee in self.employees:
            salary_list.append(int(employee.salary))
        return salary_list

    def get_all_sales(self):
        sales_list = []
        for employee in self.employees:
            sales_list.append(int(employee.sales))
        return sales_list

    def get_all_age(self):
        age_list = []
        for employee in self.employees:
            age_list.append(int(employee.age))
        age_list.sort()
        return age_list


# if __name__ == "__main__":
#     import doctest
#     doctest.testmod(verbose=True)
