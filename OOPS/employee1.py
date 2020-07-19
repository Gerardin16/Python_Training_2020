class employee1(object):
    'sdfsdfsdf'
    count = 0

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        employee1.count = employee1.count + 1
    
    def printMe(self):
        print('Emplpoyee Name : {} \n Age : {} \n sex : {}'.format(self.name, self.age, self.sex))
    '''
    def employeeCount():
        print('Employee Count {}'.format(employee1.count))
    '''
    
    def empCount(cls):
        print('name : {}'.format(cls.count))

    def __del__(self):
        print('called')

def main():
    emp = employee1('stalin', 40, 'M')
    emp.printMe()

    emp1 = employee1('valan', 43, 'M')
    emp1.printMe()

    #employee1.employeeCount()
    emp.empCount()

main()
