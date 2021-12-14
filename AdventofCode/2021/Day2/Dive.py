
with open("input.txt") as f:
    read = [line.strip() for line in f.readlines()]
    read = [line.split(' ') for line in read]
    for i in range(len(read)):
        read[i][1] = int(read[i][1])
    depth = 0
    horizontal = 0
    aim = 0
    for x in read:
        if x[0] == "forward":
            horizontal += x[1]
            depth += aim*x[1]
        if x[0] == "down":
            aim += x[1]
        if x[0] == "up":
            aim -= x[1]
    
    #print(read)
    print(depth*horizontal)