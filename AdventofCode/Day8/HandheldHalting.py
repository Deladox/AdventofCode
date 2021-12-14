


def reader(list, line, accum):
    if line in visited:
        print("fail")
        return accum
    visited.append(line)
    thisline = list[line]
    word = thisline[0:3]
    nbr = int(thisline[4:])
    if word == "acc":
        accum += nbr
        print(accum)
        reader(list, line+1, accum)
    elif word == "jmp":
        jumpers.append(line)
        reader(list, line+nbr, accum)
    elif word == "nop":
        nopers.append(line)
        reader(list, line+1, accum)

with open("input.txt") as f:
    visited = []
    jumpers = []
    nopers = []
    read = f.readlines()
    accum = 0
    reader(read, 0, accum)
    jumpers.sort()
    nopers.sort()
    print(len(jumpers))
    print(jumpers)
    print(len(nopers))
    print(nopers)

    #211 is the line where there is an error with jmp/nop