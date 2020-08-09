import sys,os

def main():
    para =len(sys.argv) - 1 
    print("Total Parameter: {}".format(para))
    for target_list in sys.argv:
        print(target_list)
        

main()