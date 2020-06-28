numlist = list()
while True :
    print('Press Y to print the result')
    inp = input('Enter a number: ')
    if inp == 'Y' :
        break
    value = int(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print ('Average: {}'.format(average))