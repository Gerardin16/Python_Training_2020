class base1(object):
    def fun1(self):
        print('base1')

class base2(object):
    def fun1(self):
        print('base2')

class base3(base2, base1):
    #  MRO - Method resolution Order
    def callParent(self):
        super().fun1()

def main():
    emp = base3()
    emp.callParent()


main()

