test1 = [[
  "5","3",".", ".","7",".", ".",".","."]
,["6",".",".", "1","9","5", ".",".","."]
,[".","9","5", ".",".",".", ".","6","."]

,["8",".",".", ".","6",".", ".",".","3"]
,["4",".",".", "8",".","3", ".",".","1"]
,["7",".",".", ".","2",".", ".",".","6"]

,[".","6",".", ".",".",".", "2","8","."]
,[".",".",".", "4","1","9", ".",".","5"]
,[".",".",".", ".","8",".", ".","7","9"]]

test2 = [[
  "8","3",".", ".","7",".", ".",".","."]
,["6",".",".", "1","9","5", ".",".","."]
,[".","9","8", ".",".",".", ".","6","."]

,["8",".",".", ".","6",".", ".",".","3"]
,["4",".",".", "8",".","3", ".",".","1"]
,["7",".",".", ".","2",".", ".",".","6"]

,[".","6",".", ".",".",".", "2","8","."]
,[".",".",".", "4","1","9", ".",".","5"]
,[".",".",".", ".","8",".", ".","7","9"]]

def isValidSudoku(board):
    rows  = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
    cols  = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
    boxes = {(0,0): [], (0,1): [], (0,2): [], (1,0): [], (1,1): [], (1,2): [], (2,0): [], (2,1): [], (2,2): []}

    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] != '.':
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in boxes[r//3, c//3]
                    ):
                    
                    print(board[r][c], boxes[r//3, c//3])
                    return False
                
                rows[r].append(board[r][c])
                cols[c].append(board[r][c])
                boxes[r//3, c//3].append(board[r][c])

    return True
    
print(isValidSudoku(test1))