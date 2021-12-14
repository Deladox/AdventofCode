import numpy as np

def createBoard(board):
    for i, line in enumerate(board):
        board[i] = line.split(" ")
        board[i] = [x for x in board[i] if x != ""]
        for j, x in enumerate(board[i]):
            board[i][j] = board[i][j].strip()
            board[i][j] = int(x)
    board = np.array(board)
    #print(board)
    return board

def updateBoards(boards, nbr):
    for board in boards:
        if nbr in board:
            index = np.where(board == nbr)
            board[index[0][0]][index[1][0]] = 0
    return boards

def winCheck(boards):
    finishedBoards = []
    indexes = []
    for j, board in enumerate(boards):
        for i in range(len(board)):
            if sum(board[i,:]) == 0 or sum(board[:,i]) == 0:
                finishedBoards.append(board)
                indexes.append(j)
    return finishedBoards, True, list(set(indexes))

with open("input.txt") as f:
    read = [line.strip() for line in f.readlines()]
    draws = read[0].split(",")
    read = read[1:]
    boards = []
    check = False
    for i, line in enumerate(read):
        if line == "":
            boards.append(createBoard(read[i+1:i+6]))
    for x in draws:
        print(len(boards))
        boards = updateBoards(boards, int(x))
        winboard = winCheck(boards)
        if winboard[1] == True:
            for i, y in enumerate(winboard[2]):
                if len(boards) == 1:
                    #print(winboard[0])
                    #winboard[0].pop(0)
                    print(winboard[0])
                    print(x)
                    #print(sum(sum(winboard[0])))
                    break
                boards.pop(winboard[2][i]-i)

