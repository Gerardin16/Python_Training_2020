# file name exists in the current folder, raise an execption
try:
    fileHander = open("testing_demo")
    count = 0 
    for lines in fileHander:
        count += 1
    
    print('Lines {}'.format(count))
except:
    print('error happned')



