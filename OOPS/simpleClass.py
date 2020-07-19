class Employee:
    'Employee class this for more information'

    def setName(self, name):
        'sets the name in the object'
        self.name = name
        return
    
    def printname(self):
        'prints the name from the object'
        print(self.name)        
        return

def main():
    emp = Employee()
    emp1 = Employee()
    emp.setName('sdfsd')

    #Employee.setName(emp, 'asdas')
    #Employee.setName(emp1, 'asdas')

    #emp.setName('sdf')
    #print(emp.__dir__)
    #emp.setName('stalin')
    #emp.printname() __

    #print(type(emp))
    #print(dir(emp))

main()