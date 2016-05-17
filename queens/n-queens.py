# naive n-queens

N = 4


def check(board, i, j):
    # a queen moves horizontally (left and right) but in our case this is redundant 
    # since queens are placed in different rows

    # a queen moves vertically down
    for a in range(i + 1, N):
        if board[a][j]:
            return False

    # a queen moves vertically up
    for a in range(i-1, -1, -1):
        if board[a][j]:
            return False

    # a queen moves diagonally bottom - right
    for a, b in zip(range(i + 1, N), range(j+1,N)):
        if board[a][b]:
            return False

    # a queen moves diagonally top - left
    for a,b in zip (range(i-1, -1, -1), range(j-1, -1, -1)):
        if board[a][b]:
            return False

    # a queen moves diagonally top - right
    for a,b in zip( range(i-1, -1, -1), range(j+1,N)):
        if board[a][b]:
            return False

    # a queen moves diagonally bottom - left
    for a, b in zip(range(i + 1, N), range(j-1, -1, -1)):
        if board[a][b]:
            return False

    return True


def isSafe(board):  # checks if the queens can kill anything
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                if not check(board, i, j):
                    return False
    return True


def allocate(board, queen, i):
    board[queen][i] = 1
    board[queen][i - 1] = 0

def cvt(n,N):
    res = ""
    s = n
    while ( s != 0):
        r = s % N
        s = s / N
        res += str(r)
    return res[::-1]

def nxt(counter):
    n = int(counter)
    n += 1
    b = cvt(n,N)
    z = "0" * (N-len(b))
    return n, z + b

def solve():
    board = []
    # setup the board
    for i in range(N):
        l = []
        for j in range(N):
            if j == 0:
                l.append(1)
            else:
                l.append(0)
        board.append(l)

    counter = 0
    strCounter = "0" * N

    while(len(strCounter) == N):
        counter, strCounter = nxt(counter)
        for i in range(N):
            allocate(board, i, int(strCounter[i]))
        if (isSafe(board)):
            print counter, board

solve()
