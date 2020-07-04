def calualteHra(sal):
    hra = sal * .2
    lta = sal * .4
    return (hra, lta)

def printMe(name, sal, hra, lta):
    print("{} \n {} \n {} \n {}".format(name, sal, hra, lta))

def main():
    salary =  1000
    a,b = calualteHra(salary)
    printMe('stalin', salary, a, b)

main()
