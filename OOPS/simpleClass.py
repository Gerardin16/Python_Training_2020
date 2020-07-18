class Employee:
    'Employee class this for more information'

    def setName(self, name):
        'sets the name in the object'
        self.name = name
        ddd = 'dfgdfg'
        return
    
    def printname(self):
        'prints the name from the object'
        print(self.name)        
        return

def main():
    emp = Employee()
    print(emp.__dir__)
    #emp.setName('stalin')
    #emp.printname() __

    #print(type(emp))
    #print(dir(emp))

main()