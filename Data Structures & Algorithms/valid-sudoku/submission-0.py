class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hor = [[] for i in range(9)]
        ver = [[] for i in range(9)]
        block = [[[] for j in range(3)] for i in range(3)]
        for i in range(9):
            for j in range(9):
                print(i,j)
                if board[i][j] not in list("123456789"): continue
                if board[i][j] in hor[i]: return False
                else: hor[i].append(board[i][j])
                if board[i][j] in ver[j]: return False
                else: ver[j].append(board[i][j])
                if board[i][j] in block[i//3][j//3]: return False
                else: block[i//3][j//3].append(board[i][j])
        print("hor",hor)
        print("ver",ver)
        print("block",block)
        return True
        