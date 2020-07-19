class Employee:
    'this class holds employee properties'
    
    def setName(self, x):
        self.name = x
    
    def printName(self):
        print(self.name)

def main():
    emp = Employee()
    emp.setName('stalin')
    emp.printName()

main()