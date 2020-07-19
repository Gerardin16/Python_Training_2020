class employee(object):
    'sdfsdfsdf'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

class permanentEmployye(employee):
    
    def print(self):
        print('Emplpoyee Name : {} \n Age : {} \n sex : {}'.format(self.name, self.age, self.sex))

class salespermanentEmployye(permanentEmployye):
    pass

def main():
    emp = permanentEmployye('stalin', 40, 'M')
    emp.print()


main()