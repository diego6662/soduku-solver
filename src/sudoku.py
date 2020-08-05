import numpy as np

board = np.matrix([[0,0,0,1,0,0,5,0,2],[0,0,0,0,9,0,0,0,0],[0,9,8,5,0,0,0,7,0],[0,0,0,0,6,1,0,0,0],[0,0,5,0,0,0,0,4,0],[9,2,0,0,5,0,0,3,0],[0,0,0,7,0,4,0,0,8],[0,0,0,0,0,0,7,0,9],[3,5,0,0,0,0,0,0,6]])
def possible(y,x,n):
    global board
    for i in range(9):
        if board[y,i] == n:
            return False
    for i in range(9):
        if board[i,x] == n:
            return False

    Yn = (y // 3) * 3
    Xn = (x // 3) * 3

    for i in range(0,3):
        for j in range(0,3):
            if board[Yn + i, Xn + j] == n:
                return False
    return True

def solve():
    global board
    for y in range(0,9):
        for x in range(0,9):
            if board[y,x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        board[y,x] = n
                        solve()
                        board[y, x] = 0
                return
    print(board)
    input("uwu")

if __name__ == "__main__":
    solve()
            

