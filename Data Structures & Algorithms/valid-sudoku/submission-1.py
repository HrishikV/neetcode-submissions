class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            col_seen=set()
            row_seen=set()
            square_seen=set()
            for j in range(9):
                if board[i][j] in row_seen or board[j][i] in col_seen:
                    return False
                
                if board[i][j]!='.':
                    row_seen.add(board[i][j])
                
                if board[j][i]!='.':
                    col_seen.add(board[j][i])
            for k in range(3):
                for l in range(3):
                    row = (i//3)*3 +k
                    col= (i%3) *3  +l
                    if board[row][col] in square_seen:
                        return False
                    if board[row][col]!= '.':
                        square_seen.add(board[row][col])
        return True