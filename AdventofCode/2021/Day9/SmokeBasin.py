import numpy as np

def checkBorders(i, j, imax, jmax, diag = False):
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

def recursiveBasin(i, j, map, thisBasin, visited):
    basinNeighbours = checkBorders(i, j, len(map)-1, len(map[0])-1)
    for k in basinNeighbours:
        if map[k] != "9" and k not in visited:
            thisBasin += 1
            visited.append(k)
            thisBasin, visited = recursiveBasin(k[0], k[1], map, thisBasin, visited)
    return thisBasin, visited

def findBasins(map):
    visited = []
    allBasins = []
    for i, x in enumerate(map):
        for j, y in enumerate(map[i]):
            coords = (i, j)
            if y != "9" and coords not in visited:
                basinSize = 1
                visited.append(coords)
                basinSize, visited = recursiveBasin(i, j, map, basinSize, visited)
                allBasins.append(basinSize)
    print(allBasins)
    

def lowPoints(heights):
    lowPointList = []
    for i, x in enumerate(heights):
        for j, y in enumerate(heights[i]):
            low = True
            neighbours = checkBorders(i, j, len(heights)-1, len(heights[0])-1)
            print(neighbours)
            print(i, j)
            for n in neighbours:
                print(f"if {heights[i,j]} is larger or equal than {heights[n[0], n[1]]}")
                if heights[i,j] >= heights[n[0], n[1]]:
                    print("poop")
                    low = False
            print(low)
            if low:
                print("hello")
                lowPointList.append(int(heights[i, j])+1)
    print(lowPointList)
    print(sum(lowPointList))


with open("input.txt") as f:
    read = [line.strip() for line in f.readlines()]
    basins = [[]]
    for i, x in enumerate(read):
        for j, y in enumerate(x):
            basins[i].append(y)
        basins.append([])
    basins.pop(len(basins)-1)
    npbasins = np.array(basins)
    #lowPoints(npbasins)
    findBasins(npbasins)