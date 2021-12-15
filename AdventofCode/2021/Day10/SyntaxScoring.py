import statistics


def decoder(input):
    start = ["(", "[", "{", "<"]
    end = [")", "]", "}", ">"]
    corrupted = []
    currOpen = []
    for i, line in enumerate(input):
        syntaxList = []
        for x in line:
            syntaxList.append(x)
            if x in start:
                currOpen.append(x)
            if x not in start:
                if start[end.index(x)] == currOpen[-1]:
                    currOpen.pop()
                else:
                    corrupted.append(line)
                    break
    print(corrupted)
    incomplete = [x for x in input if x not in corrupted]
    return incomplete

def autocompleter(incomplete):
    start = ["(", "[", "{", "<"]
    end = [")", "]", "}", ">"]
    listofPoints = []
    for line in incomplete:
        currOpen = []
        for i, x in enumerate(line):
            if x in start:
                currOpen.append(x)
            if x not in start:
                if start[end.index(x)] == currOpen[-1]:
                    currOpen.pop()
            if i == len(line)-1:
                #remain = []
                points = 0
                for y in reversed(currOpen):
                    points = calculator(y, points)
                listofPoints.append(points)
                #    remain.append(end[start.index(y)])
                #completeLine = line.extend(remain)
    print(len(listofPoints))
    print(statistics.median(listofPoints))

def calculator(symbol, points):
    #print(f"current symbol: {symbol} And current points: {points}")
    if symbol == "(":
        points = points*5 + 1
    elif symbol == "[":
        points = points*5 + 2
    elif symbol == "{":
        points = points*5 + 3
    elif symbol == "<":
        points = points*5 + 4
    #print(f"points after symbolcheck: {points}")
    return points


with open("input.txt") as f:
    read = [line.strip() for line in f.readlines()]
    notcorrupted = decoder(read)
    print(len(notcorrupted))
    autocompleter(notcorrupted)
    #calculator(corrupted)
    #print(read)
