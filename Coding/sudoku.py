from typing import List
import copy
ret = []

def solve(board: List, x: int, y: int):
    # print(f"x = {x}, y = {y}")
    if x == 8 and y == 9:
        ret.append(copy.deepcopy(board))
        return
    if y == 9:
        solve(board, x+1, 0)
        return
    if board[x][y] != 0:
        solve(board, x, y+1)
        return
    for num in range(1, 10):
        if check(board, x, y, num) is True:
            board[x][y] = num
            solve(board, x, y+1)
            board[x][y] = 0
    return


def check(board: List, x: int, y: int, num: int) -> bool:
    # check the raw
    # print(f"check x {x} y {y} num {num}")
    for i in range(9):
        if board[i][y] == num:
            return False
    for j in range(9):
        if board[x][j] == num:
            return False
    idx_x = x // 3
    idx_y = y // 3
    for i in range(3):
        for j in range(3):
            new_x = 3 * idx_x + i
            new_y = 3 * idx_y + j
            if board[new_x][new_y] == num:
                return False
    return True


if __name__ == '__main__':
    board = \
        [[0,8,0,1,0,0,7,9,5],
         [7,0,4,0,5,0,0,0,0],
         [0,5,0,0,7,0,0,0,0],
         [3,0,5,6,8,2,0,4,7],
         [0,0,6,0,1,0,0,2,0],
         [1,2,7,0,0,4,6,0,0],
         [0,0,0,0,2,8,0,5,1],
         [0,0,0,4,0,1,2,7,0],
         [0,0,0,7,0,0,9,3,8]]
    solve(board, 0, 0)
    print(ret)

    """
    [[
    [2, 8, 3, 1, 4, 6, 7, 9, 5], 
    [7, 6, 4, 8, 5, 9, 3, 1, 2], 
    [9, 5, 1, 2, 7, 3, 8, 6, 4], 
    [3, 9, 5, 6, 8, 2, 1, 4, 7], 
    [8, 4, 6, 9, 1, 7, 5, 2, 3], 
    [1, 2, 7, 5, 3, 4, 6, 8, 9], 
    [6, 7, 9, 3, 2, 8, 4, 5, 1], 
    [5, 3, 8, 4, 9, 1, 2, 7, 6], 
    [4, 1, 2, 7, 6, 5, 9, 3, 8]]]
    """