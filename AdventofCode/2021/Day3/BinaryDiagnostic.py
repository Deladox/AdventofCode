import numpy as np

with open("input.txt") as f:
    read = [line.strip() for line in f.readlines()]
    matrix = []
    epsilon = []
    gamma = []
    sums = []
    for i, x in enumerate(read):
        read[i] = list(x)
    for x in read:
        ints = [int(y) for y in x]
        matrix.append(ints)
    for i in range(len(matrix[1])):
        if len(matrix) == 1:
            break
        sums.append(sum(row[i] for row in matrix))
        print(sums)
        print(len(matrix))
        print(i)
        if sums[i] < len(matrix)/2:
            matrix = [x for x in matrix if x[i] == 1]
        else:
            matrix = [x for x in matrix if x[i] == 0]

    print(matrix)


    epsilon = 0b011001100111
    gamma = 0b101010000100
    epsilon = int(epsilon)
    gamma = int(gamma)
    print(gamma*epsilon)
