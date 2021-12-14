

with open("input.txt") as f:
    read = f.readlines()
    for i in range(0, len(read)):
        read[i] = int(read[i])
    read.sort()
    ones = []
    threes = []
    onejolts = 1                #output to first adapter
    threejolts = 1              #built in adapter
    for i in range(1, len(read)):
        if read[i]-read[i-1] > 3:
            break
        elif read[i]-read[i-1] == 1:
            onejolts += 1
            ones.append(read[i-1])
        elif read[i]-read[i-1] == 3:
            threejolts += 1
            ones.append(read[i-1])
    print(onejolts*threejolts)
    print(ones)
    print(read)
