
def commands(value, command, deg, pos, waypos):
    dist = [waypos[0] - pos[0], waypos[1] - pos[1]]
    if command == "N":
        waypos = move_north(waypos, value)
    elif command == "S":
        waypos = move_south(waypos, value)
    elif command == "E":
        waypos = move_east(waypos, value)
    elif command == "W":
        waypos = move_west(waypos, value)
    elif command == "L":
        if value == 90:
            waypos = [waypos[0] - dist[0] - dist[1], waypos[1]-dist[1] + dist[0]]                           #counterclockwise 90 (x,y) --> (-y,x)
        if value == 180:
            waypos = [waypos[0] - 2*dist[0], waypos[1] - 2*dist[1]]                                         #180 (x,y) --> (-x,-y)
        if value == 270:
            waypos = [waypos[0] - dist[0] + dist[1], waypos[1] - dist[1] - dist[0]]                         #clockwise 90 (x,y) --> (y,-x)
    elif command == "R":
        if value == 90:
            waypos = [waypos[0] - dist[0] + dist[1], waypos[1] - dist[1] - dist[0]]
        if value == 180:
            waypos = [waypos[0]-2*dist[0], waypos[1]-2*dist[1]]
        if value == 270:
            waypos = [waypos[0] - dist[0] - dist[1], waypos[1]-dist[1] + dist[0]]
    elif command == "F":
        waypos = [waypos[0] + dist[0]*value, waypos[1] + dist[1]*value]
        pos = [waypos[0] - dist[0], waypos[1] - dist[1]]


        #deg = deg % 360
        #if deg == 90:
        #    pos = move_east(pos, value)
        #elif deg == 180:
        #    pos = move_south(pos, value)
        #elif deg == 270:
        #    pos = move_west(pos, value)
        #elif deg == 0:
        #    pos = move_north(pos, value)
    return waypos, pos, deg

def move_north(pos, value):
    pos[1] = pos[1] + value
    return pos

def move_south(pos, value):
    pos[1] = pos[1] - value
    return pos

def move_east(pos, value):
    pos[0] = pos[0] + value
    return pos

def move_west(pos, value):
    pos[0] = pos[0] - value
    return pos


with open("input.txt") as f:
    read = [line.strip() for line in f.readlines()]
    pos = [0, 0]
    deg = 90
    waypos = [10, 1]
    for x in read:
        waypos, pos, deg = commands(int(x[1:]), x[0], deg, pos, waypos)
        #print(waypos, pos)
        #print(x)
        #print(read[0])
    man_dist = abs(pos[0]) + abs(pos[1])
    print(man_dist)