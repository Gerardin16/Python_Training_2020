a = 10

def calling():
    global a
    print(a)

def main():
    global a
    a = a+ 20
    calling()

main()
