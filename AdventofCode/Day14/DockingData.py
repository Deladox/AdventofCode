def maskTransfer(mask, value):
    binvalue = bin(value)
    for x,y in enumerate(mask):
        if y != "X":
            binvalue[x+2] = y


with open("input.txt") as f:
    read = [line.strip() for line in f.readlines()]
    testval = 2
    testval2 = 6
    bintest2 = bin(testval2)
    bintest = bin(testval)
    for x, y in enumerate(bintest2):
        print(x)
        print(y)
    

    print(bintest2)
