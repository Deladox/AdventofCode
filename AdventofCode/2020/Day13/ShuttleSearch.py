

with open("input.txt") as f:
    read = [line.strip() for line in f.readlines()]
    buses = read[1].split(",")
    buses = [int(x) for x in buses if x != "x"]
    arr_time = int(read[0])
    close_val = 0
    for x in buses:
        div = arr_time/x
        mult = int(div) + 1
        if mult*x-arr_time < abs(close_val-arr_time):
            close_val = mult*x
            bus = x

    print(close_val)
    print("bus " + str(bus))
