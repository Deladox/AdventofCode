

with open("input.txt") as f:
    read = [line.strip() for line in f.readlines()]
    buses = read[1].split(",")
    #buses = [int(x) for x in buses if x != "x"]
    nbrs = range(100000000000572,1000000000000000000000)
    x = nbrs[0]
    while True:
        if (x+44) % 613 == 0:
            if (x+7) % 37 == 0 and (x+13) % 401 == 0 and (x+27) % 17 == 0:
                print(x)
                if (x+32) % 19 == 0 and (x+36) % 23 == 0 and (x+42) % 29 == 0 and x % 13 == 0 and (x+85) % 41 == 0:
                    print(x)
                    break
            x += 613

print(buses)