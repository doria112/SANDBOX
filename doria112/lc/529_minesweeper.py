class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        moves = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0,1], [-1, 1]]
        
        def isValidPos(x: int, y: int) -> bool:
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
                return False
            return True
        
        def checkMines(board: List[List[str]], x: int, y:int) -> List[List[str]]:
            total = 0
            for m in moves:
                nx = x + m[0]
                ny = y + m[1]
                if isValidPos(nx, ny):
                    if board[nx][ny] == 'M':
                        total += 1
            return total
        
        x, y = click[0], click[1]
        # invalid click
        if not isValidPos(x, y):
            return board # do nothing
        if board[x][y] == 'M':
            board[x][y] = 'X'
            #return board
        if board[x][y] == 'E':
            mines = checkMines(board, x, y)
            if mines == 0:
                board[x][y] = 'B'
                for m in moves:
                    board = self.updateBoard(board, [x + m[0], y + m[1]])
            else:
                board[x][y] = str(mines)
        return board
