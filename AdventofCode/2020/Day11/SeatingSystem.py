import copy


def neighbours(top, left, right, bot, topright, topleft, botright, botleft):
    count = 0
    neighbourlist = [top, left, right, bot, topright, topleft, botright, botleft]
    count = neighbourlist.count(True)
    return count

def seating(seats):
    rounds = 1
    diff = True
    # 20211025 DO NOT TOUCH WORKS!!!! - JESPER     DOES NOT WORK...
    while diff:
        oldseats = copy.deepcopy(seats)
        for i in range(len(oldseats)):
            for j in range(len(oldseats[i])):
                if i > 0:
                    for x in range(0,i):
                        if oldseats[x][j] == "#":
                            top = True
                            break
                        else:
                            top = False
                    #top = oldseats[i-1][j]
                else:
                    top = False
                if i > 0 and j > 0:
                    for x in range(0,min(i,j)):
                        if oldseats[i-x-1][j-x-1] == "#":
                            topleft = True
                            break
                        else:
                            topleft = False
                    #topleft = oldseats[i-1][j-1]
                else:
                    topleft = False  
                if i > 0 and j < len(oldseats[i])-1: 
                    for x in range(1,min(i,len(oldseats[i])-j)):
                        if x != len(oldseats)-1:
                            if oldseats[i-x][j+x] == "#":
                                topright = True
                                break
                            else:
                                topright = False
                    #topright = oldseats[i-1][j+1]
                else:
                    topright = False
                if j > 0:
                    for x in range(0,j):
                        if oldseats[i][x] == "#":
                            left = True
                            break
                        else:
                            left = False
                    #left = oldseats[i][j-1]
                else:
                    left = False
                if j > 0 and i < len(seats)-1:
                    for x in range(1,min(len(seats)-i,j)):
                        if x != len(seats)-1:
                            if oldseats[i+x][j-x] == "#":
                                botleft = True
                                break
                            else:
                                botleft = False
                    #botleft = oldseats[i+1][j-1]
                else:
                    botleft = False
                if i == 1:
                    print(len(seats))
                if i < len(seats)-1:
                    for x in range(i+1,len(seats)):
                        if oldseats[x][j] == "#":
                            bot = True
                            break
                        else:
                            bot = False
                    #bot = oldseats[i+1][j]
                else:
                    bot = False
                if i < len(seats)-1 and j < len(oldseats[i])-1:
                    for x in range(1,len(oldseats)-max(i,j)):
                        if oldseats[i+x][j+x] == "#":
                            botright = True
                            break
                        else:
                            botright = False
                    #botright = oldseats[i+1][j+1]
                else:
                    botright = False
                if j < len(oldseats[i])-1:
                    for x in range(j+1,len(oldseats[i])):
                        if oldseats[i][x] == "#":
                            right = True
                            break
                        else:
                            right = False
                    #right = oldseats[i][j+1]
                else:
                    right = False

                if oldseats[i][j] == "#":
                    if neighbours(top, left, right, bot, topright, topleft, botright, botleft) >= 5:            #if 5 neighbours exist, seat becomes free
                        seats[i][j] = "L"

                if i >= 0 and i < len(oldseats) and j >= 0 and j < len(oldseats[0]):
                    
                    pass


        if oldseats == seats:
            occupied = 0
            diff == False
            for i in oldseats:
                occupied += i.count("#")
            print(occupied)
            break
        rounds += 1

with open("test.txt") as f:
    read = f.readlines()
    j = 0
    for line in read:
        listinread = []
        line = line.strip()
        for i in line:
            listinread.append(i)
        read[j] = listinread
        j += 1
    row = 1
    col = 1
    directions = [(-1, -1),
                (-1, 0),
                (-1, 1), 
                (0, 1), 
                (1, 1), 
                (1, 0), 
                (1, -1), 
                (0,-1)]
  
    for yincr, xincr in directions:
        yix, xix = row, col
        print(yix, xix)
        print(yincr, xincr)
    
    seating(read)