class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen =set()
            for c in range(9):
                if board[row][c]==".":
                    continue
                if board[row][c] in seen:
                    return False
                seen.add(board[row][c])
        
        for col in range(9):
            seen =set()
            for r in range(9):
                if board[r][col]==".":
                    continue
                if board[r][col] in seen:
                    return False
                seen.add(board[r][col])

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3)*3 + i
                    col = (square%3)*3 + j
                    if board[row][col]==".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True