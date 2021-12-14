
import re
from typing import overload
import numpy as np


def diagLines(coords, overlaps):
    twoLine = 0
    diagLines = [x for x in coords if not (x[0] == x[2] or x[1] == x[3])]
    for line in diagLines:
        x1, y1, x2, y2 = int(line[0]), int(line[1]), int(line[2]), int(line[3])
        xpath = np.arange(x1,x2+1)
        if not len(xpath) > 0:
            xpath = np.arange(x1,x2-1,-1)
        ypath = np.arange(y1,y2+1)
        if not len(ypath) > 0:
            ypath = np.arange(y1,y2-1,-1)
        for i, j in zip(xpath, ypath):
            overlaps[j, i] += 1
            if overlaps[j, i] == 2:
                twoLine += 1
            #print(i,j)
            #print(overlaps)
    print(twoLine)

def lines(coords):
    straightLines = [x for x in coords if x[0] == x[2] or x[1] == x[3]]
    overlaps = np.zeros((1000,1000))
    twoLine = 0
    for line in straightLines:
        y1, x1, y2, x2 = int(line[0]), int(line[1]), int(line[2]), int(line[3])
        if x1 - x2 == 0:
            path = np.arange(y1,y2+1)
            if not len(path) > 0:
                path = np.arange(y2,y1+1)
            for i in path:
                overlaps[x1, i] += 1
                if overlaps[x1, i] == 2:
                    twoLine += 1
        elif y1 - y2 == 0:
            path = np.arange(x1,x2+1)
            if not len(path) > 0:
                path = np.arange(x2,x1+1)
            for i in path:
                    overlaps[i, y1] += 1
                    if overlaps[i, y1] == 2:
                        twoLine += 1
    print(twoLine)
    return overlaps


with open("input.txt") as f:
    read = [line.strip() for line in f.readlines()]
    for i, x in enumerate(read):
        read[i] = re.split(",| -> ", x)
    map = lines(read)
    #print(np.where(map > 0))
    diagLines(read, map)
    