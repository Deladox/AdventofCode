import numpy as np

def checkBorders(i, j, imax, jmax, diag = True):
    borders = [(i,j+1), (i, j-1), (i+1, j), (i-1, j)]
    diagborders = [(i+1,j+1), (i-1, j-1), (i+1, j-1), (i-1, j+1)]
    toCheck = []
    if diag:
        borders.extend(diagborders)

    for bi, bj in borders:
        if bi < 0 or bi > imax or \
            bj < 0 or bj > jmax:
            continue

        toCheck.append((bi, bj))
    return toCheck

def octoLights(octopus):
    onematrix = np.ones((10,10), int)
    flashCounts = 0
    for i in np.arange(1000):
        flashed = []
        flashing = []
        octopus += onematrix
        for index, x in np.ndenumerate(octopus):
            if x > 9:
                flashing.append(index)
        for y in flashing:
            octoneighbours = checkBorders(y[0], y[1], 9, 9)
            if y not in flashed:
                octopus[y] = 0
                flashed.append(y)
                flashCounts += 1
                for yIndex in octoneighbours:
                    if yIndex not in flashed:
                        octopus[yIndex] += 1
                    if octopus[yIndex] > 9 and yIndex not in flashing:
                        flashing.append(yIndex)
        if len(flashed) == 100:
            print(i)
            break
    print(flashCounts)


with open("input.txt") as f:
    read = [line.strip() for line in f.readlines()]
    octopus = [[]]
    for i, x in enumerate(read):
        for j, y in enumerate(x):
            octopus[i].append(int(y))
        octopus.append([])
    octopus.pop()
    octopus = np.array(octopus)
    octoLights(octopus)