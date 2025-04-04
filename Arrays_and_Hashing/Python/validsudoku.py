from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        boxesByRow = defaultdict(set)
        boxesByCol = defaultdict(set)
        smallBoxesByRowAndCol = defaultdict(set)
        
        rowLen = len(board)
        colLen = len(board[0])

        for i in range(rowLen):
            for j in range(colLen):
                val = board[i][j]
                if (val == '.'): 
                    continue

                if (val in boxesByRow[i] or 
                    val in boxesByCol[j] or
                    val in smallBoxesByRowAndCol[(i // 3, j //3)]):
                    return False

                boxesByRow[i].add(val)
                boxesByCol[j].add(val)
                smallBoxesByRowAndCol[(i // 3, j // 3)].add(val)
                
        return True