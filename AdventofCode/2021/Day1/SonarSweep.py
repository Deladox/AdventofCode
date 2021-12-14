

with open("input.txt") as f:
    read = [line.strip() for line in f.readlines()]
    count = 0
    nbrs = [0,1,2]
    for i in range(len(read)):
        read[i] = int(read[i])
        if i not in nbrs:
            Aval = read[i-3] + read[i-2] + read[i-1]
            Bval = read[i-2] + read[i-1] + read[i]
            if Bval > Aval:
                count += 1

    print(count)