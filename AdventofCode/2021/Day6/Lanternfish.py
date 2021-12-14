

with open("input.txt") as f:
    read = [line.strip() for line in f.readlines()]
    fishes = read[0]
    fishes = fishes.split(",")
    fishes = [int(x) for x in fishes]
    betterfishes = [0,0,0,0,0,0,0,0,0]
    for x in fishes:
        betterfishes[x] += 1

    for i in range(256):
        newFishes = 0
        newFishes = betterfishes[0]
        betterfishes.pop(0)
        betterfishes.append(newFishes)
        betterfishes[6] += newFishes
    print(sum(betterfishes))
    print(len(fishes))
