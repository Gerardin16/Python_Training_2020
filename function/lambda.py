def sum(a,b):
    return a + b

def main():
    #a = sum(2,3)
    #print(a)

    sum = lambda a, b: a +b

    x = lambda a,b: a-b

    print(x(5,2))
    print(sum(2,3))

main()