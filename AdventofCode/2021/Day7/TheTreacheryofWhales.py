

with open("input.txt") as f:
    read = [line.strip() for line in f.readlines()]
    crabs = read[0]
    crabs = crabs.split(",")
    crabs = [int(x) for x in crabs]
    minfuel = 9837495*2036203570
    for x in range(max(crabs)):
        fuel = 0
        for y in crabs:
            fuel += abs(x-y)*(abs(x-y)+1)/2
        if fuel < minfuel:
            minfuel = fuel
    print(minfuel)
        