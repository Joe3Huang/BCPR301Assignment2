from datetime import date, datetime


class Employee(object):

    def __init__(self, parameter_object):
        self.parameter_object = parameter_object
        self.id = self.parameter_object['Id']
        self.gender = self.parameter_object['Gender']
        self.age = self.parameter_object['Age']
        self.sales = self.parameter_object['Sales']
        self.BMI = self.parameter_object['BMI']
        self.salary = self.parameter_object['Salary']
        self.birthday = datetime.strptime(
            self.parameter_object['Birthday'], '%d-%m-%Y')

    def __str__(self):
        txt = self.id + ',' + self.gender + ',' + \
            self.age + ',' + self.sales + ','
        txt += self.BMI + ',' + self.salary + \
            ',' + self.birthday.strftime('%d-%m-%Y')
        return txt
    # def speak(self):))
    #    print self.words
