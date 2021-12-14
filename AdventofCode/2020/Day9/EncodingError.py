

def encoder(input, checksum):
    preamble = input[0:25]
    for line in input[25:]:
        nbr = int(line)
        if nbr not in checksum:
            #print(nbr)
            pass
        else:
            #print(nbr)
            preamble.append(nbr)
            preamble.pop(0)
            newpreamble = list(preamble)
            checksum = checksumcreator(newpreamble)

def checksumcreator(preamble2):
    for j in range(0, 25):
        for i in range(0, len(preamble2)):
            if preamble2[0] != preamble2[i]:
                checksum.append(preamble2[0]+preamble2[i])
        preamble2.pop(0)
    return checksum

def contiguous(input):
    nbr = 167829540
    for line1 in input:
        sum = 0
        visited = []
        for line2 in input:
            sum += int(line2)
            visited.append(line2)
            if sum == nbr:
                visited.sort()
                print(visited[0]+visited[-1])
                print(visited)
        input.pop(0)


with open("input.txt") as f:
    read = f.readlines()
    for i in range(0, len(read)):
        read[i] = int(read[i])
    preamble = read[0:25]
    checksum = []
    checksum = checksumcreator(preamble)
    encoder(read, checksum)
    contiguous(read)
    