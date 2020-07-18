def loopthroughlist(names):    
    for name in names:
        print('The eleemnt is {}'.format(name))

def main():
    # names = ['stalin', 'sobana', 'valan']
    names = []
    '''
    while True:
        name = input('Enter names : ')
        if(name == 'Y'): 
            break

        names.append(name)
    '''
    for item in range(0,5):
        name = input('Enter names : ')
        names.append(name)
        if(item == 3):
            break

    loopthroughlist(names)

    ages = [1,3,7,8,9,9]
    loopthroughlist(ages)

main()