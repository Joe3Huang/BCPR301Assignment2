from datetime import date, datetime
#from dateutil.parser import parse


class Employee(object):

    def __init__(self, parameter_object):
        self.id = parameter_object['Id']
        self.gender = parameter_object['Gender']
        self.age = parameter_object['Age']
        self.sales = parameter_object['Sales']
        self.BMI = parameter_object['BMI']
        self.salary = parameter_object['Salary']
        self.birthday = datetime.strptime(parameter_object['Birthday'], '%d-%m-%Y')

    def __str__(self):
        txt = self.id + ',' + self.gender + ',' + \
            self.age + ',' + self.sales + ','
        txt += self.BMI + ',' + self.salary + \
            ',' + self.birthday.strftime('%d-%m-%Y')
        return txt
    # def speak(self):))
    #    print self.words
