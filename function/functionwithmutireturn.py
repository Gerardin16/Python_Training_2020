def multireturn(number):
    if(number == 5):
        return 'a'
    else:
        return 'b'
    
    print('end')

def multireturnvoid():
    print('start')
    return
    print('end')

def main():
    #a = multireturn(3)
    #print(a)
    multireturnvoid()

main()

